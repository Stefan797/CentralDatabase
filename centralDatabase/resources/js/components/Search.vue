<script setup>
</script>

<template>
    <div class="search center">
        <div class="search-content column">
            <div class="results">
                <!-- <div style="overflow-y: scroll">
                </div> -->
            </div>
        </div>
    </div>
</template>

<script>
export default {
  methods: {
    // ... andere Methoden der search-Komponente ...
    activate(searchTerm) {
      // Implementiere die Logik für die Aktivierung oder Aktualisierung hier
      console.log('activate-Funktion wurde aufgerufen mit Suchbegriff:', searchTerm);
    }
  }
}
</script>
  
<style>
@import '@/sass/components/search.sass';   
</style>