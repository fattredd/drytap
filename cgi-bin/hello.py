#!/usr/bin/env python

from mod_python import apache
import RPi.GPIO as gpio

def js(req):
    import time
    req.content_type = "text/plain"
    req.send_http_header()
    return("thisTime = %s;" % time.time())

def swapPIN(req, q=0, t=0):
    q = int(q) # Pin number
    t = int(t) # Toggle Boolean
    pins = [q]
    gpio.setmode(gpio.BOARD)
    gpio.setup(pins, gpio.OUT)
    if t == 1:
        gpio.output(q, not bool(gpio.input(q)))
    req.content_type = "text/javascript"
    req.send_http_header()
    return '{"currentStatus":%s}' % str(gpio.input(q))

def Auto(req, t):
    t = int(t)
    w = 'r'
    with open('/var/www/autoMode.db',w) as f:
        status = bool(f.read())
    if t:
        with open('/var/www/autoMode.db','w') as f:
            status = not status
            f.write(str(int(status)))
    req.content_type = "text/javascript"
    req.send_http_header()
    return '{"currentStatus":%s}' % str(int(status))

    
