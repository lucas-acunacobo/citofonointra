<template>
  <div class="videos-container">
    <aside class="sidebar">
      <h2>Mis Grabaciones</h2>
      <VideoList :usuario-id="usuarioId" @videoSelected="playVideo" />
    </aside>

    <main class="player">
      <div v-if="selectedVideo">
        <video
          v-if="selectedVideo"
          :src="selectedVideo"
          controls
          autoplay
        ></video>
      </div>
      <div v-else class="placeholder">
        <p>Selecciona un video para reproducir</p>
      </div>
    </main>
  </div>
</template>

<script>
import VideoList from "../components/videoList.vue";
import {getRecord} from "../services/videos.js";
import Cookies from "js-cookie";

export default {
  name: "VideosView",
  components: { VideoList },
  data() {
    return {
      usuarioId: Cookies.get("usuario"),
      selectedVideo: null,
    };
  },
  methods: {
    async playVideo(id) {
    try {
      const response = await getRecord(id); 
      this.selectedVideo = URL.createObjectURL(response.data);
    } catch (error) {
      console.error("Error cargando el video:", error);
    }
  },
  },
};
</script>

<style>
.videos-container {
  display: flex;
  height: 100vh;
  font-family: Arial, sans-serif;
}

.sidebar {
  width: 25%;
  background: #f5f5f5;
  border-right: 1px solid #ddd;
  padding: 16px;
  overflow-y: auto;
}

.sidebar h2 {
  font-size: 18px;
  margin-bottom: 12px;
}

.player {
  flex: 1;
  padding: 20px;
}

.player h3 {
  margin-bottom: 12px;
}

.player video {
  max-width: 100%;
  max-height: 70vh;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.placeholder {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #777;
}
</style>
