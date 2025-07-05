# pylint: disable=unused-import

import time
from RFM69 import Radio, FREQ_315MHZ, FREQ_433MHZ, FREQ_868MHZ, FREQ_915MHZ

node_id = 1
network_id = 100
recipient_id = 2

# The following are for an Adafruit RFM69HCW Transceiver Radio
# Bonnet https://www.adafruit.com/product/4072
# You should adjust them to whatever matches your radio
board = {'isHighPower': True, 'interruptPin': 15, 'resetPin': 22, 'spiDevice': 1}

# The following are for an RaspyRFM RFM69CW Module #1
# http://www.seegel-systeme.de/2015/09/02/ein-funkmodul-fuer-den-raspberry-raspyrfm/
# board = {'isHighPower': False, 'interruptPin': 22, 'resetPin': None, 'spiDevice': 0}

# The following are for an RaspyRFM RFM69CW Module #2
# http://www.seegel-systeme.de/2015/09/02/ein-funkmodul-fuer-den-raspberry-raspyrfm/
# board = {'isHighPower': False, 'interruptPin': 18, 'resetPin': None, 'spiDevice': 1}

with Radio(FREQ_915MHZ, node_id, network_id, verbose=False, **board) as radio:
    print ("Starting loop...")

    while True:
        startTime = time.time()
        # Get packets for at most 5 seconds
        while time.time() - startTime < 5:
            # We end at (startTime+5), so we have (startTime+5 - time.time())
            # seconds left
            timeRemaining = max(0, startTime + 5 - time.time())

            # This call will block until a packet is received,
            # or timeout in however much time we have left
            packet = radio.get_packet(timeout = timeRemaining)

            # If radio.get_packet times out, it will return None
            if packet is not None:
                # Process packet
                print (packet)

        # After 5 seconds send a message
        print ("Sending")
        if radio.send(recipient_id, "TEST", attempts=3, waitTime=100):
            print ("Acknowledgement received")
        else:
            print ("No Acknowledgement")
