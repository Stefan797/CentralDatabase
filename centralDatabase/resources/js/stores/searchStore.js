import { defineStore } from 'pinia';
import { usehandledataManager } from '@/composables/handledataManager.js';

export const useSearchStore = () => {
  const dataManager = usehandledataManager();

  return defineStore('search', {
    id: 'search',
    state: () => ({
      searchResults: [],
      searchActive: false,
      isSearching: false,
      searchQueries: '',
    }),
    actions: {
      getSearchResults(results) {
        this.searchResults = results;
      },
      clearSearchResults() {
        this.searchResults = [];
      },
      setSearch(searchterm) {
        this.searchQueries = searchterm;
        this.search(this.searchQueries);
      },
      setSearchStatus(status) {
        this.searchActive = status;
      },
      async search(searchQueries) {
        const data = new FormData();
        data.append("query", searchQueries);
        try {
          let response = await dataManager.postData('/api/searchFileInput', data);
          const body = await response.json();

          if (body.File[0]) {
            this.searchResults = body.File;
            console.log('current searchResults', this.searchResults);
          } else {
            console.error('Fehler beim Abrufen der Daten');
          }
        } catch (error) {
          console.error('Fehler bei der Suche:', error);
          throw error;
        }
      }
    },
  })();
}
