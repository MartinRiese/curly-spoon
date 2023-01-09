from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Location
from django.urls import reverse
from .geoname import get_lat_lon
import itertools


def index(request):
    # TODO only one per person
    location_list = Location.objects.order_by('user_name', '-created')
    template = loader.get_template('whereis/index.html')

    # TODO: sql lite does not support should be replaced with query
    distinct_location_list = list(map(lambda l: list(l[1])[0], itertools.groupby(location_list, lambda l: l.user_name)))

    context = {
        'location_list': distinct_location_list,
    }
    return HttpResponse(template.render(context, request))


def add_location(request):
    # TODO: Only POST, validate fields exist
    user_name = request.POST['user_name']
    location_name = request.POST['location_name']
    print(f"looking up location for {user_name} at {location_name}")

    lat_lon = get_lat_lon(location_name)
    l = Location(user_name=user_name, location_name=location_name, lat_lon=lat_lon)
    l.save()

    return HttpResponseRedirect(reverse('whereis:index'))
