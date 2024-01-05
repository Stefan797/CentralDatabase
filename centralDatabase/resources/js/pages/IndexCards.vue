<script setup>
import { onMounted, ref, computed } from 'vue';
import { usehandledataManager } from '@/composables/handledataManager.js';

const dataManager = usehandledataManager(); 

const indexcards = ref([]);
// const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
// const fileObjects = ref([]);

async function fetchData() {
    try {
        const result = await dataManager.getData('/api/getUserIndexCards');
        if (result) {
            indexcards.value = result.data;
            console.log('Datei wurde ausgewählt:', indexcards);
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
</script>
  
<style>
@import '@/sass/pages/indexcards.sass';
</style>