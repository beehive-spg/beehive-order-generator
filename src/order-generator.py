#!/usr/bin/env python3
import sys, logging, time
from data import generator, operator
from data import rest

logging.basicConfig(stream=sys.stdout, level=logging.INFO,
    format='%(asctime)s - %(levelname)-5s - %(message)s')

'''
python3 order_generator.py generate #amount
python3 order_generator.py send #amount #drones_per_hive #timeout
'''
def main():
    command = sys.argv[1]
    amount = int(sys.argv[2])
    drones_per_hive = int(sys.argv[3])
    logging.info(command)
    logging.info(amount)
    logging.info(drones_per_hive)
    try:
        time.sleep(int(sys.argv[4]))
    except:
        logging.info("Starting without a timeout")
    if (command == 'generate'):
        logging.info("Starting to generate " + str(amount) +" orders...")
        generator.generate_orders(amount)
    elif (command == 'send'):
        while (True):
            status = rest.post_give_drones(drones_per_hive)
            logging.info(status)
            if(status == 204):
                break
            time.sleep(5)
        logging.info("Sending " + str(amount) + " orders from file...")
        while (True):
            operator.send_orders_from_file(amount)

if __name__ == '__main__':
    main()