<<<<<<< Updated upstream
<<<<<<< Updated upstream
// function buildMetadata(sample) {

  // @TODO: Complete the following function that builds the metadata panel

  // Use `d3.json` to fetch the metadata for a sample

//     var MetaData = `/metadata/${sample}`;
//     d3.json(MetaData).then(function(response) {
// // Use d3 to select the panel with id of `#sample-metadata`
//       var panelData = d3.select("#sample-metadata");

//     // Use `.html("") to clear any existing metadata
//       panelData.html("");

//       var data = Object.entries(response);
//       data.forEach(function(item) {
//         panelData.append("div").text(item);
//       });


//     })
 


    // Use `Object.entries` to add each key and value pair to the panel
    // Hint: Inside the loop, you will need to use d3 to append new
    // tags for each key-value in the metadata.

    // BONUS: Build the Gauge Chart
    // buildGauge(data.WFREQ);
// }


function buildCharts(City) {

var placesData = `/chinese/${City}`;
console.log(placesData);
d3.json(`/samples/${City}`).then(function(response) {
  console.log(response.otu_ids.otu_ids);
  var topOtuIDs = response.otu_ids.slice(0,10);
  var topOtuLabels = response.otu_labels.slice(0,10);
  var topSampleValues = response.sample_values.slice(0,10);
  
  var data = [{
    "labels": topOtuIDs,
    "values": topSampleValues,
    "mouseover": topOtuLabels,
    "type": "pie"
  }]
 

  Plotly.plot("pie", data);
});


// bubble chart


d3.json(sampleData).then(function(response) {
  var OtuIDs = response.otu_ids;
  var OtuLabels = response.otu_labels;
  var SampleValues = response.sample_values;
  
  var BubbleData = {
    mode: 'markers',
    x: OtuIDs,
    y: SampleValues,
    text: OtuLabels,
    marker: {color: OtuIDs, colorscale: 'Rainbow', size: SampleValues}

  };
 
var bdata = [BubbleData];

var layout = {
  showlegend: false,
  height:600,
  width: 1200
};

  Plotly.plot('bubble',bdata,layout);
})
}



function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/chinese").then((highestRating) => {
    highestRating.forEach((City) => {
      selector
        .append("option")
        .text(City)
        .property("value", City);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newCategory) {
  // Fetch new data each time a new sample is selected
  buildCharts(newCategory);
  buildMetadata(newCategory);
}

// Initialize the dashboard
init();
=======
var defaultURL = "/chinese";
d3.json(defaultURL).then(function(data) {
    var data = [data];
    var layout = { margin: { t: 30, b: 100 } };
    Plotly.plot("bar", data, layout);
});

// Update the plot with new data
function updatePlotly(newdata) {
    Plotly.restyle("bar", "x", [newdata.x]);
    Plotly.restyle("bar", "y", [newdata.y]);
}

=======
var defaultURL = "/chinese";
d3.json(defaultURL).then(function(data) {
    var data = [data];
    var layout = { margin: { t: 30, b: 100 } };
    Plotly.plot("bar", data, layout);
});

// Update the plot with new data
function updatePlotly(newdata) {
    Plotly.restyle("bar", "x", [newdata.x]);
    Plotly.restyle("bar", "y", [newdata.y]);
}

>>>>>>> Stashed changes
function getData(route) {
    console.log(route);
    d3.json(`/${route}`).then(function(data){
      console.log("newdata", data);
      updatePlotly(data);
    });
<<<<<<< Updated upstream
}
>>>>>>> Stashed changes
=======
}
>>>>>>> Stashed changes
