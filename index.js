var earth;
var curMarkers = []; 

function initialize() {
      const options = {atmosphere: true, center: [0, 0], zoom: 0};
      earth = new WE.map('earth_div', options);
      WE.tileLayer('http://tileserver.maptiler.com/nasa/{z}/{x}/{y}.jpg', {
      minZoom: 0,
      maxZoom: 5,
      attribution: 'NASA'
    }).addTo(earth);

}

function change_year() {
    yearLabel = document.getElementById("yearLabel")
    slider = document.getElementById("myRange")
    yearLabel.innerHTML = parseInt(slider.value) + 1920
    for (const marker of curMarkers) {
        marker.detach()
    }
    curMarkers = []
    fetch()
}

function fetch(year) {
    const url = `http://localhost:4000/api/v1/ex`
    axios.get(url).then(res => {
        console.log(res.data.data)
        for (const event of res.data.data) {
            var marker = WE.marker([event.location.lat, event.location.lon]).addTo(earth);
            marker.bindPopup(`<b>${event.title}</b><br>${event.description}<br/><span style='font-size:10px;color:#999'></span>`, {maxWidth: 150, closeButton: true});
            curMarkers.push(marker)
        }
    }).catch(err => {
        console.log(err)
    })
}