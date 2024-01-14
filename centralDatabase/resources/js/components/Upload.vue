<script setup>
import { ref } from 'vue';
import { usehandledataManager } from '@/composables/handledataManager.js';

const apiUrl = '/api/upload';
const dataManager = usehandledataManager(apiUrl);

const formData = ref({});
const uploadPath = ref(null);

const onUploadFiles = (evt) => {
    //console.log(evt.target.files);
    formData.value.file = evt.target.files[0];
    //console.log(formData.value.file.name);
};

const sendForm = () => {
    if (!formData.value.file) {
        console.error('Keine Datei ausgewählt');
        return;
    }

    const fileData = new FormData();
    fileData.append('file', formData.value.file);

    dataManager.postData('/api/upload', fileData)
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
};
</script>

<template>
    <div class="upload-container center">
        <div class="form-container">
            <div class="draganddropfield">
                <h2>
                    {{ uploadPath }}
                </h2>
            </div>
            
            <form class="file-upload-form">
                <div class="choose-file-container">
                    <input class="primary-button" ref="myfile" type="file" name="myfile" id="myfile"
                        @change="onUploadFiles">
                </div>

                <div class="submit-btn-container">
                    <button class="primary-button" @click.prevent="sendForm">Upload starten</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>

</script>


<style>
@import '@/sass/components/upload.sass';
</style>