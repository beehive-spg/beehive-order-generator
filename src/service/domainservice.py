import random, sys
from data import rest
from domain.customer import Customer
from domain.buildinghive import BuildingHive
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

def get_all_hives():
    all_hives = rest.get_all_hives_json()
    hives = []
    for hive in all_hives:
        hivedomain = get_hivedomain(hive)
        hives.append(hivedomain)
    return hives

def get_hivedomain(json):
    hive = BuildingHive(json)
    hive.validate()
    return hive

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