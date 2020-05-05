<template>
  <section id="acerca" data-view="acerca" class="view">
    <img
      class="perfil"
      :src="`http://localhost:8000${picture}`"
      alt="foto-de-perfil"
    />
    <div class="social-wrapper">
      <a
        class="icon"
        v-for="socialIcon in socialIcons"
        :key="socialIcon.id"
        :href="socialIcon.link"
        target="_blank"
      >
        <font-awesome-icon :icon="['fab', socialIcon.icon]" />
      </a>
    </div>
    <div class="presentation" v-html="presentation"></div>
  </section>
</template>

<script>
import axios from '../axios.config'
export default {
  props: {
    pageId: Number,
  },
  data() {
    return {
      picture: '',
      socialIcons: [],
      presentation: '',
    }
  },
  created() {
    axios
      .get(`/pages/${this.$route.name}/`)
      .then(res => res.data)
      .then(page => {
        this.presentation = page.presentation
        this.socialIcons = page.social_icons
        this.picture = page.picture.meta.download_url
      })
  },
}
</script>

<style scoped>
.perfil {
  width: 120px;
  border-radius: 100px;
}
.social-wrapper {
  display: flex;
}
.icon {
  margin: 1em;
  color: white;
}
#acerca {
  grid-column: 1 / -1;
  grid-row: 1 / -1;
  position: relative;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: white;
  background: transparent;
}

.presentation {
  max-width: 600px;
  padding: 1em;
  background: rgba(0, 0, 0, 0.4);
  border-radius: 10px;
  margin: 0.3em;
}

@media (min-width: 320px) and (max-width: 480px) {
  #acerca p {
    font-size: 0.8em;
  }
}
</style>
