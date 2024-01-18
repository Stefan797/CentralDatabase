<script setup>
import { ref } from 'vue';
import { useSearchStore } from '@/stores/searchStore';

const searchStore = useSearchStore();
const search = ref(searchStore.search);
</script>

<template>
    <div  class="search">
        <div class="search-content column">
            <div class="results">
                <!-- <div style="overflow-y: scroll">
                </div> -->
                <h1>Treffer: </h1>

                <pre class="results-files" v-for="result in searchStore.searchResults">
                    <h1>{{ result.filename }}</h1>
                    
                    <div class="file-content" v-html="result.file_content.replace(searchStore.searchQueries, `<span class='highlighted-text'>${searchStore.searchQueries}</span>`)"></div>
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