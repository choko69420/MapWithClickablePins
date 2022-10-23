// Initialize and add the map
function initMap() {
    // The location of Uluru
    const uluru = { lat: -25.344, lng: 131.036 };
    // The map, centered at Uluru
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 4,
        center: { lat: pins[0].latitude, lng: pins[0].longitude },
    });
    const markers = pins.map(pin => {
        return [new google.maps.Marker({ position: { lat: pin.latitude, lng: pin.longitude, post: pin.post }, map: map }), pin.post]
    });
    // add event listener to each marker
    markers.forEach(marker => {
        marker[0].addListener("click", () => {
            const postdiv = document.getElementById("post");
            postdiv.innerHTML = "";
            postdiv.innerHTML = `<h3>${marker[1].title}</h3><p>${marker[1].body}</p>`;
            console.log(marker);
        })
    })
  const marker = new google.maps.Marker({
    position: uluru,
    map: map,
  });
}

window.initMap = initMap;