import requests
import haversine as hs
import functools


def get_lat_lon(location_name: str):
    """Get the latitude and longitude for a location name. Result will be as a string formatted '<lat>,<long>'"""

    url = f"http://api.geonames.org/searchJSON?q={location_name}&username=mriese"
    response = requests.request("GET", url)
    first_geo_name = response.json()['geonames'][0]
    return f"{first_geo_name['lat']},{first_geo_name['lng']}"


def distance(locations: list):
    """calculate the accumulative distance of the locations"""
    if len(locations) < 2:
        return 0
    else:
        return functools.reduce(lambda l1, l2: hs.haversine(_to(l1), _to(l2), unit=hs.Unit.KILOMETERS), locations)


def _to(lat_lon: str):
    ps = lat_lon.split(",")
    lat = float(ps[0])
    lon = float(ps[1])
    return lat, lon


lls = ['50.9787,11.03283', '51.01454,11.04377']
print(distance(locations=lls))
