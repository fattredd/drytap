#!/usr/bin/env python

from mod_python import apache
import RPi.GPIO as gpio

def say(req, q="NOTHING"):
    req.content_type = "text/html"
    req.send_http_header()
    return "<h1>How do things like %s</h1>" % q

def js(req):
    import time
    req.content_type = "text/plain"
    req.send_http_header()
    return("thisTime = %s;" % time.time())

def swapLED(req):
    pins = [11, 12]
    gpio.setmode(gpio.BOARD)
    gpio.setup(pins, gpio.OUT)
    gpio.output(11, not bool(gpio.input(11)))
    req.content_type = "text/javascript"
    req.send_http_header()
    return '{"currentStatus":%s}' % str(gpio.input(11))
