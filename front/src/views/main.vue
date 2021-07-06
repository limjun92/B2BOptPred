<template>
  <div class="wrapper" :class="{ 'nav-open': $sidebar.showSidebar }">
      <h1>home</h1>
    <signUp/>
    <sidebar-fixed-toggle-button />
        <side-bar
      :background-color="sidebarBackground"
      :short-title="sidebar.shortTitle"
      :title="sidebar.title"
    >
    <template slot="links">
        <sidebar-item
          :link="{
            name: sidebar.dashboard,
            icon: 'tim-icons icon-chart-pie-36',
            path: '/'
          }"
        >
        </sidebar-item>
        <sidebar-item
          :link="{ name: sidebar.pages, icon: 'tim-icons icon-image-02' }"
        ><sidebar-item
            :link="{ name: sidebar.pricing, path: '/pricing' }"
          ></sidebar-item>
        </sidebar-item>
        </template>

        </side-bar>
  </div>
</template>

<script>
import PerfectScrollbar from 'perfect-scrollbar';
import signUp from '@/components/user/signUp.vue'
import SidebarFixedToggleButton from '@/components/sidebar/SidebarFixedToggleButton.vue'
function hasElement(className) {
  return document.getElementsByClassName(className).length > 0;
}
function initScrollbar(className) {
  if (hasElement(className)) {
    new PerfectScrollbar(`.${className}`);
  } else {
    // try to init it later in case this component is loaded async
    setTimeout(() => {
      initScrollbar(className);
    }, 100);
  }
}
export default {
  name: 'Main',
  components: {
    signUp,
    SidebarFixedToggleButton,
  },
    data() {
    return {
      sidebarBackground: 'vue' //vue|blue|orange|green|red|primary
    };
  },
  methods:{
    initScrollbar() {
      let docClasses = document.body.classList;
      let isWindows = navigator.platform.startsWith('Win');
      if (isWindows) {
        // if we are on windows OS we activate the perfectScrollbar function
        initScrollbar('sidebar');
        initScrollbar('main-panel');
        initScrollbar('sidebar-wrapper');

        docClasses.add('perfect-scrollbar-on');
      } else {
        docClasses.add('perfect-scrollbar-off');
      }
    },
    toggleSidebar() {
      if (this.$sidebar.showSidebar) {
        this.$sidebar.displaySidebar(false);
      }
    },
  },
  mounted() {
    this.initScrollbar();
  }
}
</script>
