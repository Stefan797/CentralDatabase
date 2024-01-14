<script setup>
import { ref, computed } from 'vue';

const runtimeTranscription_ = ref("");
const transcription_ = ref([]);
const lang_ = ref("de-DE");
const startrec = ref(false);
let recognition;

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

async function submitNewTxtToSelectedFile(event) {
    event.preventDefault();

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
                // newprojectbox.value = responseData.name;
                // fetchData();
            } else {
                console.error("Ungültige Serverantwort");
            }
        })
        .catch((error) => {
            console.error("Fehler beim Hochladen der Datei:", error);
        });
}
</script>

<template>
    <div class="voice center">
        <form class="form-container" @submit.prevent="submitNewTxtToSelectedFile">

            <div class="text-container">
                <textarea class="textresult textarea-focus-settings">{{ transcriptionText }}</textarea>
            </div>

            <div class="button-container">
                <div class="display-flex">
                    <div class="choose-file-container">
                        <select class="primary-button" id="category" name="category" required>
                            <option value="" disabled selected>Wähle hier die Datei aus</option>
                            <option value="Option 1">Option 1</option>
                            <option value="Option 2">Option 2</option>
                            <option value="Option 3">Option 3</option>
                        </select>
                    </div>
                    <div class="submit-btn-container">
                        <button class="primary-button" type="submit">Hinzufügen</button>
                    </div>
                </div>

                <div class="display-flex">
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