<script setup>
import { onMounted, ref, computed } from 'vue';
import { usehandledataManager } from '@/composables/handledataManager.js';

const dataManager = usehandledataManager();

const runtimeTranscription_ = ref("");
const transcription_ = ref([]);
const lang_ = ref("de-DE");
const startrec = ref(false);
let recognition;

// import { useFilesStore } from '@/stores/filesStore.js';
// const filesStore = useFilesStore();
// const fileObjects = ref(filesStore.getFileObjects);

const fileObjects = ref([]);
const filesDict = ref({});

//const apiUrl = '/api/getAllFiles';
const apiUrl = '/api/getUserFiles';
const { getData } = usehandledataManager(apiUrl);

const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
// const fileObjects = ref([]);

async function fetchData() {
    const result = await getData(apiUrl);
    if (result) {
        fileObjects.value = result.data;
        //console.log('Datei wurde ausgewählt:', fileObjects);
        sortdata();
        // filesStore.saveFileObjects(data);
    } else {
        console.error('Fehler beim Abrufen der Daten');
    }
}

async function sortdata() {
    const newfilesDict = {};
    //console.log('Z30:', fileObjects.value);
    alphabet.forEach((letter) => {
        // debugger;
        const filteredFiles = fileObjects.value.filter((fileObject) => {
            //console.log('Z34:', fileObject);
            const fileName = fileObject.filename.toUpperCase();
            return fileName.startsWith(letter);
        });

        // console.log('Sortierte Dateiobjekte nach Buchstaben:', filteredFiles);

        const sortedFiles = filteredFiles.sort((a, b) => {
            const fileNameA = a.filename.toUpperCase();
            const fileNameB = b.filename.toUpperCase();
            return fileNameA.localeCompare(fileNameB);
        });

        newfilesDict[letter] = sortedFiles;
    });

    filesDict.value = newfilesDict;
}

onMounted(() => {
    fetchData();
});

async function submitNewTxtToSelectedFile(event) {
    event.preventDefault();

    debugger;

    const selectedFileName = event.target.elements['category'].value;
    const message = event.target.elements['message'].value;

    if (!selectedFileName || !message) {
        console.error('Bitte wähle eine Datei aus und gib eine Nachricht ein.');
        return;
    }

    const fileObject = fileObjects.value.find(file => file.filename === selectedFileName);

    if (!fileObject) {
        console.error('Ausgewählte Datei nicht gefunden.');
        return;
    }

    const data = new FormData();
    data.append("filename", selectedFileName);
    data.append("message", message);

    dataManager
        .postData("/api/addFurtherTxt", data)
        .then((responseData) => {
            console.log('Antwort vom Server:', responseData);
            if (responseData) {
                document.getElementById('message').value = '';
                // newprojectbox.value = responseData.name;
            } else {
                console.error("Ungültige Serverantwort");
            }
        })
        .catch((error) => {
            console.error("Fehler beim Hochladen der Datei:", error);
        });
}

const transcriptionText = computed(() => {
    return transcription_.value.join("\n");
});

const startSpeechToTxt = () => {
    window.SpeechRecognition =
        window.SpeechRecognition ||
        window.webkitSpeechRecognition;

    recognition = new window.SpeechRecognition();
    console.log(recognition);

    recognition.lang = lang_.value;
    recognition.interimResults = true;

    recognition.addEventListener("result", event => {
        let text = Array.from(event.results)
            .map(result => result[0])
            .map(result => result.transcript)
            .join("");
        runtimeTranscription_.value = text;
    });

    recognition.start();
};

const stopSpeechToTxt = () => {
    if (recognition) {
        recognition.stop();
        transcription_.value.push(runtimeTranscription_.value);
        runtimeTranscription_.value = "";
    }
};
</script>

<template>
    <div class="voice center">
        <form class="form-container" @submit.prevent="submitNewTxtToSelectedFile">

            <div class="text-container">
                <textarea id="message" name="message" class="textresult textarea-focus-settings">{{ transcriptionText }}</textarea>
            </div>

            <div class="button-container">
                <div class="button-container-first">
                    <div class="choose-file-container">
                        <select class="primary-button" id="category" name="category" required>
                            <option value="" disabled selected>Wähle hier die Datei aus</option>

                            <template v-for="letter in Object.keys(filesDict)" :key="letter">
                                <optgroup :label="letter" v-if="filesDict[letter].length > 0">
                                    <option v-for="fileObject in filesDict[letter]" :key="fileObject.id"
                                        :value="fileObject.filename">
                                        {{ fileObject.filename }}
                                    </option>
                                </optgroup>
                            </template>

                        </select>
                    </div>
                    <div class="submit-btn-container">
                        <button class="primary-button" type="submit">Hinzufügen</button>
                    </div>
                </div>

                <div class="button-container-second">
                    <div class="speech-btn-container">
                        <button class="primary-button" @click="startSpeechToTxt">Aufnahme starten</button>
                    </div>

                    <div class="speech-btn-container">
                        <button class="primary-button" @click="stopSpeechToTxt">Aufnahme stoppen</button>
                    </div>
                </div>

            </div>
        </form>
    </div>
</template>

<script>
</script>

<style>
@import '@/sass/components/speech.sass';
</style>