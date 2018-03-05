import os, requests, json
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

apiKeyMichi = "AIzaSyB_Ld9ROBJON_kx9QoW8tCyoUVDpFPuWwI"
apiKey = "AIzaSyCseWsBGzArQUI2a6EPtywN8QKaAtjHDPo"

def get_address(lon, lat):
	address_response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?latlng=" + str(lat) + ","+ str(lon) +"&key=" + apiKey)
	return address_response.json()['results'][0]['formatted_address']

def get_all_buildings_json():
    hives = requests.get(url("/hives"))
    return hives.json()

def get_all_shops_json():
    shops = requests.get(url("/shops"))
    return shops.json()

def post_customer(customer):
    postcustomer = dict()
    postcustomer['name'] = customer.customer[0].name
    postcustomer['address'] = customer.address
    postcustomer['xcoord'] = customer.xcoord
    postcustomer['ycoord'] = customer.ycoord
    customer_response = requests.post(url("/customers"), data=json.dumps(postcustomer), headers = {'content-type': 'application/json'})
    return customer_response.json()

def url(route):
    host = os.getenv('DBURL')
    return host + route