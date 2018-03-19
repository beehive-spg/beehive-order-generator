import sys, logging, json, time, random
from data import generator, rest
from rabbitmq import publisher
from service import domainservice

logging.basicConfig(stream=sys.stdout, level=logging.INFO,
    format='%(asctime)s - %(levelname)-5s - %(message)s')

ORDERFILE = "generated_orders.txt"

def write_orders_to_file(orders):
    try:
        with open(ORDERFILE, 'r') as file:
            if (len(file.read()) == 0):
                write_orders(orders)
            else:
                append_orders(orders)
    except FileNotFoundError:
        open(ORDERFILE, 'w')
        write_orders_to_file(orders)

def write_orders(orders):
    with open(ORDERFILE, 'w') as file:
        file.write(
            'address\t' +
            'xcoord\t' +
            'ycoord\t' +
            'shopid\n'
        )

        CONTENT = ""
        for o in orders:
            CONTENT += '{0}\t{1}\t{2}\t{3}\n'.format(
                o['to'].address,
                o['to'].xcoord,
                o['to'].ycoord,
                o['from'].shop[0].id
            )
        file.write(CONTENT)
    logging.info("Created file " + ORDERFILE + " with " + str(len(orders)) + " orders.")

def append_orders(orders):
    with open(ORDERFILE, 'a') as file:
        CONTENT = ""
        for o in orders:
            CONTENT += '{0}\t{1}\t{2}\t{3}\n'.format(
                o['to'].address,
                o['to'].xcoord,
                o['to'].ycoord,
                o['from'].shop[0].id
            )
        file.write(CONTENT)
    logging.info("Appended to file " + ORDERFILE + " " + str(len(orders)) + " new orders.")

def send_orders_from_file(amount):
    with open(ORDERFILE, 'r') as file:
        for iteration, line in enumerate(file):
            if (iteration-1 == amount):
                    break
            if (iteration != 0):
                l = line.split("\t")
                l[3] = l[3].strip("\n")
                logging.info("file content:")
                logging.info(str(l))
                customer = domainservice.get_customerdomain_by_attributes(generator.get_random_names(1)[0], l[0], float(l[1]), float(l[2]))
                create_customer(customer, l)
                time.sleep(random.randint(4, 8))
            else:
                publisher.setup()
            if (iteration%30 == 0 and iteration > 0):
                time.sleep(30)
    file.close()

def create_customer(customer, l):
    try:
        new_customer = domainservice.get_customerdomain(rest.post_customer(customer))
        logging.info("customer")
        logging.info(new_customer)

        order = dict()
        order['from'] = str(l[3])
        logging.info("New Customer: " + str(new_customer.to_primitive()))
        order['to'] = str(new_customer.customer[0].id)
        print(json.dumps(order))
        publisher.send_message(json.dumps(order))
    except Exception as e:
        logging.info(e)
        logging.info("post crashed")
        logging.info("tried to send customer: ")
        logging.info(customer.to_primitive())