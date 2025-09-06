<template>
  <a :disabled="isSaving" @click="saveVideo">
    {{ isSaving ? "Guardando..." : "Guardar" }}
  </a>
</template>

<script setup>
import { ref } from "vue";
import Cookies from "js-cookie";
import { saveRecord } from "../services/videos";

const props = defineProps({
  videoBlob: Blob
});

const isSaving = ref(false);

const saveVideo = async () => {
  if (!props.videoBlob) {
    alert("No hay video para guardar");
    return;
  }
  const usr = Cookies.get("usuario");
  console.log("props.videoBlob", props.videoBlob, props.videoBlob.size);


  isSaving.value = true;

  // Crear un File a partir del Blob
  const videoFile = new File([props.videoBlob], "grabacion.webm", { type: "video/webm" });

  const response = await saveRecord(usr, videoFile);

  if (response) {
    alert("Grabación guardada");
  } else {  
    alert("Error al guardar grabación");
  }

  isSaving.value = false;
};

</script>
