import sys, logging, json, time
from data import generator
from rabbitmq import publisher

logging.basicConfig(stream=sys.stdout, level=logging.INFO,
    format='%(asctime)s - %(name)-5s- %(levelname)-5s- %(message)s')

ORDERFILE = "generated_orders.txt"
LOCATIONFILE = "generated_locations.txt"

def write_orders_to_file(orders):
    try:
        with open(ORDERFILE, 'r') as file:
            if (len(file.read()) == 0):
                write_orders(orders)
            else:
                append_orders(orders)
    except FileNotFoundError:
    	write_locations(locations)

def write_locations_to_file(locations):
    try:
        with open(LOCATIONFILE, 'r') as file:
            if (len(file.read()) == 0):
                write_locations(locations)
            else:
                append_locations(locations)
    except FileNotFoundError:
        write_locations(locations)

def write_orders(orders):
    with open(ORDERFILE, 'w') as file:
        file.write(
            'FROM\t' +
            'TO\n'
        )

        CONTENT = ""
        for o in orders:
            CONTENT += '{0}\t{1}\n'.format(
                o[0],
                o[1]
            )
        file.write(CONTENT)
    logging.info("Created file " + ORDERFILE + " with " + str(len(orders)) + " orders.")

def append_orders(orders):
    with open(ORDERFILE, 'a') as file:
        CONTENT = ""
        for o in orders:
            CONTENT += '{0}\t{1}\n'.format(
                o[0],
                o[1]
            )
        file.write(CONTENT)
    logging.info("Appended to file " + ORDERFILE + " " + str(len(orders)) + " new orders.")

def write_locations(locations):
    with open(LOCATIONFILE, 'w') as file:
        file.write(
        	'address\t' +
            'xcoord\t' +
            'ycoord\n'
        )
        CONTENT = ""
        for i in range(0, len(locations[1])):
            CONTENT += '{0}\t{1}\t{2}\n'.format(
                locations[0][i],
                locations[1][i],
                locations[2][i]
            )
        file.write(CONTENT)
    logging.info("Created file " + LOCATIONFILE + " with " + str(len(locations[1])) + " locations.")

def append_locations(locations):
    with open(LOCATIONFILE, 'a') as file:
        CONTENT = ""
        for i in range(0, len(locations[1])):
            CONTENT += '{0}\t{1}\t{2}\n'.format(
            	locations[0][i],
                locations[1][i],
                locations[2][i]
            )
        file.write(CONTENT)
    logging.info("Appended to file " + LOCATIONFILE + " " + str(len(locations[1])) + " new locations.")

def send_orders_from_file(amount):
    with open(ORDERFILE, 'r') as file:
        for iteration, line in enumerate(file):
            if (iteration != 0):
                l = line.split("\t")
                l[1] = l[1].strip("\n")
                order = dict()
                order['from'] = l[0]
                order['to'] = l[1]
                publisher.send(json.dumps(order))
                time.sleep(5)
                if (iteration == amount):
                    break
    file.close()

def send_locations_from_file(amount):
    locations = get_locations_from_file()
    orders = generator.get_orders(len(locations[1]), locations)
    for order in orders:
        orders = dict()
        orders['from'] = order[0]
        orders['to'] = order[1]
        publisher.send(json.dumps(orders))
        time.sleep(10)

def get_locations_from_file():
    with open(LOCATIONFILE, 'r') as file:
        locations = []
        addresses = []
        xcoords = []
        ycoords = []
        for iteration, line in enumerate(file):
            if (iteration != 0):
                l = line.split("\t")
                l[2] = l[2].strip("\n")
                addresses.append(l[0])
                xcoords.append(float(l[1]))
                ycoords.append(float(l[2]))
        locations.append(addresses)
        locations.append(xcoords)
        locations.append(ycoords)
    return locations