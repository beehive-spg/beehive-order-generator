import random, sys
from data import rest
from domain.building import Building
from domain.customer import Customer
from domain.buildingshop import BuildingShop
from domain.buildingcustomer import BuildingCustomer

def get_customerdomain_by_attributes(name, address, xcoord, ycoord):
    customer = BuildingCustomer()
    c = Customer()
    c.name = name
    customer.customer = [ c ]
    customer.address = address
    customer.xcoord = xcoord
    customer.ycoord = ycoord
    return customer

def get_customerdomain(json):
    customer = BuildingCustomer(json)
    customer.validate()
    return customer

def get_all_buildings():
    all_buildings = rest.get_all_buildings_json()
    buildings = []
    for building in all_buildings:
        buildingdomain = get_buildingdomain(building)
        buildings.append(buildingdomain)
    return buildings

def get_buildingdomain(json):
    building = Building(json)
    building.validate()
    return building

def get_all_shops():
    all_shops = rest.get_all_shops_json()
    shops = []
    for shop in all_shops:
        shopdomain = get_shopdomain(shop)
        shops.append(shopdomain)
    return shops

def get_shopdomain(json):
    shop = BuildingShop(json)
    shop.validate()
    return shop

def get_upper_x(all_buildings):
    x = -1
    for building in all_buildings:
        if (x < building.xcoord):
            x = building.xcoord
    return x

def get_upper_y(all_buildings):
    y = -1
    for building in all_buildings:
        if (y < building.ycoord):
            y = building.ycoord
    return y

def get_lower_x(all_buildings):
    x = sys.maxsize
    for building in all_buildings:
        if (x > building.xcoord):
            x = building.xcoord
    return x

def get_lower_y(all_buildings):
    y = sys.maxsize
    for building in all_buildings:
        if (y > building.ycoord):
            y = building.ycoord
    return y