from geopy.geocoders import Nominatim
import time

"""
Returns lat/long given place name:
    (latitude, longitude) if found otherwise None
"""
def get_coordinates_simple(place: str):
    geolocator = Nominatim(user_agent="my_simple_geocoder", timeout=10)
    location = geolocator.geocode(place)
    if location:
        return (location.latitude, location.longitude)
    return None

"""
Returns place name given lat/long otherwise None
"""
def get_place_simple(latitude: float, longitude: float):
    geolocator = Nominatim(user_agent="my_simple_geocoder", timeout=10)
    location = geolocator.reverse((latitude, longitude), exactly_one=True)
    if location:
        return location.address
    return None

if __name__ == "__main__":
    timenow = time.time()

    # Forwrd geocoding test
    place_name = "Paris, Italy"
    coords = get_coordinates_simple(place_name)
    print(f"Coordinates for '{place_name}': {coords}")

    # Reverse geocoding test
    lat, lon = 28.5383, -81.3792
    address = get_place_simple(lat, lon)
    print(f"Address for {lat}, {lon}: {address}")

    print("---"*4)
    print(f"Time taken: {time.time() - timenow:.2f} seconds")
