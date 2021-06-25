



 // Define streetmap layer
 var streetmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    tileSize: 512,
    maxZoom: 18,
    zoomOffset: -1,
    id: "light-v10",
    accessToken: API_KEY
  });


  // Define a baseMaps object to hold our map layers
  var baseMaps = {
    "US map": streetmap
    
  };
  
// Create our map, giving it the streetmap and earthquakes layers to display on load
var myMap = L.map("map", {
    center: [ 37.09, -95.71 ],
    zoom: 4,
    layers: [streetmap]     //default selected layer
    });


// Add streetmap tile to map
streetmap.addTo(myMap);


// // create overlay layers
var elections = new L.LayerGroup();
// var population = new L.LayerGroup();


// // Create overlay object to hold the overlay layer
var overlayMaps = {
  "Vaccination rate": elections
  // "Population": population
};

// // Create a layer control
L.control.layers(baseMaps, overlayMaps, {
  collapsed: true //shows or hide the legend
}).addTo(myMap);


  // Create a GeoJSON layer containing the features array on the electionData object
  // Run the onEachFeature function once for each piece of data in the array

  L.geoJson(data, {
    onEachFeature: function(feature, layer) {
      layer.bindPopup("<h3> State:" + feature.properties.NAME +
      "</h3><hr><p> Vaccination rate:"+ feature.properties.vac_ratio*100 +"%"+"</h3><p> Population:" + feature.properties.population + "</p>");
    }
    // pointToLayer: function(feature, latlng) {
    //   return new L.CircleMarker(latlng, {
    //     radius: feature.properties.mag * 6, 
    //     color: depthColor(feature.geometry.coordinates[2]),  
    //     fillOpacity: 0.85
      // });
  
  }).addTo(elections);


  elections.addTo(myMap);

