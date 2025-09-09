import axios from "axios";

const host = import.meta.env.VITE_APP_API_HOST + "video";

export async function saveRecord(usuarioId, video) {
    try {
        const formData = new FormData();

        formData.append("video", video);      
        formData.append("usuarioId", usuarioId);

        return await axios.post(`${host}/guardarvideo`, formData, {
            headers: {
                "Content-Type": "multipart/form-data"
            }
        });
    } catch (error) {
        return error;
    }
}

export async function getUsersRecords(userid) {
    try {
        return await axios.post(`${host}/obtenervideousuario`,
            {
                userid
            },
            {
                headers: {
                    "Content-Type": "application/json"
                }
            }
        );
    } catch (error) {
        return error;
    }
}

export async function getRecord(videoid) {
    try {
        return await axios.post(`${host}/obtenerVideo`,
            {
                videoid
            },
            {
                responseType: 'blob',
                headers: {
                    "Content-Type": "application/json"
                }
            }
        );
    } catch (error) {
        return error;
    }
}