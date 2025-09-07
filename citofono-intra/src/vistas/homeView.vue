<template>
  <div class="citofonia-container">
    <h2>Grabadora</h2>
    <div class="video-section">
      <video ref="videoElement" autoplay muted playsinline></video>
    </div>

    <div class="options-bar">
      <button @click="toggleRecording" class="record-button">
        {{ isRecording ? 'Detener' : 'Grabar' }}
      </button>

      <select v-model="selectedDeviceId" @change="startCameraStream">
        <option v-for="device in videoDevices" :key="device.deviceId" :value="device.deviceId">
          {{ device.label || `Cámara ${device.deviceId.substring(0, 5)}...` }}
        </option>
      </select>

      <a v-if="videoURL" :href="videoURL" download="grabacion.webm" class="download-button">
        Descargar
      </a>
      <a v-if="videoURL" class="download-button">
        <guardarVideo :videoBlob="videoBlob"/>
      </a>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import guardarVideo from '../components/guardarVideo.vue';

const videoElement = ref(null);
const isRecording = ref(false);
const videoURL = ref(null);
const videoDevices = ref([]);
const selectedDeviceId = ref('');
const status = ref('');

// Variables de grabación
let mediaRecorder = null;
const recordedChunks = [];
const videoBlob = ref(null);

const getCameras = async () => {
  try {
    const devices = await navigator.mediaDevices.enumerateDevices();
    videoDevices.value = devices.filter(device => device.kind === 'videoinput');
    if (videoDevices.value.length > 0) {
      selectedDeviceId.value = videoDevices.value[0].deviceId;
    }
  } catch (err) {
    status.value = "Error: No se pudo acceder a la lista de dispositivos.";
    console.error(err);
  }
};

const startCameraStream = async () => {
  status.value = 'Iniciando cámara...';
  // Detener cualquier stream actual
  if (videoElement.value && videoElement.value.srcObject) {
    videoElement.value.srcObject.getTracks().forEach(track => track.stop());
  }

  try {
    const constraints = {
      video: { deviceId: { exact: selectedDeviceId.value } },
      audio: true
    };
    const stream = await navigator.mediaDevices.getUserMedia(constraints);
    videoElement.value.srcObject = stream;
    status.value = 'Cámara lista.';
  } catch (err) {
    status.value = "Error: No se pudo iniciar el stream. Asegúrate de dar permisos.";
    console.error(err);
  }
};

const toggleRecording = async () => {
  if (!isRecording.value) {
    if (!videoElement.value || !videoElement.value.srcObject) {
      status.value = 'Primero selecciona una cámara.';
      return;
    }
    
    mediaRecorder = new MediaRecorder(videoElement.value.srcObject);
    recordedChunks.length = 0; 
    videoURL.value = null; 

    mediaRecorder.ondataavailable = (event) => {
      recordedChunks.push(event.data);
    };
    
    mediaRecorder.onstop = () => {
      const blob = new Blob(recordedChunks, { type: 'video/webm' });
      videoBlob.value = blob;
      videoURL.value = URL.createObjectURL(blob);
      status.value = 'Grabación finalizada. Ya puedes descargarla.';
    };

    mediaRecorder.start();
    isRecording.value = true;
    status.value = 'Grabando...';
  } else {
    mediaRecorder.stop();
    isRecording.value = false;
  }
};

onMounted(async () => {
  await getCameras();
  if (videoDevices.value.length > 0) {
    startCameraStream();
  }
});
</script>

<style scoped>
.citofonia-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  gap: 20px;
}
.video-section {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  gap: 20px;
}
video {
  width: 100%;
  max-width: 600px;
  border: 2px solid red;
}
.options-bar {
  display: flex;
  gap: 15px;
  align-items: center;
  justify-content: center;
  margin-top: 10px;
}
.record-button, .download-button {
  padding: 12px 24px;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  background-color: #f44336;
  color: white;
  text-decoration: none;
  font-size: 16px;
  font-weight: bold;
}
.download-button {
  background-color: #4caf50;
}
select {
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
  font-size: 14px;
}
</style>