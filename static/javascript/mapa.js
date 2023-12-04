let map = L.map('map').setView([21.0181,-101.258],15)

//Agregar tilelAyer mapa base desde openstreetmap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

document.getElementById('select-location').addEventListener('change',function(e){
  let coords = e.target.value.split(",");
  map.flyTo(coords,18);
})

// Agregar un marcador
var marker1 = L.circleMarker(L.latLng(21.0189180,-101.2584613), {
  radius: 6,
  fillColor: "#C0392B",
  color: "black",
  weight: 2,
  opacity: 1,
  fillOpacity: 1,
}).addTo(map).bindPopup("Alhóndiga de Granaditas");

// Agregar un marcador
var marker2 = L.circleMarker(L.latLng(21.0144923,-101.2545417), {
  radius: 6,
  fillColor: "#9B59B6",
  color: "black",
  weight: 2,
  opacity: 1,
  fillOpacity: 1,
}).addTo(map).bindPopup("Monumento al Pípila");

// Agregar un marcador
var marker3 = L.circleMarker(L.latLng(21.0164947,-101.2534303), {
  radius: 6,
  fillColor: "#2980B9",
  color: "black",
  weight: 2,
  opacity: 1,
  fillOpacity: 1,
}).addTo(map).bindPopup("Basílica Colegiata de Nuestra Señora de Guanajuato");

// Agregar un marcador
var marker4 = L.circleMarker(L.latLng(21.016331,-101.2565218), {
  radius: 6,
  fillColor: "#1ABC9C",
  color: "black",
  weight: 2,
  opacity: 1,
  fillOpacity: 1,
}).addTo(map).bindPopup("Callejón del beso");

// Agregar un marcador
var marker5 = L.circleMarker(L.latLng(21.0182835,-101.2551951), {
  radius: 6,
  fillColor: "#27AE60",
  color: "black",
  weight: 2,
  opacity: 1,
  fillOpacity: 1,
}).addTo(map).bindPopup("Museo Casa Diego Rivera");

// Agregar un marcador
var marker6 = L.circleMarker(L.latLng(21.0158316,-101.2529488), {
  radius: 6,
  fillColor: "#F1C40F",
  color: "black",
  weight: 2,
  opacity: 1,
  fillOpacity: 1,
}).addTo(map).bindPopup("Jardín Unión");

// Agregar un marcador
var marker7 = L.circleMarker(L.latLng(21.0175111,-101.2582807), {
  radius: 6,
  fillColor: "#E47D22",
  color: "black",
  weight: 2,
  opacity: 1,
  fillOpacity: 1,
}).addTo(map).bindPopup("Mercado Hidalgo");

// Agregar un marcador
var marker8 = L.circleMarker(L.latLng(21.0200597,-101.2665268), {
  radius: 6,
  fillColor: "#FFFFFF",
  color: "black",
  weight: 2,
  opacity: 1,
  fillOpacity: 1,
}).addTo(map).bindPopup("Museo de las momias de Guanajuato");

// Agregar un marcador
var marker9 = L.circleMarker(L.latLng(21.0154679,-101.2530315), {
  radius: 6,
  fillColor: "#0000FF",
  color: "black",
  weight: 2,
  opacity: 1,
  fillOpacity: 1,
}).addTo(map).bindPopup("Teatro Juárez");

// Agregar un marcador
var marker10 = L.circleMarker(L.latLng(21.0172625,-101.253583), {
  radius: 6,
  fillColor: "#00FFFF",
  color: "black",
  weight: 2,
  opacity: 1,
  fillOpacity: 1,
}).addTo(map).bindPopup("Universidad de Guanajuato");

//Agregar una leyenda
const legend = L.control.Legend({
  position: "bottomright",
  collapsed: false,
  symbolWidth: 14,
  opacity:1,
  column:1,
  legends: [
      {
          label: "Alhóndiga de Granaditas",
          type: "circle",
          radius: 6,
          color: "black",
          fillColor: "#C0392B",
          fillOpacity: 1,
          weight: 2,
          layers: [marker1],
          inactive: false,
      },
      {
        label: "Monumento al Pípila",
        type: "circle",
        radius: 6,
        color: "black",
        fillColor: "#9B59B6",
        fillOpacity: 1,
        weight: 2,
        layers: [marker2],
        inactive: false,
      },
      {
        label: "Basílica Colegiata",
        type: "circle",
        radius: 6,
        color: "black",
        fillColor: "#2980B9",
        fillOpacity: 1,
        weight: 2,
        layers: [marker3],
        inactive: false,
      },
      {
        label: "Callejón del beso",
        type: "circle",
        radius: 6,
        color: "black",
        fillColor: "#1ABC9C",
        fillOpacity: 1,
        weight: 2,
        layers: [marker4],
        inactive: false,
      },
      {
        label: "Museo Casa Diego Rivera",
        type: "circle",
        radius: 6,
        color: "black",
        fillColor: "#27AE60",
        fillOpacity: 1,
        weight: 2,
        layers: [marker5],
        inactive: false,
      },
      {
        label: "Jardín Unión",
        type: "circle",
        radius: 6,
        color: "black",
        fillColor: "#F1C40F",
        fillOpacity: 1,
        weight: 2,
        layers: [marker6],
        inactive: false,
      },
      {
        label: "Mercado Hidalgo",
        type: "circle",
        radius: 6,
        color: "black",
        fillColor: "#E47D22",
        fillOpacity: 1,
        weight: 2,
        layers: [marker7],
        inactive: false,
      },
      {
        label: "Museo de las momias de Guanajuato",
        type: "circle",
        radius: 6,
        color: "black",
        fillColor: "#FFFFFF",
        fillOpacity: 1,
        weight: 2,
        layers: [marker8],
        inactive: false,
      },
      {
        label: "Teatro Juárez",
        type: "circle",
        radius: 6,
        color: "black",
        fillColor: "#0000FF",
        fillOpacity: 1,
        weight: 2,
        layers: [marker9],
        inactive: false,
      },
      {
        label: "Universidad de Guanajuato",
        type: "circle",
        radius: 6,
        color: "black",
        fillColor: "#00FFFF",
        fillOpacity: 1,
        weight: 2,
        layers: [marker10],
        inactive: false,
      }]
      }).addTo(map);