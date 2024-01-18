<script setup>
import { computed, ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { usehandledataManager } from '@/composables/handledataManager.js';
import { useFileStore } from '@/stores/fileStore';
import { useSearchStore } from '@/stores/searchStore';

const searchStore = useSearchStore();
const search = ref(searchStore.search);

const fileStore = useFileStore();
const fileContent = computed(() => fileStore.fileContent);
const dataManager = usehandledataManager();

const router = useRouter();
const route = useRoute();
const fileObject = ref([]);
// const fileContent = ref([]);
let textFileProcessed = false;
const filename = route.params.filename;
const apiUrl = `/api/files/getbyfilename/${filename}`;
const apiUrlSingleTxtFile = '/api/readAngularFile';
const { getData } = usehandledataManager(apiUrl);


async function fetchData() {
    try {
        const result = await getData(apiUrl);
        if (result) {
            fileObject.value = result.data;

            // console.log(fileObject.value);
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

async function save() {
    console.log(fileContent);

    if (fileContent.value) {

        // fileStore.setFileContent(neuerInhalt);

        const data = new FormData();
        data.append("filecontent", fileContent.value);
        data.append("filename", filename);
        dataManager
            .postData("/api/updateFileContent", data)
            .then((responseData) => {
                console.log('Antwort vom Server:', responseData);
                if (responseData) {
                    console.log(responseData.message);
                } else {
                    console.error("Ungültige Serverantwort");
                }
            })
            .catch((error) => {
                console.error("Fehler beim Hochladen der Datei:", error);
            });
    } else {
        console.log('File Content ist nicht verändert! Datei ist bereits so gespeichert');
    }
}
</script>


<template>
    <div class="page">
        <customheader></customheader>
        <div class="wrapper center">
            <div class="file-wrapper">
                <div class="file-settings">
                    <div class="file-name-container">
                        <h1>{{ fileObject.filename }}</h1>
                    </div>

                    <div class="file-edit">
                        <img @click="save()" src="/images/speichern.png" />
                    </div>

                </div>

                <codeDisplay :fileContent="fileContent"></codeDisplay>

            </div>
        </div>
    </div>

    <search v-if="search"></search>
</template>

<script>
</script>
  
<style>
@import '@/sass/pages/file.sass';
</style>