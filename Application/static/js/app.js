var responselat = d3.json("/chinese/lat");
var responselon = d3.json("/chinese/lon");

console.log(responselat)
console.log(responselon)





function createMap(places) {

  // Create the tile layer that will be the background of our map
  var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, <a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"http://mapbox.com\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.light",
    accessToken: API_KEY
  });

  // Create a baseMaps object to hold the lightmap layer
  var baseMaps = {
    "Light Map": lightmap
  };

  // Create an overlayMaps object to hold the bikeStations layer
  var overlayMaps = {
    "places": Places
  };

  // Create the map object with options
  var map = L.map("map-id", {
    center: [39.096977, -94.578681],
    zoom: 12,
    layers: [lightmap, places]
  });

  // Create a layer control, pass in the baseMaps and overlayMaps. Add the layer control to the map
  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(map);
}

function createMarkers(response) {

  // Pull the "stations" property off of response.data
  // var places = response.Place_Name;
  // // Initialize an array to hold bike markers
  // var placeMarkers = [];
  // Object.entries(response).forEach(([key, value]) => 
  //   console.log(`Key: ${key} and Value ${value}`)
  
  // Loop through the stations array
  for (var index = 0; index < responselat.length; index++) {

    // For each station, create a marker and bind a popup with the station's name
    var placeMarker = L.marker(responselat, responselon)
      .bindPopup("<h3>" + responselat + responselon + "<h3>");

    // Add the marker to the bikeMarkers array
    placeMarkers.push(placeMarker);
  }


  // // Create a layer group made from the bike markers array, pass it into the createMap function
createMap(L.layerGroup(placeMarkers));
};

