import { defineStore } from 'pinia';

export const useFileStore = defineStore('file', {
    id: 'file',
    state: () => ({
        fileContent: '',
    }),
    actions: {
        setFileContent(content) {
            this.fileContent = content;
        },
    },
});