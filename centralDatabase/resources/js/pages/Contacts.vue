<script setup>
import { onMounted, ref, computed } from 'vue';
import { usehandledataManager } from '@/composables/handledataManager.js';

const dataManager = usehandledataManager(); 
const contacts = ref([]);

const fileObjects = ref([]);
const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');


async function fetchData() {
    try {
        const result = await dataManager.getData('/api/getUserContacts');
        if (result) {
            contacts.value = result.data;
            console.log('Datei wurde ausgewählt:', contacts);
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