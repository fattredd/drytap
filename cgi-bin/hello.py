#!/usr/bin/env python

from mod_python import apache
import RPi.GPIO as gpio
import sqlite3 as sql

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
    comm = ""
    state = None
    con = sql.connect('/var/www/data/autoOn.db')
    with con:
        cur = con.cursor()
        cur.execute("SELECT state FROM Auto")
        state = cur.fetchone()[0]
        if (t == 1):
            state = int(not bool(state))
            comm += "State is now "+str(state)
            cur.execute("UPDATE Auto SET state = %d" % state)
        con.commit()
    req.content_type = "text/javascript"
    req.send_http_header()
    return '{"currentStatus":%d,"Comment":"%s"}' % (state,comm)

def Continue(req, t):
    t = int(t)
    comm = ""
    state = None
    con = sql.connect('/var/www/data/autoOn.db')
    with con:
        cur = con.cursor()
        cur.execute("SELECT current FROM paused")    
        state = cur.fetchone()[0]
        if (t == 1 && state == 1):
            state = 0
            comm += "State is now "+str(state)
            cur.execute("UPDATE paused SET current = %d" % state)
        con.commit()
    req.content_type = "text/javascript"
    req.send_http_header()
    return '{"currentStatus":%d,"Comment":"%s"}' % (state,comm)
