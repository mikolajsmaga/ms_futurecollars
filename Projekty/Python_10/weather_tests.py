#____Mozliwosc testow____
print("Witamy w programie testowym - v1.0 Alpha")
geolocator = Nominatim(user_agent="mikola_smaga_app")
location = geolocator.geocode(city)
print(location.address)
print((location.latitude, location.longitude))
print(location.raw)
