import requests


def get_lat_lon(location_name: str):
    url = f"http://api.geonames.org/searchJSON?q={location_name}&username=mriese"
    response = requests.request("GET", url)
    first_geo_name = response.json()['geonames'][0]
    return f"{ first_geo_name['lat'] },{ first_geo_name['lng'] }"


print(get_lat_lon("Paris"))