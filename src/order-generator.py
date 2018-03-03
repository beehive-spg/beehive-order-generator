#!/usr/bin/env python3
import sys, logging, time
from data import generator, writer

logging.basicConfig(stream=sys.stdout, level=logging.INFO,
    format='%(asctime)s - %(name)-5s- %(levelname)-5s- %(message)s')

'''
    python3 order_generator.py generate #number
    python3 order_generator.py send #number pause
    python3 order_generator.py generate #number normalized/...
'''

def main():
    command = sys.argv[1]
    amount = int(sys.argv[2])
    if (command == 'generate'):
        logging.info("Starting to generate " + str(amount) +" orders...")
        generator.generate_orders(amount)
    elif (command == 'send'):
        logging.info("Sending" + str(amount) + " orders...")
        writer.send_orders_from_file(amount)
    elif (command == 'sendsaved'):
        logging.info("Sending" + str(amount) + " orders based on saved locations...")
        writer.send_locations_from_file(amount)

if __name__ == '__main__':
    main()