export function usehandledataManager() {
    async function fetchData() {
        const result = await getData(apiUrl);
        if (result) {
            fileObjects.value = result.data;
            //console.log('Datei wurde ausgewählt:', fileObjects);
            sortdata();
            // filesStore.saveFileObjects(data);
        } else {
            console.error('Fehler beim Abrufen der Daten');
        }
    }

    async function sortdata() {
        const newfilesDict = {};
        //console.log('Z30:', fileObjects.value);
        alphabet.forEach((letter) => {
            // debugger;
            const filteredFiles = fileObjects.value.filter((fileObject) => {
                //console.log('Z34:', fileObject);
                const fileName = fileObject.filename.toUpperCase();
                return fileName.startsWith(letter);
            });

            // console.log('Sortierte Dateiobjekte nach Buchstaben:', filteredFiles);

            const sortedFiles = filteredFiles.sort((a, b) => {
                const fileNameA = a.filename.toUpperCase();
                const fileNameB = b.filename.toUpperCase();
                return fileNameA.localeCompare(fileNameB);
            });

            newfilesDict[letter] = sortedFiles;
        });

        filesDict.value = newfilesDict;
    }

    onMounted(() => {
        fetchData();
    });

    async function submitNewTxtToSelectedFile(event) {
        event.preventDefault();

        const selectedFileName = event.target.elements['category'].value;
        const message = event.target.elements['message'].value;

        if (!selectedFileName || !message) {
            console.error('Bitte wähle eine Datei aus und gib eine Nachricht ein.');
            return;
        }

        const fileObject = fileObjects.value.find(file => file.filename === selectedFileName);

        if (!fileObject) {
            console.error('Ausgewählte Datei nicht gefunden.');
            return;
        }

        const data = new FormData();
        data.append("filename", selectedFileName);
        data.append("message", message);

        dataManager
            .postData("/api/addFurtherTxt", data)
            .then((responseData) => {
                console.log('Antwort vom Server:', responseData);
                if (responseData) {
                    document.getElementById('message').value = '';
                    // newprojectbox.value = responseData.name;
                } else {
                    console.error("Ungültige Serverantwort");
                }
            })
            .catch((error) => {
                console.error("Fehler beim Hochladen der Datei:", error);
            });
    }
}