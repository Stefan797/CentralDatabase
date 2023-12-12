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

  //console.log('Sortierte Dateiobjekte nach Buchstaben:', newfilesDict);
  filesDict.value = newfilesDict;
}

onMounted(() => {
  fetchData();
  //debugger;
});

function selectFile(fileObject) {
  const { filename } = fileObject;
  router.push({ name: 'File', params: { filename } });
}

</script>

<template>
  <div class="page">
    <customheader></customheader>
    <div class="wrapper center">
      <div class="directory">
        <h2>Verzeichnis</h2>

        <table>
          <tbody>
            <tr v-for="(letter, index) in alphabet" :key="index">
              <td>{{ letter }}
                <div class="files-container" v-for="fileObject in filesDict[letter]">
                  <p @click="selectFile(fileObject)">{{ fileObject.filename }}</p>
                  <!-- <p @click="selectFile(fileObject)"><a :href="fileObject.fileurl">{{ fileObject.filename }}</a></p> -->
                </div>
              </td>
            </tr>
          </tbody>
        </table>

      </div>
    </div>
  </div>
</template>

<script>
export default {
};
</script>
  
<style>
@import '@/sass/pages/directory.sass';
</style>