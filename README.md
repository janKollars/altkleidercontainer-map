# Altkleidercontainer-Map Österreich

Webapp zur Anzeige der Altkleidercontainer auf einer Karte


## Datenquellen

Aktuell wird nur eine [Tabelle](https://www.carla-wien.at/fileadmin/storage/wien/shops-services/carla/Kleidercontainer_EDW_Gesamt_Stand_V01_06022020.pdf) der Caritas Wien verwendet. Gerne werden Beiträge zur Erweiterung der Organisationen angenommen.

Das Rote Kreuz Wien bietet bereits eine [Karte](https://www.google.com/maps/d/viewer?mid=1QQ8mc-Cm8L6YSvhMXz9tS1jITfOmSZLS) der Altkleidercontainer.

Das Kartenmaterial stammt von [OpenStreetMap](https://www.openstreetmap.org/).


## Lokales Setup

Voraussetzung ist, dass Node.js in einer aktuellen Version installiert ist.

Zur Installation der Abhängigkeiten ist im Verzeichnis das auszuführen:
```
npm install
```

Anschließend, kann die Webapp lokal gestartet werden:
```
npm run dev
```

Jetzt kann sie auf `localhost:3000` betrachtet werden.
