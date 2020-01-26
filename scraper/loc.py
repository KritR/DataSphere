import geopy

geopy.geocoders.options.default_user_agent = "wikiglobe"
geolocator = geopy.geocoders.Nominatim()
city = "Sarajevo"
loc = geolocator.geocode(city)
if loc:
    print("latitude: ", loc.latitude, "\nlongtitude: ", loc.longitude)
else:
    print("location not found")