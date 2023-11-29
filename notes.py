# uppy.io


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
