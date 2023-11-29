<script setup>
</script>

<template>
    <div class="page">
        <customheader></customheader>
        <div class="wrapper center">
            <div class="directory">
                <h2>Verzeichnis</h2>
                
                <table>
                    <tbody>
                        <tr v-for="(letter, index) in alphabet" :key="index">
                            <td>{{ letter }}</td>
                        </tr>
                    </tbody>
                </table>
                <!-- <ul v-for="(client, index) in clients.sort((a, b) => (a.name > b.name) ? 1 : -1)" :key="index">

                    <li v-for="(fileName, index) in sortedFileNames" :key="index">
                    {{ fileName }}
                    </li>
                </ul> -->
            </div>
        </div>
    </div>
</template>

<script>
export default {
    // Woher ich die Datei Namen hole?
    // Wie wird es a - z eingebunden?
    // 

    data() {
        return {
            alphabet: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split(''),
            'file': {
                'name': 'test',
                'path': 'public/files'
            },
            path: 'public/files',
            fileNames: [],
        };
    },
    // computed: {
    //     sortedFileNames() {
    //         return this.fileNames.sort();
    //     },
    // },
    // mounted() {
    //     this.fetchFileNames();
    // },
    // methods: {
    //     fetchFileNames() {
    //         this.fileNames = ["file1.txt", "file2.txt", "file3.txt"];
    //     },
    // },
};
</script>
  
<style>
@import '@/sass/pages/directory.sass';
</style>