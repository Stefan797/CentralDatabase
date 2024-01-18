<script setup>
//import { ref, onMounted, watchEffect } from 'vue'; 
import { useSearchStore } from '@/stores/searchStore';

const searchStore = useSearchStore();

// onMounted(() => {
//   watchEffect(() => {
//     if (searchStore.searchActive) {
//       console.log('Die Suche ist aktiviert.');
//     } else {
//       console.log('Die Suche ist deaktiviert.');
//     }
//   });
// });
</script>

<template>
  <div class="page">
    <customheader></customheader>
    <div class="wrapper center column">
      <add></add>
      <speech></speech>
      <upload></upload>
    </div>
  </div>
  
  <search v-if="searchStore.searchActive"></search>
</template>

<script>
</script>
  
<style>
@import '@/sass/pages/home.sass';
</style>