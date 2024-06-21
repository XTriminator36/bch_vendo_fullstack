from Main.models import *
import logging
import paho.mqtt.client as mqtt
import json
import time
from django.utils import timezone
from django.core.management.base import BaseCommand
from decouple import config
import ssl

LOGGER = logging.getLogger(__name__)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("transactions/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # index = CashAddress.objects.all().last().id
    # address = CashAddress.objects.all().last().cash_address

    # Get wallet address from database
    # Used to compare from the MQTT listenertransactions 
    address = CashAddress.objects.last().cash_address

    # Get updated value of channel from database 
    # Used for debug purposes
    # channel = CashAddress.objects.all().last().channel
    # channel = ProductItem.objects.all().last().product_code #prints product code as a channel
    # print("Channel: ", channel)

    # Get updated amount from database
    # Used to save along with transaction hash
    amount = 0

    data = json.loads(msg.payload)
    print("Data: ", data)
    print("Cash Address from data: ", data["recipient"])
    print("Cash Address from database: ", address)

    tx_hash = data["txid"]

    if data["token"] == "bch" and data["recipient"] == address:
        value = data["value"]
        decimals = data["decimals"]
        amount = value / (10 ** decimals)
        
        print(f"{tx_hash} | {amount:.7f} BCH ")

        # Save BCH value and transaction hash to database
        # b = ProductTransactions(bch_value=amount, tx_hash=tx_hash)
        # b.save()
        recent_tx = ProductTransactions.objects.latest('id')
        recent_tx.tx_hash = tx_hash
        recent_tx.total_paid = amount
        recent_tx.paid_timestamp = timezone.now()
        recent_tx.is_paid = True
        recent_tx.save()
        print(f"Updated txid for product {recent_tx.product_code}: {tx_hash}")
        

FIRST_RECONNECT_DELAY = 1
RECONNECT_RATE = 2
MAX_RECONNECT_COUNT = 12
MAX_RECONNECT_DELAY = 60

def on_disconnect(client, userdata, rc):
    print(f"Disconnected with result code: {rc}")
    reconnect_count, reconnect_delay = 0, FIRST_RECONNECT_DELAY
    while reconnect_count < MAX_RECONNECT_COUNT:
        print(f"Reconnecting in {reconnect_delay} seconds...")
        time.sleep(reconnect_delay)

        try:
            client.reconnect()
            print("Reconnected successfully!")
            return
        except Exception as err:
            print(f"{err}. Reconnect failed. Retrying...")

        reconnect_delay *= RECONNECT_RATE
        reconnect_delay = min(reconnect_delay, MAX_RECONNECT_DELAY)
        reconnect_count += 1
    print(f"Reconnect failed after {reconnect_count} attempts. Exiting...")

_timestamp = str(int(time.time()))

# Suppress SSL warnings
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

client = mqtt.Client(transport='websockets', client_id="vending-machine-3-" + _timestamp, clean_session=False)
client.tls_set_context(ssl_context)
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

mqtt_broker_url = 'mqtt.watchtower.cash'
client.connect(mqtt_broker_url, 443, 60)

class Command(BaseCommand):
    help = 'Run the transaction listener'
    
    def handle(self, *args, **options):
        client.loop_forever() 
