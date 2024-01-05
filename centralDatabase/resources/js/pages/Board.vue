<script setup>
import { onMounted, ref, computed } from 'vue';
import { usehandledataManager } from '@/composables/handledataManager.js';

const dataManager = usehandledataManager();

const overlayRef = ref(null);
const tickets = ref([]);

const ticket = ref({
    text: '',
    color: '',
    category: ''
});

async function fetchData() {
    try {
        const result = await dataManager.getData('/api/getUserBoard');
        if (result) {
            tickets.value = result.data;
            console.log('Datei wurde ausgewählt:', tickets);
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

const openCreateNewTicket = (ticketcategory) => {
    ticket.category = ticketcategory;
    if (overlayRef.value) {
        overlayRef.value.classList.remove('d-none');
    } else {
        console.error('Overlay-Element nicht gefunden.');
    }
};

function submitNewTicket() {
    dataManager.postData('/api/createNewUserTicket', ticket)
        .then((responseData) => {
            if (responseData && responseData.uploaded_path) {
                uploadPath.value = responseData.uploaded_path;
            } else {
                console.error('Ungültige Serverantwort');
            }
        })
        .catch((error) => {
            console.error('Fehler beim Hochladen der Datei:', error);
        });

    // overlayRef.value.classList.add('d-none');
}
</script>

<template>
    <div class="overlay center d-none" id="overlay" ref="overlayRef">
        <div class="overlay-content center">
            <form @submit.prevent="submitNewTicket()">
                <p>Neues Ticket</p>
                <input type="text" v-model="ticket.text">
                <input type="text" v-model="ticket.color">

                <button class="primary-button" type="submit">Hinzufügen</button>
            </form>
        </div>
    </div>

    <div class="page">
        <customheader></customheader>
        <div class="wrapper center">
            <div class="kanban-board">
                <div class="column">
                    <div class="column-header">
                        Ideas
                        <img @click="openCreateNewTicket('ideas')" src="/images/addticketgreen.png" />
                    </div>
                    <div class="column-content">

                    </div>
                </div>
                <div class="column">
                    <div class="column-header">
                        Todo
                        <img @click="openCreateNewTicket('todo')" src="/images/addticketgreen.png" />
                    </div>
                    <div class="column-content">

                    </div>
                </div>
                <div class="column">
                    <div class="column-header">
                        In Progress
                        <img @click="openCreateNewTicket('in-progress')" src="/images/addticketgreen.png" />
                    </div>
                    <div class="column-content">

                    </div>
                </div>
                <div class="column">
                    <div class="column-header">
                        Done
                        <img @click="openCreateNewTicket('done')" src="/images/addticketgreen.png" />
                    </div>
                    <div class="column-content">

                    </div>
                </div>
            </div>



        </div>
    </div>
</template>
  
<script>
</script>
  
<style>
@import '@/sass/pages/board.sass';
</style>
  