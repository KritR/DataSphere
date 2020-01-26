var earth;
var curMarkers = [];
var before = null;
var myReq;

var year = 2020;
var month = 1;

function initialize() {
    const options = { atmosphere: true, center: [0, 0], zoom: 0 };
    earth = new WE.map('earth_div', options);
    WE.tileLayer('https://tileserver.maptiler.com/nasa/{z}/{x}/{y}.jpg', {
        minZoom: 0,
        maxZoom: 5,
        attribution: 'NASA'
    }).addTo(earth);

    // Start a simple rotation animation
    myReq = requestAnimationFrame(function animate(now) {
        var c = earth.getPosition();
        var elapsed = before ? now - before : 0;
        before = now;
        earth.setCenter([c[0], c[1] + 0.8 * (elapsed / 30)]);
        myReq = requestAnimationFrame(animate);
    });
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
    window.cancelAnimationFrame(myReq);
    fetch_markers();
}

const months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

function change_year_label() {
    if (data == "news") {
        yearLabel = document.getElementById("yearLabel");
        slider = document.getElementById("myRange");
        year = 2010 + Math.floor(parseInt(slider.value) / 12);
        month = parseInt(slider.value) % 12 + 1;
        let month_string = months[month - 1];
        yearLabel.innerHTML = month_string + " " + year;
    } else if (data == "earthquakes") {
        yearLabel = document.getElementById("yearLabel");
        slider = document.getElementById("myRange");
        year = -500 + 100 * Math.floor(parseInt(slider.value) / 4.8);
        if (year < 0) {
            yearLabel.innerHTML = -year + "'s BCE";
        } else {
            yearLabel.innerHTML = year + "'s CE";
        }
    }
}

function fetch_markers() {
    for (const marker of curMarkers) {
        marker.detach()
    }
    curMarkers = []
    fetch()
}

function show_info(title, url, description) {
    document.querySelector("#info_panel").style.opacity = 1;
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    document.querySelector("#info_title").innerHTML = title;
    document.querySelector("#info_url").innerHTML = "<a href='" + url + "'>" + url + "</a>";
    document.querySelector("#info_description").innerHTML = description;
}

function fetch() {
    const url = `https://api.datasphere.space/api/v1/ex`
    axios.get(url, {
        params: {
            year: year,
            month: month
        }
    }).then(res => {
        console.log(res.data.data)
        for (const event of res.data.data) {
            var marker = WE.marker([event.location.lat, event.location.lon]).addTo(earth);
            marker.element.addEventListener("click", function () {
                show_info(event.title, event.url, event.description);
            });
            //marker.
            //marker.bindPopup(`<b>${event.title}</b><br>${event.description}<br/><span style='font-size:10px;color:#999'></span>`, { maxWidth: 150, closeButton: true });
            curMarkers.push(marker);
        }
    }).catch(err => {
        console.log(err);
    })
}

var data = "news";
function handleDataChange(radio) {
    data = radio.value;
    change_year_label();
}