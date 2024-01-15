<script setup>
import { watchEffect, ref, onMounted } from 'vue'
import { Codemirror } from 'vue-codemirror'
import { javascript } from '@codemirror/lang-javascript'
import { oneDark } from '@codemirror/theme-one-dark'
import { usehandledataManager } from '@/composables/handledataManager.js';
import { useRoute, useRouter } from 'vue-router';
import { useFileStore } from '@/stores/fileStore';

const fileStore = useFileStore();
const dataManager = usehandledataManager();
const route = useRoute();

const filename = route.params.filename;
const code = ref('');
const extensions = [javascript(), oneDark];
const view = ref(null);

const fetchFileContent = async () => {
    try {
        const data = new FormData();
        data.append("filename", filename);
        const response = await dataManager.postData('/api/readFileContent', data);
        // console.log(response);
        const body = await response.json();
        // console.log(body);

        if (body.data) {
            code.value = body.data;
            fileStore.setFileContent(body.data);

            console.log(fileStore.fileContent);
        } else {
            console.error('Fehler beim Abrufen der Daten');
        }
    } catch (error) {
        console.error('Fehler beim Abrufen der Daten:', error);
    }
}

onMounted(fetchFileContent);

const handleReady = (payload) => {
    view.value = payload.view
};

const getCodemirrorStates = () => {
    const state = view.value.state
    const ranges = state.selection.ranges
    const selected = ranges.reduce((r, range) => r + range.to - range.from, 0)
    const cursor = ranges[0].anchor
    const length = state.doc.length
    const lines = state.doc.lines
    // more state info ...
    // return ...
};

const log = console.log;

const handleCodeChange = () => {
    fileStore.setFileContent(code.value);
    // console.log(fileStore.fileContent);
}

watchEffect(() => {
    handleCodeChange();
});
</script>

<template>
    <Codemirror v-model="code" :extensions="extensions" @ready="handleReady" />
</template>

<!-- <template>
    <codemirror v-model="code" placeholder="Code goes here..." :style="{ height: '400px' }" :autofocus="true"
        :indent-with-tab="true" :tab-size="2" :extensions="extensions" @ready="handleReady" @change="log('change', $event)"
        @focus="log('focus', $event)" @blur="log('blur', $event)" />
</template> -->

<!-- <script>
import { defineComponent, ref, shallowRef } from 'vue'
import { Codemirror } from 'vue-codemirror'
import { javascript } from '@codemirror/lang-javascript'
import { oneDark } from '@codemirror/theme-one-dark'

async function fetchDataSingleTxtFileAsString() {
    try {
        const resultSingleTxtFile = await getData(apiUrlSingleTxtFile);
        if (resultSingleTxtFile) {
            // fileContent.value = result.data;
            // console.log('Datei wurde ausgewählt:', fileContent);
            fileContent.value = String(resultSingleTxtFile.data).split('\n');
            console.log(typeof resultSingleTxtFile.data);
            console.log(resultSingleTxtFile.data);
        } else {
            console.error('Fehler beim Abrufen der Daten');
        }
    } catch (error) {
        console.error('Fehler beim Abrufen der Daten:', error);
    }
}

export default defineComponent({
    components: {
        Codemirror
    },
    setup() {
        const code = ref(`console.log('Hello, world!')`)
        const extensions = [javascript(), oneDark]

        // Codemirror EditorView instance ref
        const view = shallowRef()
        const handleReady = (payload) => {
            view.value = payload.view
        }

        // Status is available at all times via Codemirror EditorView
        const getCodemirrorStates = () => {
            const state = view.value.state
            const ranges = state.selection.ranges
            const selected = ranges.reduce((r, range) => r + range.to - range.from, 0)
            const cursor = ranges[0].anchor
            const length = state.doc.length
            const lines = state.doc.lines
            // more state info ...
            // return ...
        }

        return {
            code,
            extensions,
            handleReady,
            log: console.log
        }
    }
})
</script> -->

