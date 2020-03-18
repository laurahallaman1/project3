//app.js
function buildMetadata(iso_code) {
  var meta_url = `/metadata/${iso_code}`;
  console.log(meta_url);
  var meta_data = d3.json(meta_url).then(function(data) {
    // Use d3 to select the panel with id of `#iso_code-metadata`
    var metaPanel = d3.select("#iso-code-metadata");
    metaPanel.html("");
    console.log(data);
    Object.entries(data).forEach(function([key, value]) {
      // Append a cell to the row for each value
      // in the weather report object
      var key_value = `${key}:  ${value}`;
      var para = metaPanel.append("p");
      para.text(key_value);
    })
  
  });  

  
}

function buildCharts(sample) {


}


function init() {
    // Grab a reference to the dropdown select element
    var selector = d3.select("#selDataset");
  
    // Use the list of sample names to populate the select options
    d3.json("/country_codes").then((sampleNames) => {
      sampleNames.forEach((sample) => {
        selector
          .append("option")
          .text(sample)
          .property("value", sample);
      });
  
      // Use the first sample from the list to build the initial plots
      const firstSample = sampleNames[0];
      console.log(firstSample);
      buildCharts(firstSample);
      buildMetadata(firstSample);
    });
  }
  
  function optionChanged(newSample) {
    // Fetch new data each time a new sample is selected
    buildCharts(newSample);
    buildMetadata(newSample);
  }
  
  // Initialize the dashboard
  init();