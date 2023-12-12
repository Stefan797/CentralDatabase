<script setup>
import { useRoute, useRouter } from 'vue-router';
import { onMounted, ref, computed } from 'vue';
import { usehandledataManager } from '@/composables/handledataManager.js';

const router = useRouter();
const route = useRoute(); // Verwenden von useRoute, um auf Routeninformationen zuzugreifen

// let fileObject = null;
const fileObject = ref([]);

const test = route.params.filename; // Zugriff auf Routenparameter mit useRoute
console.log('Z11:', test);

const apiUrl = `/api/files/getbyfilename/${test}`; // Verwenden von Template-Literals, um die test-Variable zu interpolieren
const { getData } = usehandledataManager(apiUrl);

async function fetchData() {
  try {
    const result = await getData(apiUrl);
    if (result) {
      fileObject.value = result.data;
      console.log('Datei wurde ausgewählt:', fileObject);
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

// if (router.currentRoute.value.query.file) {
//   console.log('URL-Parameter:', router.currentRoute.value.query.file);
//   try {
//     fileObject = JSON.parse(decodeURIComponent(router.currentRoute.value.query.file));
//     console.log('File Object:', fileObject);
//   } catch (error) {
//     console.error('Fehler beim Parsen der JSON-Zeichenfolge:', error);
//   }
// }

const fileContentType = computed(() => {
    if(fileObject.value && fileObject.value.filename) {
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
        return 'text';
    } else {
        return 'other';
    }
};
</script>

<template>
    <div class="page">
        <customheader></customheader>
        <div class="wrapper center">
            <div class="file-wrapper">
                <h1>{{ fileObject.filename }}</h1>
                
                <div class="file-content-container" v-if="fileObject">
                    <div v-if="fileContentType == 'text'">
                        <embed :src="fileObject.fileurl">
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