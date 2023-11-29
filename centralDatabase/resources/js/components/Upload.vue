<script setup>
</script>

<template>
    <div class="upload-container">
        <h2>File Uploader</h2>

        <form>
            <div>
                <label for="title">Titel</label>
                <input v-model="formData.title" type="text" name="title" id="title">
            </div>
            <div>
                <label for="myfile">Datei uploaden</label>
                <input ref="myfile" type="file" name="myfile" id="myfile" @change="onUploadFiles">
            </div>

            <div>
                <button @click.prevent="sendForm">Upload starten</button>
            </div>
        </form>

        <div>
            <h2>
                {{ uploadPath }}
            </h2>
        </div>
    </div>
</template>

<script>

export default {
    data() {
        return {
            apiUrl: '/api/upload',
            formData: {},
            uploadPath: null
        }
    },

    methods: {
        onUploadFiles(evt) {
            console.log(this.$refs.myfile.files)
            this.formData.file = this.$refs.myfile.files[0];

            console.log(this.formData.file.name);
        },

        sendForm() {
            if (!this.formData.title) {
                console.error('no title set');
                return;
            }

            if (!this.formData.file) {
                console.error('no file set');
                return;
            }

            console.log('good to go!')

            const formData = new FormData();
            formData.append("file", this.formData.file);
            formData.append("title", this.formData.title);

            fetch(this.apiUrl, {
                method: 'post',
                body: formData,
            })
            .then((response) => {
                if (response.ok) {
                    return response.json();
                }
                throw new Error('Something went wrong');
            })
            .then((responseJson) => {
                // Do something with the response
                this.uploadPath = responseJson.uploaded_path;
            })
            .catch((error) => {
                console.log(error)
            });
        }
    }
}

</script>


<style>
@import '@/sass/components/upload.sass';
</style>