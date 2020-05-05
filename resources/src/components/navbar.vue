<template>
  <div id="menu">
    <transition name="menu-popover">
      <ul v-if="open">
        <li v-for="m in menu" :key="m.id">
          <router-link :to="m.link" class="menu-item-link">
            {{ m.title }}
          </router-link>
        </li>
      </ul>
    </transition>
    <button @click="openNav" id="menu-trigger">
      <transition name="menu-trigger">
        <font-awesome-icon icon="bars" v-if="!open" class="manu-trigger-icon" />
      </transition>
      <transition name="menu-trigger">
        <font-awesome-icon v-if="open" icon="times" class="menu-trigger-icon" />
      </transition>
    </button>
  </div>
</template>

<script>
export default {
  props: {
    menu: Array,
  },
  data() {
    return {
      open: false,
    }
  },
  methods: {
    openNav() {
      this.open = !this.open
    },
    onClick(e) {
      e.preventDefault()
      const section = e.target.dataset.section
      this.$emit('navigate', section)
      this.open = false
    },
  },
}
</script>

<style scoped>
#menu {
  position: fixed;
  bottom: 25px;
  left: 25px;
}

#menu ul {
  list-style: none;
  font-weight: bold;
  transform-origin: bottom left;
  background: rgba(9, 89, 112, 1);
  padding: 0 2em;
  border-radius: 10px;
}

#menu li {
  padding: 2em 0;
}

#menu a {
  color: white;
  text-decoration: none;
}

#menu-trigger {
  padding: 20px;
  background: none;
  border: none;
  border-radius: 100px;
  width: 60px;
  color: white;
  font-weight: bold;
  background: #206275;
}

#menu-trigger:hover {
  cursor: pointer;
}

#menu-trigger:focus {
  outline: none;
}

.menu-popover-enter,
.menu-popover-leave-to {
  transform: scale(0);
}
.menu-popover-enter-to,
.menu-popover-leave {
  transform: scale(1);
}
.menu-popover-enter-active,
.menu-popover-leave-active {
  transition: transform 200ms linear;
}

.menu-trigger-enter,
.menu-trigger-leave-to {
  transform: scale(0);
  opacity: 0;
}
.menu-trigger-enter-to,
.menu-trigger-leave {
  transform: scale(1) rotate(360deg);
  opacity: 1;
}
.menu-trigger-enter-active,
.menu-trigger-leave-active {
  transition: all 100ms ease-in-out;
}
</style>
