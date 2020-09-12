<template>
  <AcMap :organisations="organisations" />
</template>

<script>
import AcMap from "./components/AcMap.vue";

export default {
  name: "App",
  components: {
    AcMap,
  },
  setup() {
    const organisations = {
      caritas: {
        name: "Caritas"
      }
    }
    return {
      organisations
    };
  },
};
</script>
