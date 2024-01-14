<script setup>
import { defineProps, onBeforeMount, computed, ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { usehandledataManager } from '@/composables/handledataManager.js';

const router = useRouter();
const route = useRoute();
const fileObject = ref([]);
const fileContent = ref([]);
let textFileProcessed = false;
const test = route.params.filename;
const apiUrl = `/api/files/getbyfilename/${test}`;
const apiUrlSingleTxtFile = '/api/readAngularFile';
const { getData } = usehandledataManager(apiUrl);

async function fetchDataSingleTxtFileAsString() {
    try {
        const resultSingleTxtFile = await getData(apiUrlSingleTxtFile);
        if (resultSingleTxtFile) {
            // fileContent.value = result.data;
            // console.log('Datei wurde ausgewählt:', fileContent);
            fileContent.value = String(resultSingleTxtFile.data).split('\n');
            console.log(typeof resultSingleTxtFile.data);
            console.log(resultSingleTxtFile.data);
        } else {
            console.error('Fehler beim Abrufen der Daten');
        }
    } catch (error) {
        console.error('Fehler beim Abrufen der Daten:', error);
    }
}

async function fetchData() {
    try {
        const result = await getData(apiUrl);
        if (result) {
            fileObject.value = result.data;
        } else {
            console.error('Fehler beim Abrufen der Daten');
        }
    } catch (error) {
        console.error('Fehler beim Abrufen der Daten:', error);
    }
}

onMounted(() => {
    fetchData();
});

const fileContentType = computed(() => {
    if (fileObject.value && fileObject.value.filename) {
        return getFileType(fileObject.value.filename)
    }
    return null
})

const getFileType = (filename) => {
    const extension = filename.split('.').pop().toLowerCase();
    if (extension === 'jpg' || extension === 'jpeg' || extension === 'png' || extension === 'gif') {
        return 'image';
    } else if (extension === 'mp4' || extension === 'webm' || extension === 'ogg') {
        return 'video';
    } else if (extension === 'txt' || extension === 'pdf' || extension === 'doc' || extension === 'docx') {
        if (!textFileProcessed) {
            fetchDataSingleTxtFileAsString();
            textFileProcessed = true;
        }
        return 'text';
    } else {
        return 'other';
    }
};

function copyLine(lineNumber) {
    const codeElement = codeContent.value;
    const lines = codeElement.textContent.split('\n');
    const lineToCopy = lines[lineNumber];
    console.log('Kopiere Zeile:', lineToCopy);
}
</script>


<template>
    <div class="page">
        <customheader></customheader>
        <div class="wrapper center">
            <div class="file-wrapper">
                <div class="file-name-container">
                    <h1>{{ fileObject.filename }}</h1>
                </div>

                <codeDisplay></codeDisplay>
                
            </div>
        </div>
    </div>
</template>

<script>
</script>
  
<style>
@import '@/sass/pages/file.sass';
</style>