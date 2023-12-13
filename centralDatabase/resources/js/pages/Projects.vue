<script setup>
import { useRoute, useRouter } from 'vue-router';
import { onMounted, ref, computed } from 'vue';
import { usehandledataManager } from '@/composables/handledataManager.js';

const router = useRouter();
const route = useRoute();

const projectname = ref('');
const projects = ref([]);

const apiUrl = '/api/getUserProjects';
const { getData } = usehandledataManager(apiUrl);

async function fetchData() {
    try {
        const result = await getData(apiUrl);
        if (result) {
            projects.value = result.data;
            console.log('Datei wurde ausgewählt:', fileObject);
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

function addNewProject() {
    console.log('test');
}

function deleteProject(customIdName) {
    console.log('test');
}

function selectProject(project) {
    console.log('test');
}
</script>

<template>
    <div class="page">
        <customheader></customheader>
        <div class="wrapper center">
            <div class="projects">

                <div class="card-actions">
                    <button @click="addNewProject">CREATE</button>
                    <button>SHARE</button>
                </div>
                
                <div v-for="project in projects" class="project-card">
                    <div class="card-header">
                        <h3>{{ project.name }}</h3>
                    </div>

                    <div class="card-actions">
                        <button @click="deleteProject(project.customIdName)">Delete</button>
                        <button @click="selectProject(project)">Select</button>
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>
  
<script>

</script>
  
<style>
@import '@/sass/pages/projects.sass';
</style>