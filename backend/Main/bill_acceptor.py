import RPi.GPIO as GPIO

#definitions
pulse_input = 6
bill_acceptor = 5

#GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(pulse_input, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(bill_acceptor, GPIO.OUT)

pulse_count = 0 #count holder

GPIO.output(bill_acceptor, False)

#will count the bill inputs
def counter(channel):
    global pulse_count
    if GPIO.input(channel) > 0.5:
        pulse_count += 1
        print(pulse_count)
    else:
        pulse_count += 0

    #print pulses
    print("Pulse Count: ", pulse_count)

#detect events
GPIO.add_event_detect(pulse_input, GPIO.RISING, callback=counter, bouncetime=4)