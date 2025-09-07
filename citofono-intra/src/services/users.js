import axios from "axios";

const host = import.meta.env.VITE_APP_API_HOST + "auth";

export async function login(email, clave) {
    try {
        return await axios.post(`${host}/login`,
            {
                email,
                clave
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

export async function registroUsuario(data) {
    try {
        return await axios.post(`${host}/registrar`,
            {
                nombre: data.nombre,
                apellido_paterno: data.apellido_paterno,
                apellido_materno: data.apellido_materno,
                email: data.email,
                clave: data.clave
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
