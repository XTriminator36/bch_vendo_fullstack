from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BchValue, CashAddress
import time
import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit


print("Starting django signal...")

# Pin Definitons:
sensorPins = [14, 15, 18, 23, 24, 25, 8, 7, 1, 12, 16, 20, 21, 26, 19, 13]

# Pin Setup:
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensorPins, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setwarnings(True)

# Set channels to the number of servo channels
kit = ServoKit(channels=16)

def delay(seconds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator

channel_pins = dict(zip(range(16), sensorPins))

@receiver(post_save, sender=BchValue)
@delay(3)
def trigger_gpio(sender, instance, created, **kwargs):
    channel = CashAddress.objects.all().last().channel
    kit.continuous_servo[channel].throttle = -1
    time.sleep(0.75)

    print("Triggering servo motor on channel:", channel)

    while True:
        if GPIO.input(channel_pins[channel]):
            kit.continuous_servo[channel].throttle = -1
        else:
            kit.continuous_servo[channel].throttle = 0
            break


