import asyncio
import aio_pika
import os, sys
import logging
import json
from data import operator

logging.basicConfig(stream=sys.stdout, level=logging.INFO,
    format='%(asctime)s - %(levelname)-5s - %(message)s')

def start_settings_queue(drones_per_minute, sending_connection):
    logging.info("started consumer")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(settings_queue(drones_per_minute, sending_connection, loop))
    loop.close()

async def settings_queue(drones_per_minute, sending_connection, loop):
    connection = await aio_pika.connect_robust(os.getenv('RABBITMQ_URL'), loop=loop)

    queue_name = os.getenv('SETTINGS_QUEUE')

    channel = await connection.channel()

    queue = await channel.declare_queue(queue_name, durable=True)

    async for message in queue:
        with message.process():
            try:
                decoded_message = message.body.decode("utf-8")
                loaded_message = json.loads(decoded_message)
                logging.info("Received message: " + str(loaded_message))
                setting = loaded_message['setting']
                if(setting == "drones"):
                    drones_per_minute = int(loaded_message['value'])
                    logging.info(drones_per_minute)
                    sending_connection.send(drones_per_minute)
            except Exception as e:
                logging.warning(e)

            if queue.name in message.body.decode():
                break