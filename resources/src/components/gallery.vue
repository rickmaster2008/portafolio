<template>
  <div id="galeria">
    <carousel :perPage="3">
      <slide v-for="(item, i) in items" :key="item.id">
        <img
          :src="item.image.meta.download_url"
          :alt="item.image.title"
          @click="openLightBox(i)"
        />
      </slide>
    </carousel>
    <transition name="modal-popup">
      <div class="modal" v-if="lightbox">
        <font-awesome-icon
          icon="times"
          class="close"
          size="2x"
          @click="lightbox = false"
        />
        <img
          :src="items[lightBoxIndex].image.meta.download_url"
          :alt="items[lightBoxIndex].image.title"
        />
      </div>
    </transition>
  </div>
</template>

<script>
import { Carousel, Slide } from 'vue-carousel'
const deviceWidth = window.innerWidth
export default {
  props: {
    items: Array,
  },
  data() {
    return {
      lightbox: false,
      lightBoxIndex: 0,
      showAll: deviceWidth >= 480,
      perPage: deviceWidth >= 992 ? 8 : deviceWidth >= 768 ? 4 : 1,
    }
  },
  methods: {
    openLightBox(i) {
      this.lightBoxIndex = i
      this.lightbox = true
    },
  },
  created() {
    if (window.innerWidth <= 375) {
      this.galleryStyle['flex-wrap'] = 'no-wrap'
    }
  },
  components: {
    Carousel,
    Slide,
  },
}
</script>

<style scoped>
#galeria {
  justify-content: center;
  align-items: center;
  display: flex;
  grid-column: 2 / 6;
  grid-row: 2 / 6;
}

.item {
  min-width: 300px;
  max-width: 400px;
  padding: 0.3em;
}

img {
  width: 100%;
  cursor: pointer;
}
.modal {
  position: fixed;
  z-index: 1;
  padding-top: 100px;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background: rgba(5, 50, 71, 0.9);
}
.close {
  color: white;
  position: absolute;
  top: 10px;
  right: 25px;
  cursor: pointer;
}
.modal img {
  display: block;
  width: 90%;
  padding: 0;
  max-width: 1200px;
  margin: auto;
}

.modal-popup-enter,
.modal-popup-leave-to {
  opacity: 0;
}
.modal-popup-enter-to,
.modal-popup-leave {
  opacity: 1;
}
.modal-popup-enter-active,
.modal-popup-leave-active {
  transition: all 0.6s;
}
</style>
