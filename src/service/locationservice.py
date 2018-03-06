import sys
from geopy.distance import vincenty
from data import rest
from service import domainservice

MAXDISTANCE = ( (rest.get_drone_types_json()[0]['dronetype/range'] / 1000) / 2) *0.92

def is_reachable(lon, lat):
    all_hives = domainservice.get_all_hives()
    for hive in all_hives:
        if (is_in_range((lon, lat), (hive.xcoord, hive.ycoord), MAXDISTANCE)):
            return True
    return False

def is_in_range(a, b, maxdistance):
    return get_distance(a, b) < maxdistance

def get_distance(a, b):
    return vincenty(a, b).km

def get_upper_x(all_hives):
    x = -1
    for hive in all_hives:
        if (x < hive.xcoord):
            x = hive.xcoord
    return x

def get_upper_y(all_hives):
    y = -1
    for hive in all_hives:
        if (y < hive.ycoord):
            y = hive.ycoord
    return y

def get_lower_x(all_hives):
    x = sys.maxsize
    for hive in all_hives:
        if (x > hive.xcoord):
            x = hive.xcoord
    return x

def get_lower_y(all_hives):
    y = sys.maxsize
    for hive in all_hives:
        if (y > hive.ycoord):
            y = hive.ycoord
    return y