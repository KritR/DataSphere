var earth;
var curMarkers = [];

function initialize() {
    const options = { atmosphere: true, center: [0, 0], zoom: 0 };
    earth = new WE.map('earth_div', options);
    WE.tileLayer('http://tileserver.maptiler.com/nasa/{z}/{x}/{y}.jpg', {
        minZoom: 0,
        maxZoom: 5,
        attribution: 'NASA'
    }).addTo(earth);

}

var interval = 0;

function fade_out() {
    const splash = document.querySelector('#splash');
    opacity = Number(window.getComputedStyle(splash).getPropertyValue("opacity"));
    if (opacity > 0) {
        opacity = opacity - 1.0;
        splash.style.opacity = opacity;
    } else {
        clearInterval(interval);
        splash.parentNode.removeChild(splash);
    }
}

function close_splash() {
    interval = setInterval(fade_out, 20);
}

function change_year_label() {
    yearLabel = document.getElementById("yearLabel")
    slider = document.getElementById("myRange")
    yearLabel.innerHTML = parseInt(slider.value) + 1920
}

function fetch_markers() {
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
            marker.bindPopup(`<b>${event.title}</b><br>${event.description}<br/><span style='font-size:10px;color:#999'></span>`, { maxWidth: 150, closeButton: true });
            curMarkers.push(marker)
        }
    }).catch(err => {
        console.log(err)
    })
}