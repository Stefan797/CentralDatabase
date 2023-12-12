export function usehandledataManager(apiUrl) {
    async function getData() {
        try {
            const response = await fetch(apiUrl);
            console.log(response);
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

    async function postData(data) {
        console.log(data);
        try {
            const response = await fetch(apiUrl, {
                method: 'post',
                body: data,
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

    async function putData(dataId, updatedData) {
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

    async function deleteData(dataId) {
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