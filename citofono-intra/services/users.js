import axios from "axios";

const host = import.meta.env.VITE_APP_API_HOST_ROLMATRIX;
const userId = import.meta.env.VITE_APP_USER_ID;

export async function obtenerComunasService(){
    try {
        return await axios.get(`${host}/${userId}/engine/consulta/todasComunas`);
    } catch (error) {
        console.error("Error al cargar las comunas, error:", error);
        return error;
    }
}