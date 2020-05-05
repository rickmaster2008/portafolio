<template>
  <section id="home" data-view="home" class="view">
    <h1>
      {{ featuredTitle }}
    </h1>
    <p>{{ tagline }}</p>
  </section>
</template>

<script>
import axios from '../axios.config'
export default {
  data() {
    return {
      featuredTitle: '',
      tagline: '',
    }
  },
  created() {
    axios
      .get(`/pages/${this.$route.name}/`)
      .then(res => res.data)
      .then(page => {
        this.featuredTitle = page.featured_title
        this.tagline = page.tagline
      })
  },
}
</script>

<style scoped>
#home {
  grid-column: 1 / -1;
  grid-row: 1 / -1;
  height: 100vh;
  width: 100vw;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: transparent;
}

.perfil {
  width: 120px;
  border-radius: 100px;
}

h1 {
  font-family: 'Sacramento';
  font-size: 6em;
  text-align: center;
}

h1,
p {
  color: white;
  font-weight: bold;
}

p {
  font-size: 1.5em;
}

@media (max-width: 480px) {
  h1 {
    margin-bottom: 0;
  }
}
</style>
