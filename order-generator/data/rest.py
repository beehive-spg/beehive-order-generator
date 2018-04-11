import os, requests, json
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

apiKey = os.getenv("GOOGLE_API_KEY")

def get_address(lon, lat):
	address_response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?latlng=" + str(lat) + ","+ str(lon) +"&key=" + apiKey)
	return address_response.json()['results'][0]['formatted_address']

def get_all_hives_json():
    hives = requests.get(url("/hives"))
    return hives.json()

def get_all_shops_json():
    shops = requests.get(url("/shops"))
    return shops.json()

def get_drone_types_json():
    types = requests.get(url("/types"))
    return types.json()

def post_give_drones(amount):
    response =requests.post(url("/api/givedrones/{}".format(amount)))
    return response.status_code

def post_customer(customer):
    postcustomer = dict()
    postcustomer['name'] = customer.customer[0].name
    postcustomer['address'] = customer.address
    postcustomer['xcoord'] = customer.xcoord
    postcustomer['ycoord'] = customer.ycoord
    print("trying to create customer: " + str(postcustomer))
    try:
        customer_response = requests.post(url("/customers"), data=json.dumps(postcustomer), headers = {'content-type': 'application/json'})
    except:
        print("could add")
    return customer_response.json()

def url(route):
    host = os.getenv('DATABASE_URL')
    return host + route