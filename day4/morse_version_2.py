#!/usr/bin/python

from morseParity import MorseParity
from transmitter import Transmitter
from time import sleep


def send_dot():
        print "Dot"
    
def send_dash():
        print "Dash"
    
def send_character(val):
    encoded = codec.encode(val)
    for c in encoded:
        if c == ".":
            tx.send_dot()
        elif c == "-":
            tx.send_dash()
    sleep(3.5)

if __name__=='__main__':
# read a character
# convert it to morse
# For each chacter in the string, call dot or dash appropriately
    codec = MorseParity()
    tx = Transmitter()
    toSend = raw_input("Send :")
    for c in toSend:
		if c == " ":
			sleep(8)
		else:
			send_character(c)
