<script setup>
import { ref } from 'vue';
import { useSearchStore } from '@/stores/searchStore';

const searchStore = useSearchStore();
const search = ref(searchStore.search);
</script>

<template>
    <div  class="search center">
        <div class="search-content column">
            <div class="results">
                <!-- <div style="overflow-y: scroll">
                </div> -->
                <h1>Test</h1>

                <pre v-for="result in searchStore.searchResults">
                    {{ result.filename }}
                    <!-- {{ result.user_id }} -->
                    <div v-html="result.file_content.replace(searchStore.searchQueries, `<span style='color: red;'>${searchStore.searchQueries}</span>`)"></div>
                </pre>
            </div>
        </div>
    </div>
</template>

<script>
</script>
  
<style>
@import '@/sass/components/search.sass';   
</style>