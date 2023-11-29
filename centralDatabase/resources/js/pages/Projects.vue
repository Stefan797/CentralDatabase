<script setup>
</script>

<template>
    <div class="projects">
        <router-link to="/v/board"><img class="choose-img cursor" src="/images/directory.png"/></router-link>
        <!-- <div class="projects-card">
            <div class="card-header">
                <h3>New Project</h3>
            </div>

            <div class="card-content">
                <label for="projectName">Name of the project</label>
                <input v-model="projectname" id="projectName" type="text" />
            </div>

            <div class="card-actions">
                <button @click="addNewProject">CREATE</button>
                <button>SHARE</button>
            </div>
        </div>

        <div v-for="project in projects" :key="project.customIdName" class="projects-card">
            <div class="card-header">
                <h3>{{ project.name }}</h3>
            </div>

            <div class="card-content">
            </div>

            <div class="card-actions">
                <button @click="deleteProject(project.customIdName)">Delete</button>
                <button @click="selectProject(project)">Select</button>
            </div>
        </div>  -->
    </div>
</template>
  
<script>
export default {
    data() {
        return {
            projectname: '',
            projects: []
        };
    },
    methods: {
        addNewProject() {
            console.log('test');
        },
        deleteProject(customIdName) {
            console.log('test');
        },
        selectProject(project) {
            console.log('test');
        }
    }
};
</script>
  
<style>
@import '@/sass/pages/projects.sass'; 
</style>