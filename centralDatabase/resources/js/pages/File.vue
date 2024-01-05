<script setup>
import { useRoute, useRouter } from 'vue-router';
import { onMounted, ref, computed } from 'vue';
import { usehandledataManager } from '@/composables/handledataManager.js';
const router = useRouter();
const route = useRoute();
const fileObject = ref([]);
const fileContent = ref([]);
let textFileProcessed = false;
const test = route.params.filename;
// console.log('Z11:', test);
const apiUrl = `/api/files/getbyfilename/${test}`;
const apiUrlSingleTxtFile = '/api/readAngularFile';
const { getData } = usehandledataManager(apiUrl);

// async function fetchDataSingleTxtFileAsString() {
//     debugger;
//     try {
//         let resultSingleTxtFile;

//         // Überprüfe, ob die Datei bereits abgerufen wurde
//         if (!fileContent.value.length) {
//             resultSingleTxtFile = await getData(apiUrlSingleTxtFile);

//             if (resultSingleTxtFile) {
//                 fileContent.value = String(resultSingleTxtFile.data).split('\n');
//                 console.log(typeof resultSingleTxtFile.data);
//                 console.log(resultSingleTxtFile.data);
//             } else {
//                 console.error('Fehler beim Abrufen der Daten');
//             }
//         }
//     } catch (error) {
//         console.error('Fehler beim Abrufen der Daten:', error);
//     }
// }

async function fetchDataSingleTxtFileAsString() {
    // debugger;
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
    // debugger;
    try {
        const result = await getData(apiUrl);
        if (result) {
            fileObject.value = result.data;
            // console.log('Datei wurde ausgewählt:', fileObject);
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
    // debugger;
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

                <div class="file-content-container" v-if="fileObject">

                    <!-- <div v-if="fileContentType == 'text'">
                        <embed :src="fileObject.fileurl">
                    </div> -->
                    <div v-if="fileContentType === 'text'">
                        <pre>
                            <button v-for="(line, index) in fileContent" :key="index" @click="copyLine(index)">
                                {{ index + 1 }}
                            </button>
                            <!-- <code ref="codeContent">{{ fileContent.join('\n') }}</code> -->
                        </pre>
                    </div>
                    <div v-else-if="fileContentType == 'image'">
                        <img :src="fileObject.fileurl">
                    </div>
                    <div v-else-if="fileContentType == 'video'">
                        <video :src="fileObject.fileurl" controls></video>
                    </div>
                    <div v-else>Nichts!</div>


                </div>

            </div>
        </div>
    </div>
</template>

<script>
</script>
  
<style>
@import '@/sass/pages/file.sass';
</style>