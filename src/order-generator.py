#!/usr/bin/env python3
import sys, logging, time
from data import generator, operator

logging.basicConfig(stream=sys.stdout, level=logging.INFO,
    format='%(asctime)s - %(levelname)-5s - %(message)s')

'''
python3 order_generator.py generate #number
python3 order_generator.py send #number
'''
def main():
    command = sys.argv[1]
    amount = int(sys.argv[2])
    try:
        time.sleep(int(sys.argv[3]))
    except:
        logging.info("Starting without a timeout")
    if (command == 'generate'):
        logging.info("Starting to generate " + str(amount) +" orders...")
        generator.generate_orders(amount)
    elif (command == 'send'):
        logging.info("Sending " + str(amount) + " orders from file...")
        while (True):
            operator.send_orders_from_file(amount)

if __name__ == '__main__':
    main()