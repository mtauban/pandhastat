import piVirtualWire.piVirtualWire as piVirtualWire
import time
import pigpio



def rfSend(msg):
    pi = pigpio.pi()
    tx = piVirtualWire.tx(pi, 17, 1200) # Set pigpio instance, TX module GPIO pin and baud rate
    for i in range(0,10):
        tx.put(msg)
        tx.waitForReady()
        time.sleep(0.05) # allows for better transmission ...
    
    tx.cancel()
    pi.stop()
