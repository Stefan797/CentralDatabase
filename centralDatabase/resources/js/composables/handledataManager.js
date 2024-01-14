export function usehandledataManager() {
    async function getData(path) {
        try {
            const response = await fetch(path);
            //console.log(response);
            if (!response.ok) {
                throw new Error('Something went wrong');
            }
            const data = await response.json();
            // console.log(data);
            return data;
        } catch (error) {
            console.error(error);
            return null;
        }
    }

    async function postData(path, data) {
        // debugger;
        console.log(data);
        try {
            const response = await fetch(path, {
                method: 'post',
                body: data,
            });
    
            if (!response.ok) {
                throw new Error('Something went wrong');
            }
    
            //const responseData = await response.json();
            const responseData = await response;
            return responseData;
        } catch (error) {
            console.error(error);
            return null;
        }
    }

    async function putData(path, dataId, updatedData) {
        try {
            const response = await fetch(`${apiUrl}/${dataId}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(updatedData),
            });
            if (!response.ok) {
                throw new Error('Something went wrong');
            }
            const responseData = await response.json();
            return responseData;
        } catch (error) {
            console.error(error);
            return null;
        }
    }

    async function deleteData(path, dataId) {
        try {
            const response = await fetch(`${apiUrl}/${dataId}`, {
                method: 'DELETE',
            });
            if (!response.ok) {
                throw new Error('Something went wrong');
            }
            const responseData = await response.json();
            return responseData;
        } catch (error) {
            console.error(error);
            return null;
        }
    }

    return {
        getData,
        postData,
        putData,
        deleteData,
    };
}