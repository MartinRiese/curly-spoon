from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Location
from django.urls import reverse
from .geotools import distance, get_lat_lon
import itertools


def index(request):
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


def details(request, user_name):
    location_list = Location.objects.filter(user_name=user_name).order_by('-created')
    if len(location_list) < 1:
        raise Http404("No user with this name in the data base")

    # total_distance = distance(list(map(lambda l: l.lat_lon, location_list)))
    # print(total_distance)
    template = loader.get_template('whereis/details.html')

    context = {
        'user_name': user_name,
        'location_list': location_list,
        # 'total_distance': total_distance,
    }
    return HttpResponse(template.render(context, request))