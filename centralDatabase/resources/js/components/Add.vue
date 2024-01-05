<script setup>
import { onMounted, ref, computed } from 'vue';
import { usehandledataManager } from '@/composables/handledataManager.js';
import { usehandleroutingManager } from '@/composables/handleroutingManager.js';
import { useRouter } from 'vue-router';
const router = useRouter();
const { goToPath } = usehandleroutingManager();
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

async function submitNewTxtToSelectedFile() {
    debugger;
    const submitEndpoint = '/api/addFurtherTxt';
    const selectedFileName = document.getElementById('category').value;
    const message = document.getElementById('message').value;

    if (!selectedFileName || !message) {
        console.error('Bitte wähle eine Datei aus und gib eine Nachricht ein.');
        return;
    }

    const fileObject = fileObjects.value.find(file => file.filename === selectedFileName);

    if (!fileObject) {
        console.error('Ausgewählte Datei nicht gefunden.');
        return;
    }

    const data = {
        filename: selectedFileName,
        message: message
        // Weitere Daten, die du möglicherweise senden musst
    };

    const result = await postData(submitEndpoint, data);
    if (result) {
        fileObjects.value = result.data;
        sortdata();
        console.log('Neue Nachricht wurde hinzugefügt.');
    } else {
        console.error('Fehler beim Hinzufügen der Nachricht.');
    }
}
</script>

<template>
    <div class="add center">
        <form class="form-container column">

            <div class="text-container">
                <textarea class="textarea-focus-settings" id="message" name="message" required>
                </textarea>
            </div>

            <div class="button-container">
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
                    <button @click="submitNewTxtToSelectedFile()" class="primary-button"
                        type="submit">Hinzufügen</button>
                </div>

            </div>
        </form>
    </div>
</template>

<script>
</script>
  
<style>
@import '@/sass/components/add.sass';</style>