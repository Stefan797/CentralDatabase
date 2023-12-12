<script setup>
import { ref } from 'vue';

const runtimeTranscription_ = ref("");
const transcription_ = ref([]);
const lang_ = ref("de-DE");
const startrec = ref(false);
let recognition;

const startSpeechToTxt = () => {
    window.SpeechRecognition =
        window.SpeechRecognition ||
        window.webkitSpeechRecognition;

    recognition = new window.SpeechRecognition();
    console.log(recognition);

    recognition.lang = lang_.value;
    recognition.interimResults = true;

    recognition.addEventListener("result", event => {
        let text = Array.from(event.results)
            .map(result => result[0])
            .map(result => result.transcript)
            .join("");
        runtimeTranscription_.value = text;
    });

    recognition.start();
};

const stopSpeechToTxt = () => {
    if (recognition) {
        recognition.stop();
        transcription_.value.push(runtimeTranscription_.value);
        runtimeTranscription_.value = "";
    }
};
</script>


<template>
    <div class="voice center">
        <form class="form-container column">

            <div class="text-container">
                <textarea class="textresult textarea-focus-settings">
                    {{ transcription_ }}
                </textarea>
            </div>

            <div class="button-container">
                <div class="choose-file-container">
                    <select class="primary-button" id="category" name="category" required>
                        <option value="" disabled selected>Wähle hier die Datei aus</option>
                        <option value="Option 1">Option 1</option>
                        <option value="Option 2">Option 2</option>
                        <option value="Option 3">Option 3</option>
                    </select>
                </div>
                <div class="submit-btn-container">
                    <button class="primary-button" type="submit">Hinzufügen</button>
                </div>

                <div class="speech-btn-container">
                    <button class="primary-button" @click="startSpeechToTxt">Aufnahme starten</button>
                </div>

                <div class="speech-btn-container">
                    <button class="primary-button" @click="stopSpeechToTxt">Aufnahme stoppen</button>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
</script>

<style>
@import '@/sass/components/speech.sass';
</style>