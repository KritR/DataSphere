function initialize() {
    var options = {atmosphere: true, center: [0, 0], zoom: 0};
    var earth = new WE.map('earth_div', options);
    WE.tileLayer('http://tileserver.maptiler.com/nasa/{z}/{x}/{y}.jpg', {
      minZoom: 0,
      maxZoom: 5,
      attribution: 'NASA'
    }).addTo(earth);

    var marker = WE.marker([40.4, -86.9]).addTo(earth);
    marker.bindPopup("<b>This is Purdue!</b><br>I am a popup.<br /><span style='font-size:10px;color:#999'>Tip: Another popup is hidden in Cairo..</span>", {maxWidth: 150, closeButton: true}).openPopup();
  }

function fetch(year) {
    const url = `http://localhost:4000/api/v1/ex?year=${year}`
    axios.get(url).then(data => {
        console.log(data)
    }).catch(err => {
        console.log(err)
    })
}