<script setup>
</script>


<template>
    <div class="voice">
        <div class="center">
            <button class="speech-to-txt" @click="startSpeechToTxt">Speech to txt</button>
        </div>

        <div class="textresult">
            <p>{{ transcription_ }}</p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'speech_to_text',
    data() {
        return {
            runtimeTranscription_: "",
            transcription_: [],
            lang_: "de-DE",
            keyRegister: {},
            startrec: false
        };
    },

    mounted() {
        window.addEventListener("keydown", (keyboard) => {
            this.keyRegister[keyboard.key] = true;
        });

        window.addEventListener("keyup", (keyboard) => {

            if (this.startrec) {
                if (this.keyRegister['e'] && this.keyRegister['l']) {
                    this.startSpeechToTxt();
                }
            }
            
            this.keyRegister[keyboard.key] = false;
        });
    },

    methods: {
        startSpeechToTxt() {

            window.SpeechRecognition =
                window.SpeechRecognition ||
                window.webkitSpeechRecognition;

            const recognition = new window.SpeechRecognition();
            console.log(recognition);

            recognition.lang = this.lang_;
            recognition.interimResults = true;

            recognition.addEventListener("result", event => {
                let text = Array.from(event.results)
                    .map(result => result[0])
                    .map(result => result.transcript)
                    .join("");
                this.runtimeTranscription_ = text;
            });

            recognition.addEventListener("end", () => {
                this.transcription_.push(this.runtimeTranscription_);
                this.runtimeTranscription_ = "";
                recognition.stop();
            });
            recognition.start();
        },

    }
}
</script>

<style>
@import '@/sass/components/speech.sass';
</style>