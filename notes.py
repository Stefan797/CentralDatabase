# test@t.de   
# test

# // " ", leerzeichen  "\n" neue Zeile
# // async function fetchDataSingleTxtFileAsString() {
# //     debugger;
# //     try {
# //         let resultSingleTxtFile;

# //         // Überprüfe, ob die Datei bereits abgerufen wurde
# //         if (!fileContent.value.length) {
# //             resultSingleTxtFile = await getData(apiUrlSingleTxtFile);

# //             if (resultSingleTxtFile) {
# //                 fileContent.value = String(resultSingleTxtFile.data).split('\n');
# //                 console.log(typeof resultSingleTxtFile.data);
# //                 console.log(resultSingleTxtFile.data);
# //             } else {
# //                 console.error('Fehler beim Abrufen der Daten');
# //             }
# //         }
# //     } catch (error) {
# //         console.error('Fehler beim Abrufen der Daten:', error);
# //     }
# // }



# <div class="file-content-container" v-if="fileObject">
#                     <div v-if="fileContentType === 'text'">
#                         <pre>
#                             <button v-for="(line, index) in fileContent" :key="index" @click="copyLine(index)">
#                                 {{ index + 1 }}
#                             </button>
#                         </pre>
#                     </div>
#                     <div v-else-if="fileContentType == 'image'">
#                         <img :src="fileObject.fileurl">
#                     </div>
#                     <div v-else-if="fileContentType == 'video'">
#                         <video :src="fileObject.fileurl" controls></video>
#                     </div>
#                     <div v-else>Nichts!</div>
#                 </div>


# document.addEventListener("DOMContentLoaded", function() {
#     const codeBlock = document.getElementById('code-block');
#     const lines = codeBlock.innerHTML.split('\n');
#     let numberedLines = '';
#     for (let i = 0; i < lines.length; i++) {
#         numberedLines += `<span class="line-num">${i + 1}</span>${lines[i]}\n`;
#     }
 
#     codeBlock.innerHTML = numberedLines;
# });


# padding-top: 20px
#     height: calc(100vh - 8vh)
#     position: relative

# .cards 
#     width: 38vw
#     height: 30vh
#     padding: 0 4vw 0 4vw
#     margin: 20px 2vw 0 2vw
#     border-radius: 8px

#  <!-- <keyboard></keyboard> -->
#  <!-- <div class="first-part">
#                 <add></add>
                
#             </div>

#             <div class="second-part">
                
#             </div> -->

# /* filter: drop-shadow(5px 5px 15px rgba(0, 0, 0, 0.15)); */
#     /* font-family: 'Poppins', sans-serif; */
# /* background: radial-gradient(74.22% 74.22% at 19.79% 22.42%,
#             #5988ff 6.25%,
#             #5988ff 51.56%,
#             #0043f0 100%); */

#  // console.log(newprojectdata);
#     // console.log(newprojectdata.projectname);
#     // console.log(newprojectdata.get("projectname"));
#     // debugger;

# // const onChangeLetters = (evt) => {
# //     console.log('Z92', evt.target.files);
# //     formData.value.file = evt.target.files[0];
# //     //console.log(formData.value.file.name);

# //     // @change="onChangeLetters"
# // NICHT DEN RICHTIGEN WERT ERHALTEN AUS DEM INPUT
# // };


# // const apiUrl = path;  Z3 handledataManager
# const apiUrl = path;
# uppy.io

# const smartphonemenu = ref(false);
# const ideasList = ref(null);
# const ideas = ref([]);
# const isDragged = ref(false);

# function contentMoveLeft() {
#     console.log('Move content left');

# }

# function contentMoveRight() {
#     console.log('Move content right');

# }

# function dropEvent(event, category) {
#     console.log('Drop event:', event, 'Category:', category);

# }

# function openTask(item) {
#     console.log('Open task:', item);

# }

# function dragStart(event) {
#     console.log('Drag start:', event);

# }

# function dragEnd() {
#     console.log('Drag end');

# }

# function checkTaskColor(color) {
#     return { backgroundColor: color };
# }

# function openDialog() {
#     console.log('Open dialog');

# }

#  //test.append('projectname', formData.value.file);
# <!DOCTYPE html>
# <html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
#     <head>
#         <meta charset="utf-8">
#         <meta name="viewport" content="width=device-width, initial-scale=1">

#         <title>Laravel</title>

#         <!-- Fonts -->
#         <link rel="preconnect" href="https://fonts.bunny.net">
#         <link href="https://fonts.bunny.net/css?family=figtree:400,600&display=swap" rel="stylesheet" />

#         <!-- Styles -->
#         <link rel="stylesheet" href="test.css">
#         <style>
#             .main {
#                 height: 100vh;
#                 width: 100vw;
#             }
#         </style>

#         @vite('resources/js/app.js')
#         @vite('resources/css/app.css')
#     </head>
#     <body>
#         <div id="app" class="main">
#             <customheader></customheader>
#             <directory></directory>
#         </div>
#     </body>
# </html>

# laravel and vue-router combine

# // Route::get('/home', function () {
# //     return view('main');
# // });


# // Route::get('/directory', function () {
# //     return view('directory');
# // });

# const counter = window.counter

# {{counter}}

# window.counter = 10;

#https://router.vuejs.org/guide/

#  Linux Befehl per meiner App zu linux.txt
#  zip -r modaltest.zip . -x data/\* -x freshlaravel/vendor/\* -x freshlaravel/node_modules/\* = Erstellt einen Zip Ordner aus dem aktuellen Ordner. 


# https://sweetalert2.github.io/
# https://www.npmjs.com/package/vue-sweetalert2
# https://pinia.vuejs.org/core-concepts/


# backToHome() {
#       this.$router.push('/v');
#     },

#     goToDirectory() {
#         this.$router.push('/v/directory');
#     },

#     goToModules() {
#         this.$router.push('/v/modules');
#     }


# <!-- <p v-if="!password">Es muss ein Passwort eingegeben werden.</p>
# <p v-else-if="password.length < 8">Es sollten mindestens 8 Buchstaben sein.</p> -->
# <!-- <p v-if="!email">Es muss eine E-Mail-Adresse eingegeben werden.</p>
# <p v-else-if="!isValidEmail">Die E-Mail-Adresse muss ein @ Zeichen enthalten.</p> -->


# <div v-if="currentLoading" class="upload-animation-gif-position">
#     <img src="/assets/img/upload_animation.gif" alt="Upload Animation">
# </div>

# <div class="guest-account-container addbottom">
#     <button @click="loginAsGuest" class="guest-account-button primary-button">Mit Gast Account einloggen
#     !</button>
# </div>

# <div class="movieflix-title-container">
#     <img src="/assets/img/movieflix.PNG" alt="Movieflix Logo">
# </div>


# import { ref, reactive } from 'vue';

# const currentLoading = ref(false);
# // const eyeImage = ref('images/eye.png');
# const registerForm = reactive({
#     username: '',
#     firstname: '',
#     lastname: '',
#     email: '',
#     password: ''
# });

# function loginAsGuest() {
#     // Logik für die Anmeldung als Gast
# }

# function registerNewUser() {
#     // Logik für die Registrierung eines neuen Benutzers
# }

# function showPassword() {
#     // Logik, um das Passwort anzuzeigen
# }

# function togglePasswordVisibility() {
#     // Logik, um die Sichtbarkeit des Passworts zu ändern
# }

# function isFormValid() {
#     // Überprüfung der Formularvalidierung
# }

# function isInvalid(fieldName) {
#     // Überprüfung auf Ungültigkeit eines bestimmten Feldes
# }

# function getErrorMessage(fieldName) {
#     // Abrufen der Fehlermeldung für ein bestimmtes Feld
# }


#<p v-if="isInvalid('firstname')" class="error">{{ getErrorMessage('firstname') }}</p>

# <!-- Similar structure for 'To do', 'Review', and 'Done' sections -->
#             <!-- Replace the placeholder 'ideas', 'todo', 'review', 'done' with actual data properties -->


# Stefan
# Hübner
# stefan.huebner97@web.de
# html
# Erding
# Germany
# Männlich


# 1. Username: testuser1
#    First Name: John
#    Last Name: Doe
#    Email: john.doe@example.com
#    Password: Test@123

# 2. Username: testuser2
#    First Name: Emily
#    Last Name: Smith
#    Email: emily.smith@example.com
#    Password: Pssw0rd!

# 3. Username: testuser3
#    First Name: Michael
#    Last Name: Johnson
#    Email: michael.johnson@example.com
#    Password: SecurePwd123

# 4. Username: testuser4
#    First Name: Sarah
#    Last Name: Brown
#    Email: sarah.brown@example.com
#    Password: Pass123word

# 5. Username: testuser5
#    First Name: David
#    Last Name: Wilson
#    Email: david.wilson@example.com
#    Password: StrongPwd!456

# 6. Username: testuser6
#    First Name: Jessica
#    Last Name: Miller
#    Email: jessica.miller@example.com
#    Password: Paw0rd789

# 7. Username: testuser7
#    First Name: Kevin
#    Last Name: Anderson
#    Email: kevin.anderson@example.com
#    Password: Password123!

# 8. Username: testuser8
#    First Name: Olivia
#    Last Name: Martinez
#    Email: olivia.martinez@example.com
#    Password: MyPssw0rd

# 9. Username: testuser9
#    First Name: Daniel
#    Last Name: Garcia
#    Email: daniel.garcia@example.com
#    Password: DnielPwd789


# 10. Username: testuser10
#     First Name: Sophia
#     Last Name: Lee
#     Email: sophia.lee@example.com
#     Password: LeeSoph!a42

# 11. Test1
#     test
#     nutzer
#     test@t.de
#     test


#background-color: rgba(0, 0, 0, 0.2)
#background-color: #fff



# <script setup>
# // import Uppy from '@uppy/core';
# // import Dashboard from '@uppy/dashboard';
# // import XHR from '@uppy/xhr-upload';

# // import '@uppy/core/dist/style.min.css';
# // import '@uppy/dashboard/dist/style.min.css';

# // new Uppy()
# //     .use(Dashboard, { inline: true, target: 'body' })
# //     .use(XHR, { endpoint: 'https://your-domain.com/upload' });
# </script>

# <template>
#     <div class="upload-container">
#     <form enctype="multipart/form-data" method="POST" action="/uploadS" class="form-container display-flex column">
#         <input type="file" name="file">
#         <button class="cursor" type="submit">Hinzufügen</button>
#     </form>
#     <!-- <h2>Inline Dashboard</h2>
#         <label>
#             <input type="checkbox" :checked="showInlineDashboard" @change="
#                 (event) => {
#                     showInlineDashboard = event.target.checked
#                 }
#             " />
#             Show Dashboard
#         </label>
#         <Dashboard v-if="showInlineDashboard" :uppy="uppy" :props="{
#             metaFields: [{ id: 'name', name: 'Name', placeholder: 'File name' }],
#         }" />
#         <h2>Modal Dashboard</h2>
#         <div>
#             <button @click="open = true">Show Dashboard</button>
#             <DashboardModal :uppy="uppy2" :open="open" :props="{
#                 onRequestCloseModal: handleClose,
#             }" />
#         </div>

#         <h2>Drag Drop Area</h2>
#             <DragDrop :uppy="uppy" :props="{
#                 locale: {
#                     strings: {
#                         chooseFile: 'Boop a file',
#                         orDragDrop: 'or yoink it here',
#                     },
#                 },
#             }" />

#             <h2>Progress Bar</h2>
#             <ProgressBar :uppy="uppy" :props="{
#                 hideAfterFinish: false,
#             }" /> -->
#     </div>
# </template>


# <script>
# </script>

# <!-- <style src="@uppy/core/dist/style.css"></style>
# <style src="@uppy/dashboard/dist/style.css"></style>
# <style src="@uppy/drag-drop/dist/style.css"></style>
# <style src="@uppy/progress-bar/dist/style.css"></style> -->
  
# <style>
# .upload-container {
#     width: 38vw;
#     height: 30vh;
#     padding: 0 4vw 0 4vw;
#     margin: 20px 2vw 0 2vw;
#     background-color: lightblue;
#     border-radius: 8px;
# }

# .draganddrop {
#     height: 50px;
#     width: 40px;
# }
# </style>


# // import Search from '../components/Search.vue'
# // import Add from '../components/Add.vue'
# // import Upload from '../components/Upload.vue'


# function upload() {

#     }

#     function uploadPost(Request $request) {
#         $file = $request->file('file');
#         echo 'File Name: ' . $file->getClientOriginalName();
#         echo '<br>';
#         echo 'File Extension: ' . $file->getClientOriginalExtension();
#         echo '<br>';
#         echo 'File Real Path: ' . $file->getRealPath();
#         echo '<br>';
#         echo 'File Size: ' . $file->getSize();
#         echo '<br>';
#         echo 'File Mime Type: ' . $file->getMimeType();
#         $destinationPath = 'uploads';
#         if ($file->move($destinationPath, $file->getClientOriginalName())) {
#             echo 'success';
#         }
#         else
#             echo 'failed';
#     }


#  public function upload(Request $request) {
#         // dd($request->all());

#         // $request->validate([
#         //     'file'=> ['required','max:200'],
#         //     'title'=> ['required']
#         // ]);

#         if($request->hasFile('file')){
#             // Get filename with the extension
#             $filenameWithExt = $request->file('file')->getClientOriginalName();
#             //Get just filename
#             $filename = pathinfo($filenameWithExt, PATHINFO_FILENAME);
#             // Get just ext
#             $extension = $request->file('file')->getClientOriginalExtension();
#             // Filename to store
#             $fileNameToStore = $filename.'_'.time().'.'.$extension;
#             // Upload Image
#             $path = $request->file('file')->storeAs('public/files',$fileNameToStore);
#         }

#         return response()->json([
#             'success' => true,
#             'uploaded_path' => $path,
#             'public_path' => public_path($path)
#         ]);
#     }


#recognition.interimResults = true; 



#  window.addEventListener("keyup", (keyboard) => {

#             if (this.startrec) {
#                 if (keyRegister['e'] && keyRegister['l']) {
#                     startSpeechToTxt();
#                 }
#             }

#             // if (currentLanguage == 'English') {
#             //     if (keyRegister['d'] && keyRegister['l']) {

#             //     }
#             // }

#             keyRegister[keyboard.key] = false;
#         });



    # //  getcontest File fetch text = response.string

    # //http://localhost:4455/storage/files/laravel.txt = pfad auf Files direct
    # //http://localhost:4455/api/getAllFiles = auf controller direct zugreifen



# export default {
#     data() {
#         return {
#             alphabet: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split(''),
#             apiUrl: '/api/getAllFiles',
#             fileObjects: [],
#             // selectedFile: null,
#             // selectedFileContents: null
#         }
#     },
#     methods: {
#         getdata() {
#             fetch(this.apiUrl, {
#             })
#                 .then((response) => {
#                     console.log(response);
#                     if (response.ok) {
#                         return response.json();
#                     }
#                     throw new Error('Something went wrong');
#                 })
#                 .then((responseJson) => {
#                     console.log(responseJson);
#                     // Do something with the response
#                     this.fileObjects = responseJson.data;
#                 })
#                 .catch((error) => {
#                     console.log(error)
#                 });

#             //console.log(this.fileObject);
#         },

#         // sortdata() {
#         //     const groupIt = (array) => {
#         //         let resultObj = {};

#         //         for (let i = 0; i < array.length; i++) {
#         //             let currentWord = array[i];
#         //             let firstChar = currentWord[0].toLowerCase();
#         //             let innerArr = [];
#         //             if (resultObj[firstChar] === undefined) {
#         //                 innerArr.push(currentWord);
#         //                 resultObj[firstChar] = innerArr
#         //             } else {
#         //                 resultObj[firstChar].push(currentWord)
#         //             }
#         //         }
#         //         return resultObj
#         //     }
#         // }

#         // selectFile(fileObject) {
#         //     console.log('file has been selected', fileObject);
#         //     // logik hier um file auszulesen und anzuzeigen?
#         //     this.selectedFile = fileObject;
#         //     //this.loadFile(fileObject.fileurl)
#         // }
#     },

#     created() {
#         this.getdata(); // Call getdata() method when the component is created
#     }
# };


# <!-- <div>
# <ul v-for="(client, index) in clients.sort((a, b) => (a.name > b.name) ? 1 : -1)" :key="index">
# <li v-for="(fileName, index) in sortedFileNames" :key="index">
# {{ fileName }}
# </li>
# </ul>
# </div> -->

# height: calc(100vh - 8vh)


# const getFileObjectsByLetter = computed(() => {
#   const filteredFileObjects = {};
#   alphabet.forEach(letter => {
#     filteredFileObjects[letter] = fileObjects.value.filter(fileObject =>
#       fileObject.filename.toUpperCase().startsWith(letter)
#     );
#   });
#   return filteredFileObjects;
# });

# <div v-if="getFileObjectsByLetter(letter).length > 0" v-for="fileObject in getFileObjectsByLetter(letter)" :key="fileObject.id">
#     <p @click="selectFile(fileObject)">{{ fileObject.filename }}</p>
#     <a :href="fileObject.fileurl">Link</a>
# </div>

# <!--IF File with first letter exist then show here! -->
# <!--letter should compare with fileObject.filename -->

        # table 
        #     tbody 
        #         tr 
        #             td 

# export default {
#     name: 'speech_to_text',
#     data() {
#         return {
#             runtimeTranscription_: "",
#             transcription_: [],
#             lang_: "de-DE",
#             keyRegister: {},
#             startrec: false
#         };
#     },

#     mounted() {
#         window.addEventListener("keydown", (keyboard) => {
#             this.keyRegister[keyboard.key] = true;
#         });

#         window.addEventListener("keyup", (keyboard) => {

#             if (this.startrec) {
#                 if (this.keyRegister['e'] && this.keyRegister['l']) {
#                     this.startSpeechToTxt();
#                 }
#             }

#             this.keyRegister[keyboard.key] = false;
#         });
#     },

#     methods: {
#         startSpeechToTxt() {

#             window.SpeechRecognition =
#                 window.SpeechRecognition ||
#                 window.webkitSpeechRecognition;

#             const recognition = new window.SpeechRecognition();
#             console.log(recognition);

#             recognition.lang = this.lang_;
#             recognition.interimResults = true;

#             recognition.addEventListener("result", event => {
#                 let text = Array.from(event.results)
#                     .map(result => result[0])
#                     .map(result => result.transcript)
#                     .join("");
#                 this.runtimeTranscription_ = text;
#             });

#             recognition.addEventListener("end", () => {
#                 this.transcription_.push(this.runtimeTranscription_);
#                 this.runtimeTranscription_ = "";
#                 recognition.stop();
#             });
#             recognition.start();
#         },

#     }
# }


#  <!-- <div>
#                 <label for="title">Titel</label>
#                 <input v-model="formData.title" type="text" name="title" id="title">
#             </div> -->




# const sendForm = () => {
#     const data = new FormData();
#     data.append("file", formData.value.file);
#     console.log(data);
#     console.log(formData);

#     dataManager.postData(data)
#         .then((responseData) => {
#             // Handhaben Sie die Antwort der POST-Anfrage
#             console.log('Daten erfolgreich gepostet:', responseData);
#             uploadPath.value = responseData.uploaded_path;
#         })
#         .catch((error) => {
#             // Handhaben Sie einen Fehler bei der POST-Anfrage
#             console.error('Fehler beim Posten der Daten:', error);
#         });
    
    
#         // if (!formData.value.title) {
#     //     console.error('no title set');
#     //     return;
#     // }

#     // if (!formData.value.file) {
#     //     console.error('no file set');
#     //     return;
#     // }

#     // console.log('Alles gut!')

#     // const data = new FormData();
#     // data.append("file", formData.value.file);
#     // // data.append("title", formData.value.title);

#     // fetch(apiUrl, {
#     //     method: 'post',
#     //     body: data,
#     // })
#     //     .then((response) => {
#     //         if (response.ok) {
#     //             return response.json();
#     //         }
#     //         throw new Error('Etwas ist schiefgelaufen');
#     //     })
#     //     .then((responseJson) => {
#     //         // Etwas mit der Antwort machen
#     //         uploadPath.value = responseJson.uploaded_path;
#     //     })
#     //     .catch((error) => {
#     //         console.log(error)
#     //     });
# };
# </script>


# // export default {
# //     data() {
# //         return {
# //             'user': {
# //                 'username': '',
# //                 'first_name': '',
# //                 'last_name': '',
# //                 'email': '',
# //                 'password': ''
# //             }
# //         };
# //     },

# //     methods: {
# //         saveData() {
# //             axios.post('/user/create', this.user).then(
# //                 response => {
# //                     console.log(response);
# //                     //login();
# //                 }
# //             ).catch(error => {
# //                 console.log('error');
# //             })
# //         },

# //         // login() {
# //         //     router.push('/v');
# //         // },

# //         showPassword() {
# //             const passwordInput = this.$refs.passwordInput;
# //             if (passwordInput.type === 'password') {
# //                 passwordInput.type = 'text';
# //             } else {
# //                 passwordInput.type = 'password';
# //             }
# //         }
# //     }
# // }


# // export default {
# //     data() {
# //         return {
# //             'user': {
# //                 'email': '',
# //                 'password': ''
# //             },
# //             checkboxVisible: false,
# //             token: null,
# //             user_id: null,
# //             doNotMemorizeUserData: false
# //         };
# //     },
# //     methods: {
# //         login() {
# //             const vm = this;
# //             axios.post('/user/login', this.user).then(
# //                 response => {
# //                     console.log('loginresponse', response);
# //                     vm.token = response.data.token
# //                     vm.user_id = response.data.user_id
# //                     vm.setInformations();
# //                     vm.$router.push('/v');
# //                 },
# //             ).catch(error => {
# //                 console.log('error');
# //             })
# //         },

# //         setInformations() {
# //             if (!this.doNotMemorizeUserData) {
# //                 localStorage.removeItem('token');
# //                 localStorage.removeItem('CurrentUserID');
# //                 sessionStorage.setItem('token', this.token);
# //                 sessionStorage.setItem('CurrentUserID', this.user_id);
# //             } else {
# //                 localStorage.setItem('token', this.token);
# //                 localStorage.setItem('CurrentUserID', this.user_id);
# //             }
# //         },

# //         showPassword() {
# //             const passwordInput = this.$refs.passwordInput;
# //             if (passwordInput.type === 'password') {
# //                 passwordInput.type = 'text';
# //             } else {
# //                 passwordInput.type = 'password';
# //             }
# //         },

# //         rememberMe() {
# //             this.checkboxVisible = !this.checkboxVisible;
# //             if (this.checkboxVisible) {
# //                 this.doNotMemorizeUserData = true;
# //             } else {
# //                 this.doNotMemorizeUserData = false;
# //             }

# //             console.log(this.doNotMemorizeUserData);
# //         }
# //     },
# // };


# // export default {
# //     data() {
# //         return {
# //             //logoutresponse: null,
# //         };
# //     },
# //     methods: {
# //         logout() {
# //             const vm = this;
# //             axios.get('/user/logout', this.user).then(
# //                 response => {
# //                     console.log('logoutresponse', response);
# //                     //vm.logoutresponse = response.logout
# //                     vm.clearInformations();
# //                     vm.$router.push('/v/login');
# //                 },
# //             ).catch(error => {
# //                 console.log('error');
# //             })
# //         },

# //         clearInformations() {
# //             localStorage.removeItem('token');
# //             localStorage.removeItem('CurrentUserID');
# //             sessionStorage.removeItem('token', this.token);
# //             sessionStorage.removeItem('CurrentUserID', this.user_id);
# //         }
# //     },
# // };


# // Benutzerdaten, die wahrscheinlich aus einem anderen Ort kommen
# // let token = localStorage.getItem('token');
# // let user_id = localStorage.getItem('CurrentUserID')


# // export default {
# //     data() {
# //         return {
# //             apiUrl: '/api/upload',
# //             formData: {},
# //             uploadPath: null
# //         }
# //     },

# //     methods: {
# //         onUploadFiles(evt) {
# //             console.log(this.$refs.myfile.files)
# //             this.formData.file = this.$refs.myfile.files[0];

# //             console.log(this.formData.file.name);
# //         },

# //         sendForm() {
# //             // if (!this.formData.title) {
# //             //     console.error('no title set');
# //             //     return;
# //             // }

# //             if (!this.formData.file) {
# //                 console.error('no file set');
# //                 return;
# //             }

# //             console.log('good to go!')

# //             const formData = new FormData();
# //             formData.append("file", this.formData.file);
# //             formData.append("title", this.formData.title);

# //             fetch(this.apiUrl, {
# //                 method: 'post',
# //                 body: formData,
# //             })
# //                 .then((response) => {
# //                     if (response.ok) {
# //                         return response.json();
# //                     }
# //                     throw new Error('Something went wrong');
# //                 })
# //                 .then((responseJson) => {
# //                     // Do something with the response
# //                     this.uploadPath = responseJson.uploaded_path;
# //                 })
# //                 .catch((error) => {
# //                     console.log(error)
# //                 });
# //         }
# //     }
# // }


# const getFileContent = (fileObject) => {
#     // debugger;
#     if (fileObject.value) {
#         const fileType = getFileType(fileObject.value.filename);
#         if (fileType === 'image') {
#             return `<img src="${fileObject.value.fileurl}" alt="${fileObject.value.filename}">`;
#         } else if (fileType === 'video') {
#             return `<video src="${fileObject.value.fileurl}" controls></video>`;
#         } else if (fileType === 'text') {
#             // Hier können Sie eine Logik hinzufügen, um den Textinhalt der Datei anzuzeigen
#             return `<embed src="${fileObject.value.fileurl}">`;
#         }
#     }
#     return 'Datei nicht gefunden oder ungültiger Dateityp';
# };


# <!-- <h1>{{ $route.params.id }}</h1> -->

#                 <!-- <div class="file-content-container" v-if="fileObject">
#                     <div v-html="getFileContent(fileObject)"></div>
#                 </div>
#                 <div v-else>
#                     Datei nicht gefunden oder ungültiger Dateityp
#                 </div> -->

#  <div v-else>
#                     Datei nicht gefunden oder ungültiger Dateityp
#                 </div>

# <!-- <h1>{{ $route.params.filename }}</h1> -->


# const startSpeechToTxt = () => {
#     window.SpeechRecognition =
#         window.SpeechRecognition ||
#         window.webkitSpeechRecognition;

#     const recognition = new window.SpeechRecognition();
#     console.log(recognition);

#     recognition.lang = lang_.value;
#     recognition.interimResults = true;

#     recognition.addEventListener("result", event => {
#         let text = Array.from(event.results)
#             .map(result => result[0])
#             .map(result => result.transcript)
#             .join("");
#         runtimeTranscription_.value = text;
#     });

#     recognition.addEventListener("end", () => {
#         transcription_.value.push(runtimeTranscription_.value);
#         runtimeTranscription_.value = "";
#         recognition.stop();
#     });
#     recognition.start();
# };


# // protected function fileurl(): Attribute
#     // {
#     //     return Attribute::make(
#     //         get: fn (string $value, array $attributes) {
#     //             echo "test";
#     //             return $attributes['filename'] + "test";
#     //         },
#     //     );
#     // }


# // Route::middleware('auth:sanctum')->get('/posts/{post}', function (\App\Models\Post $post) {
# //     \Illuminate\Support\Facades\Gate::authorize('view-post', $post);
        

# //     return $post;
# // });


# // if (router.currentRoute.value.query.file) {
# //   console.log('URL-Parameter:', router.currentRoute.value.query.file);
# //   try {
# //     fileObject = JSON.parse(decodeURIComponent(router.currentRoute.value.query.file));
# //     console.log('File Object:', fileObject);
# //   } catch (error) {
# //     console.error('Fehler beim Parsen der JSON-Zeichenfolge:', error);
# //   }
# // }


# <!-- <p @click="selectFile(fileObject)"><a :href="fileObject.fileurl">{{ fileObject.filename }}</a></p> -->



# // function selectFile(fileObject) {
# //   const { filename } = fileObject;
# //   router.push({ name: 'File', params: { filename } });
# // }


# <div class="board-container section2" id="scrolling_div">
#             <div class="example-container">
#                 <h2>Ideas</h2>
#                 <div v-if="ideasList" ref="ideasList" class="example-list" @drop="dropEvent($event, 'ideas')">
#                     <div v-for="item in ideas" :key="item.id" @click="openTask(item)" :class="{ 'example-box': isDragged }"
#                         draggable="true" @dragstart="dragStart($event)" @dragend="dragEnd">
#                         <div :style="checkTaskColor(item.color)">{{ item.text }}</div>
#                     </div>
#                 </div>
#             </div>

#             <button @click="openDialog" class="btn-position btn-color" mat-fab matTooltip="Add New Ticket">
#                 add
#             </button>
#         </div>


# <div class="board">
#         <div v-if="smartphonemenu" class="scroll-container">
#             <img @click="contentMoveLeft" src="assets/img/arrow-left.png" />
#             <img @click="contentMoveRight" src="assets/img/arrow-right.png" />
#         </div>

        
#     </div>


# <!-- 
#                 <div class="column" id="todo">Todo</div>
#                 <div class="column" id="in-progress">In Progress</div>
#                 <div class="column" id="done">Done</div> -->