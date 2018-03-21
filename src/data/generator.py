import sys, os, logging, requests, random
from faker import Faker
from service import domainservice, locationservice
from data import rest, operator

logging.basicConfig(stream=sys.stdout, level=logging.INFO,
    format='%(asctime)s - %(levelname)-5s - %(message)s')

def generate_orders(amount):
    operator.write_orders_to_file(get_orders(amount, get_locations(amount)))

def generate_locations(amount):
    operator.write_locations_to_file(get_locations(amount))

def get_orders(amount, locations):
    names = get_random_names(amount)

    orders = []
    for i in range(0, amount):
        customer = domainservice.get_customerdomain_by_attributes(names[i], locations[0][i], locations[1][i], locations[2][i])
        customer = domainservice.get_customerdomain(rest.post_customer(customer))
        _to = customer
        _from = get_shop()

        order = dict()
        order['from'] = _from
        order['to'] = _to
        orders.append(order)
        logging.info("Created order from: " + str(_to.id) + " to: " + str(_from.shop[0].id))
    return orders

def get_random_names(amount):
    fake = Faker()
    names = []
    for i in range(0, amount):
        name = fake.name()
        names.append(name)
    return names

def get_locations(amount):
    all_hives = domainservice.get_all_hives()
    upper_x = locationservice.get_upper_x(all_hives)
    upper_y = locationservice.get_upper_y(all_hives)
    lower_x = locationservice.get_lower_x(all_hives)
    lower_y = locationservice.get_lower_y(all_hives)

    addresses = []
    xcoords = []
    ycoords = []
    for i in range(0, amount):
        lon = random.uniform(lower_x, upper_x)
        lat = random.uniform(lower_y, upper_y)
        while (not locationservice.is_reachable(lon, lat)):
            logging.info("Regenerate out of range location")
            lon = random.uniform(lower_x, upper_x)
            lat = random.uniform(lower_y, upper_y)

        logging.info("Generated location")

        address = rest.get_address(lon, lat)

        addresses.append(address)
        xcoords.append(lon)
        ycoords.append(lat)

    locations = []
    locations.append(addresses)
    locations.append(xcoords)
    locations.append(ycoords)

    return locations

def get_shop():
    shops = domainservice.get_all_shops()
    random_shop = random.randint(0, len(shops)-1)
    chosen_shop = shops[random_shop]
    logging.info("Generate shop")
    while (not locationservice.is_reachable(chosen_shop.xcoord, chosen_shop.ycoord)):
            logging.info("Regenerate out of range shop")
            random_shop = random.randint(0, len(shops)-1)
            chosen_shop = shops[random_shop]
    return chosen_shop