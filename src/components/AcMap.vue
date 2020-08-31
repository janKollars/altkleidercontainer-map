<template>
  <div class="ac-map" ref="map" tabindex="0">
    <div v-show="popupActive" class="ac-map__popup" ref="popup">
      {{ popupContent.street }},<br />
      {{ popupContent.postal }} {{ popupContent.state }}
    </div>
  </div>
</template>

<script>
import "ol/ol.css";
import { Map, View, Feature, Overlay } from "ol";
import { Point } from "ol/geom";
import TileLayer from "ol/layer/Tile";
import VectorLayer from "ol/layer/Vector";
import { fromLonLat } from "ol/proj";
import { OSM, Vector as VectorSource } from "ol/source";
import { Icon, Style } from "ol/style";
import { ref } from "vue";

export default {
  name: "AcMap",
  props: {
    mapData: {
      type: Object,
      required: true,
    },
  },
  setup() {
    return {
      popupActive: ref(false),
      popupContent: ref({}),
    };
  },
  mounted() {
    this.$refs.map.focus();

    const map = new Map({
      target: this.$refs.map,
      layers: [
        new TileLayer({
          source: new OSM({
            attributions: [
              '© <a href="https://www.openstreetmap.org/copyright" rel="noopener" target="_blank">OpenStreetMap</a> contributors.',
              'Daten <a href="https://www.carla-wien.at/spenden/kleidercontainer/" rel="noopener" target="_blank">Caritas Wien</a>'
            ]
          }),
        }),
      ],
      view: new View({
        center: fromLonLat([16.363449, 48.210033]),
        zoom: 12,
        extent: [...fromLonLat([15.8, 47.42]), ...fromLonLat([17.08, 48.8])],
      }),
    });

    const pinIcon = new Icon({
      anchor: [0.5, 1],
      anchorXUnits: "fraction",
      anchorYUnits: "fraction",
      src: "pin.svg",
      imageSize: 24,
    });

    const pinStyle = new Style({
      image: pinIcon,
    });

    setTimeout(() => {
      const points = [];
      for (const organisation in this.mapData) {
        for (const location of this.mapData[organisation]) {
          if (!(location.lon && location.lat)) continue;
          const point = new Feature({
            geometry: new Point(fromLonLat([location.lon, location.lat])),
            ...location,
          });
          point.setStyle(pinStyle);
          points.push(point);
        }
      }

      const vectorLayer = new VectorLayer({
        source: new VectorSource({
          features: points,
        }),
      });
      map.addLayer(vectorLayer);

      const popupOverlay = new Overlay({
        element: this.$refs.popup,
        positioning: "bottom-center",
        offset: [0, -24],
      });
      map.addOverlay(popupOverlay);

      map.addEventListener("click", (event) => {
        if (event.target === this.$refs.popup) {
          return;
        }
        const feature = map.forEachFeatureAtPixel(
          event.pixel,
          (feature) => feature
        );
        if (feature) {
          const coordinates = feature.getGeometry().getCoordinates();
          popupOverlay.setPosition(coordinates);
          this.popupContent = { ...feature.values_ };
          this.popupActive = true;
        } else {
          this.popupActive = false;
        }
      });

      let currZoom = map.getView().getZoom();
      map.addEventListener("moveend", () => {
        const newZoom = map.getView().getZoom();
        if (currZoom != newZoom) {
          if (
            (currZoom < 13 && newZoom >= 13) ||
            (currZoom >= 13 && newZoom < 13)
          ) {
            pinIcon.setScale(newZoom >= 13 ? 1.75 : 1);
            popupOverlay.setOffset([0, newZoom >= 13 ? -24 * 1.75 : -24]);
            vectorLayer.getSource().changed();
          }
          currZoom = newZoom;
        }
      });

      map.addEventListener("pointermove", (event) => {
        const pixel = map.getEventPixel(event.originalEvent);
        const hit = map.hasFeatureAtPixel(pixel);
        map.getTarget().style.cursor = hit ? "pointer" : "";
      });
    }, 1);
  },
};
</script>

<style>
.ac-map {
  height: 100vh;
}

.ac-map__popup {
  position: relative;
  padding: 0.5rem;
  width: 40ch;
  max-width: calc(100vw - 0.5rem);
  min-height: 2rem;
  background-color: white;
  border-radius: 5px;
  filter: drop-shadow(0 5px 10px black);
  margin-bottom: 10px;
}

.ac-map__popup::after {
  content: "";
  position: absolute;
  top: 100%;
  left: calc(50% - 10px);
  width: 20px;
  height: 10px;
  background-color: white;
  clip-path: polygon(0 0, 100% 0, 50% 100%);
}
</style>
