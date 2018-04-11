#!/usr/bin/env python3
import sys, logging, time
from multiprocessing import Process, Pipe
from data import generator
from data import rest
from data import operator
from rabbitmq import consumer
from requests.exceptions import ConnectionError

logging.basicConfig(stream=sys.stdout, level=logging.INFO,
    format='%(asctime)s - %(levelname)-5s - %(message)s')

'''
python3 order_generator.py generate #amount
python3 order_generator.py send #drones_per_hive #timeout
'''
def main():
    command = sys.argv[1]
    #amount = int(sys.argv[2])
    drones_per_hive = int(sys.argv[2])
    try:
        time.sleep(int(sys.argv[3]))
    except:
        logging.info("Starting without a timeout")
    if (command == 'generate'):
        amount = int(sys.argv[2])
        logging.info("Starting to generate " + str(amount) +" orders...")
        generator.generate_orders(amount)
    elif (command == 'send'):
        while (True):
            try:
                status = rest.post_give_drones(drones_per_hive)
                if(status == 204):
                    break
                    time.sleep(5)
            except ConnectionError:
                logging.critical("Connection not available...")
                time.sleep(5)
        #logging.info("Sending " + str(amount) + " orders from file...")
        logging.info("Sending orders from file...")

        drones_per_minute = 0
        parent_conn, child_conn = Pipe()
        p1 = Process(target=consumer.start_settings_queue, args=(drones_per_minute, child_conn))
        p2 = Process(target=operator.send_orders_from_file, args=(drones_per_minute, parent_conn))
        p1.start()
        p2.start()
        #while (True):
            #operator.send_orders_from_file(amount)


if __name__ == '__main__':
    main()