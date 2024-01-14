<script setup>
import { ref } from 'vue';

const searchRef = ref(null);

const activateSearch = (searchTerm) => {
  // Überprüfe, ob searchRef korrekt zugewiesen ist, bevor darauf zugegriffen wird
  if (searchRef.value && typeof searchRef.value.activate === 'function') {
    // Aktiviere oder aktualisiere die search-Komponente mit dem Suchbegriff
    searchRef.value.activate(searchTerm);
  } else {
    console.error('searchRef ist nicht korrekt zugewiesen oder activate-Funktion fehlt.');
  }
};

const handleSearch = (result) => {
  // Hier kannst du auf das Suchergebnis reagieren, wenn die Suche abgeschlossen ist
  console.log('Suchergebnis:', result);
};
</script>

<template>
    <div class="page">
        <customheader :onSearchInput="activateSearch"></customheader>
        <div class="wrapper center column">
            <add></add>
            <speech></speech>
            <upload></upload>
            <search ref="searchRef" @search="handleSearch" class="d-none"></search>
        </div>
    </div>
</template>

<script>
export default {
  methods: {
    // ... andere Methoden der search-Komponente ...
    finishSearch(result) {
      this.$emit('search', result);
    }
  }
}
</script>
  
<style>
@import '@/sass/pages/home.sass';
</style>