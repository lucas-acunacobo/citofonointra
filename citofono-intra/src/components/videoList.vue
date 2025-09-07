<template>
  <div>
    <div
      v-for="video in videos"
      :key="video.id"
      class="video-item"
      @click="selectVideo(video.id)"
    >
      <p>{{ video.fecha }}</p>
    </div>
  </div>
</template>

<script>
import Cookies from "js-cookie";
import { getUsersRecords } from "../services/videos";

export default {
  name: "VideoList",
  data() {
    return { videos: [] };
  },
  async mounted() {
    try {
      const id = Cookies.get("usuario");
      const response = await getUsersRecords(id);
      this.videos = response.data.map(v => ({
        id: v.id,
        archivo: v.archivo,
        fecha:v.creado_en,
      }));
    } catch (error) {
      console.error("Error al cargar videos:", error);
    }
  },
  methods: {
    selectVideo(videoId) {
      this.$emit("videoSelected", videoId);
    },
  },
};
</script>

<style>
.video-item {
  cursor: pointer;
  margin-bottom: 12px;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background: white;
  transition: background 0.2s;
}

.reproductor-img {
  width: 250px; /* Ejemplo: 100 píxeles de ancho */
  height: 150px; /* Mantiene la proporción original de la imagen */
  /* O puedes usar un ancho máximo */
  /* max-width: 200px; */
  /* max-height: 150px; */
}
.video-item:hover {
  background: #eaeaea;
}

.video-item video {
  width: 100%;
  height: 120px;
  object-fit: cover;
  display: block;
  margin-bottom: 4px;
}
</style>
