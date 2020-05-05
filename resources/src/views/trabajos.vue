<template>
  <section id="trabajos" data-view="trabajos" class="view">
    <h1>{{title}}</h1>
    <gallery :items="works" />
  </section>
</template>

<script>
import Gallery from '@/components/gallery'
import axios from '../axios.config'
export default {
  data() {
    return {
      title: '',
      works: [],
    }
  },
  created() {
    axios.get(`pages/${this.$route.name}/`).then(res => res.data).then(page => {
      console.log(page)
      this.works = page.works
      this.title = page.title
    })
  },
  components: { Gallery },
}
</script>

<style scoped>
h1 {
  color: 093246;
  padding-top: 3em;
  padding-bottom: 1.3em;
  text-align: center;
  font-size: 2em;
}

#trabajos {
  grid-column: 1 / -1;
  grid-row: 1 / -1;
  height: 100vh;
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  grid-template-rows: repeat(6, 1fr);
  justify-items: center;
  align-items: center;
  /* transform: scale(0); */
}
#trabajos h1 {
  grid-row: 1 / 2;
  grid-column: 1 / -1;
}

#trabajos .arrow {
  cursor: pointer;
  color: rgba(0, 0, 0, 0.3);
  padding: 0.5em;
  z-index: 3;
}

#trabajos #arrow-left {
  grid-column: 1 / 2;
  grid-row: 2 / 6;
}

#trabajos #arrow-right {
  grid-column: 6 / 7;
  grid-row: 2 / 6;
}

@media (max-width: 480px) {
  h1 {
    padding-bottom: 0;
  }
}
</style>
