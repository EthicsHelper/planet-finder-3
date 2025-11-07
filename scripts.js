// Sample planetary data (replace later with NASA data)
const planetData = [
  { name: "Earth", R: 8.2, z: 0.02, Plife: 1.0 },
  { name: "Mars", R: 1.5, z: 0.1, Plife: 0.65 },
  { name: "Proxima b", R: 4.2, z: 0.05, Plife: 0.83 },
  { name: "Kepler-452b", R: 6.7, z: 0.03, Plife: 0.92 },
  { name: "Venus", R: 0.72, z: 0.05, Plife: 0.30 }
];

// Plot the map using Plotly
function plotMap(data) {
  const trace = {
    x: data.map(p => p.R),
    y: data.map(p => p.z),
    mode: 'markers',
    marker: {
      color: data.map(p => p.Plife),
      colorscale: 'Viridis',
      size: 12,
      opacity: 0.8
    },
    text: data.map(p => `${p.name}<br>Life Probability: ${p.Plife}`),
    hoverinfo: 'text'
  };

  const layout = {
    title: 'Life Finder Map',
    xaxis: { title: 'Radial Distance (kpc)' },
    yaxis: { title: 'Vertical Distance (kpc)' },
    paper_bgcolor: '#f4f4f9',
    plot_bgcolor: '#f4f4f9'
  };

  Plotly.newPlot('lifeFinderMap', [trace], layout);
}

// Update map when slider changes
function updateMapWithThreshold(threshold) {
  const filtered = planetData.filter(p => p.Plife >= threshold);
  plotMap(filtered);
}

document.getElementById('lifeThresholdSlider').addEventListener('input', e => {
  const threshold = parseFloat(e.target.value);
  document.getElementById('lifeThresholdValue').innerText = threshold.toFixed(2);
  updateMapWithThreshold(threshold);
});

// Initialize map on load
updateMapWithThreshold(0.5);
