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

function getData(route) {
    console.log(route);
    d3.json(`/${route}`).then(function(data){
      console.log("newdata", data);
      updatePlotly(data);
    });
}