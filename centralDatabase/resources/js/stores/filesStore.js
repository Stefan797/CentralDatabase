import { defineStore } from 'pinia'

export const useFilesStore = defineStore('files', {
    state: () => ({ 
        fileCache: [],
        directories: [],
        storedFileObjects: [],
    }),

    getters: {
        getFileObjects: (state) => state.storedFileObjects,
    },

    actions: {
        sort() {
            console.log('STORE: sort files here');
        },

        saveFileObjects(fileObjects) {
          this.storedFileObjects = fileObjects;
        },
    },
})
