<template>
  <AcMap :map-data="mapData" />
</template>

<script>
import AcMap from "./components/AcMap.vue";
import caritasData from "../public/caritas.json";

export default {
  name: "App",
  components: {
    AcMap,
  },
  setup() {
    return {
      mapData: {
        caritas: caritasData,
      },
    };
  },
};
</script>
