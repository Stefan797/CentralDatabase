<script setup>
import { onMounted, ref, computed } from 'vue';
import { usehandledataManager } from '@/composables/handledataManager.js';

const fileObjects = ref([]);

const apiUrl = '/api/getAllFiles';
const { getData } = usehandledataManager(apiUrl);

const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');

async function fetchData() {
    const data = await getData(apiUrl);
    if (data) {
        fileObjects.value = data;
        console.log('Datei wurde ausgewählt:', fileObjects);
        // filesStore.saveFileObjects(data);
    } else {
        console.error('Fehler beim Abrufen der Daten');
    }
}

onMounted(() => {
    fetchData();
});

function selectFile(fileObject) {
    console.log('Datei wurde ausgewählt:', fileObject);
}

</script>

<template>
    <div class="page">
        <customheader></customheader>
        <div class="wrapper center">
            <div class="contacts">
                <h2>Kontakte</h2>

                <table>
                    <tbody>
                        <tr v-for="(letter, index) in alphabet" :key="index">
                            <td>{{ letter }}
                                <div>
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
</script>
  
<style>
@import '@/sass/pages/contacts.sass';
</style>