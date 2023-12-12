<script setup>
// import { onMounted, ref, computed } from 'vue';
// import { usehandledataManager } from '@/composables/handledataManager.js';

// const { getData } = usehandledataManager(apiUrl);

// const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
// const fileObjects = ref([]);

// async function fetchData() {
//   const result = await getData(apiUrl);
//   if (result) {
//     fileObjects.value = result.data;
//     console.log('Datei wurde ausgewählt:', fileObjects);
//   } else {
//     console.error('Fehler beim Abrufen der Daten');
//   }
// }

// onMounted(() => {
//   fetchData();
// });


</script>

<template>
  <div class="page">
    <customheader></customheader>
    <div class="wrapper center">
      <div class="indexcards">
        <h2>Karteikarten</h2>

      </div>
    </div>
  </div>
</template>

<script>
export default {
};
</script>
  
<style>
@import '@/sass/pages/indexcards.sass';
</style>