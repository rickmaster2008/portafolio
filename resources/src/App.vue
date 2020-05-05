<template>
  <div id="app">
    <div id="container">
      <section id="background"></section>
      <router-view/>
    </div>
    <navbar :menu="menu" />
    <contacto />
  </div>
</template>

<script>
import Navbar from './components/navbar'
import Contacto from './components/contacto'
import axios from './axios.config.js'
export default {
  name: 'App',
  data() {
    return {
      menu: [],
    }
  },
  created() {
    axios
      .get('/menus/?slug=main-menu')
      .then(res => res.data.items[0])
      .then(menu => (this.menu = menu.menu_items))
  },
  components: {
    Navbar,
    Contacto,
  },
}
</script>

<style scoped>
#app {
  width: 100vw;
  height: 100vh;
  overflow: hidden;
}
/** estilos generales **/
#container {
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 1fr;
  height: 100vh;
  width: 100vw;
  overflow: hidden;
}
#background {
  grid-column: 1 / -1;
  grid-row: 1 / -1;
  background: url('assets/img/landscape.svg');
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
  background-attachment: fixed;
  z-index: -100;
  overflow: hidden;
}

#container {
  height: 100vh;
}
.view-show-enter {
  /* transform: scale(0); */
  opacity: 0;
}

.view-show-enter-to {
  /* transform: scale(1); */
  opacity: 1;
}

.view-show-leave {
  /* transform: scale(1); */
  opacity: 1;
}
.view-show-leave-to {
  /* transform: scale(100); */
  opacity: 0;
}
.view-show-enter-active,
.view-show-leave-active {
  transition: all 600ms linear;
}
</style>
