import sys, os, logging, requests, random
from faker import Faker
import service
from data import rest, writer

logging.basicConfig(stream=sys.stdout, level=logging.INFO,
    format='%(asctime)s - %(name)-5s- %(levelname)-5s- %(message)s')

def generate_orders(amount):
    writer.write_orders_to_file(get_orders(amount, get_locations(amount)))

def generate_locations(amount):
    writer.write_locations_to_file(get_locations(amount))

def get_orders(amount, locations):
    names = get_random_names(amount)

    orders = []
    for i in range(0, amount):
        print(locations[0][i])
        print(locations[1][i])
        print(locations[2][i])
        customer = service.get_customerdomain_by_attributes(names[i], locations[0][i], locations[1][i], locations[2][i])
        customer = service.get_customerdomain(rest.post_customer(customer))
        _to = customer.customer[0].id
        _from = get_shop()

        order = []
        order.append(_from)
        order.append(_to)
        orders.append(order)
        logging.info("Created order from: " + str(_to) + " to: " + str(_from))
    return orders

def get_random_names(amount):
    fake = Faker()
    names = []
    for i in range(0, amount):
        name = fake.name()
        names.append(name)
    return names

def get_locations(amount):
    all_buildings = service.get_all_buildings()
    upper_x = service.get_upper_x(all_buildings)
    upper_y = service.get_upper_y(all_buildings)
    lower_x = service.get_lower_x(all_buildings)
    lower_y = service.get_lower_y(all_buildings)

    addresses = []
    xcoords = []
    ycoords = []
    for i in range(0, amount):
        lon = random.uniform(lower_x, upper_x)
        lat = random.uniform(lower_y, upper_y)

        address = rest.get_address(lon, lat)

        addresses.append(address)
        xcoords.append(lon)
        ycoords.append(lat)

    locations = []
    locations.append(addresses)
    locations.append(xcoords)
    locations.append(ycoords)

    logging.info("Saving generated locations to file.")
    writer.write_locations_to_file(locations)

    return locations

def get_shop():
    shops = service.get_all_shops()
    random_shop = random.randint(0, len(shops)-1)
    chosen_shop = shops[random_shop]
    return chosen_shop.shop[0].id