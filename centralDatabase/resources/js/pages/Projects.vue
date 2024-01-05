<script setup>
import { useRoute, useRouter } from 'vue-router';
import { onMounted, ref, computed } from 'vue';
import { usehandledataManager } from '@/composables/handledataManager.js';

const dataManager = usehandledataManager(); 

// For routing ---
const router = useRouter();
const route = useRoute();

// Input Overlay ---
const projectname = ref('');

// Input Overlay ---
const projects = ref([]);
const overlayRef = ref(null);
const formData = ref({});
const uploadPath = ref(null);

async function fetchData() {
    try {
        const result = await dataManager.getData('/api/getUserProjects');
        if (result) {
            projects.value = result.data;
            console.log('Datei wurde ausgewählt:', projects);
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

const addNewProject = () => {
    if (overlayRef.value) {
        overlayRef.value.classList.remove('d-none');
        // Oder um es zu verstecken: 
    } else {
        console.error('Overlay-Element nicht gefunden.');
    }
};

function submitNewProject() {
    const newprojectdata = new FormData();
    newprojectdata.append('projectname', projectname);

    dataManager.postData('/api/createNewUserProject', newprojectdata)
        .then((responseData) => {
            //console.log('Antwort vom Server:', responseData);
            if (responseData && responseData.uploaded_path) {
                uploadPath.value = responseData.uploaded_path;
            } else {
                console.error('Ungültige Serverantwort');
            }
        })
        .catch((error) => {
            console.error('Fehler beim Hochladen der Datei:', error);
        });

    overlayRef.value.classList.add('d-none');
}

function deleteProject(projectID) {
    console.log('Z72', projectID);
    // dataManager.deleteData(fileData)
    //     .then((responseData) => {
    //         //console.log('Antwort vom Server:', responseData);
    //         if (responseData && responseData.uploaded_path) {
    //             uploadPath.value = responseData.uploaded_path;
    //         } else {
    //             console.error('Ungültige Serverantwort');
    //         }
    //     })
    //     .catch((error) => {
    //         console.error('Fehler beim Hochladen der Datei:', error);
    //     });
}

function selectProject(project) {
    const projectname = project.name;
    const routeData = router.resolve({ name: 'Board', params: { projectname } });
    window.open(routeData.href, '_blank');
}

// const onChangeLetters = (evt) => {
//     console.log('Z92', evt.target.files);
//     formData.value.file = evt.target.files[0];
//     //console.log(formData.value.file.name);

//     // @change="onChangeLetters"
       // NICHT DEN RICHTIGEN WERT ERHALTEN AUS DEM INPUT
// };

</script>

<template>
    <div class="overlay center d-none" id="overlay" ref="overlayRef">
        <div class="overlay-content center">
            <!-- <img src=""> -->
            <p>Neues Projekt</p>
            <input name="mynewprojectname" id="mynewprojectname" type="text" ref="mynewprojectname" placeholder="Projekt Name">

            <button @click.prevent="submitNewProject" class="primary-button">Hinzufügen</button>
        </div>
    </div>

    <div class="page">
        <customheader></customheader>
        <div class="wrapper center">
            <div class="projects">

                <div class="create-card center">
                    <p>Create a new Project</p>

                    <div>
                        <button class="primary-button" @click="addNewProject">CREATE</button>
                        <button class="primary-button">SHARE</button>
                    </div>
                </div>

                <div v-for="project in projects" class="project-card center">
                    <div class="card-header">
                        <h3>{{ project.name }}</h3>
                    </div>

                    <div class="card-actions">
                        <button class="primary-button" @click="deleteProject(project.id)">Delete</button>
                        <button class="primary-button" @click="selectProject(project)">Select</button>
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