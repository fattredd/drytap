#!/usr/bin/env python

import sys, time
from daemon import Daemon
import sqlite3 as sql
import RPi.GPIO as gpio
import logging
from logging.handlers import RotatingFileHandler

class AutoTap(Daemon):
        def stop(self):
                daemonActivePin = 8
                gpio.setwarnings(False)
                gpio.setmode(gpio.BOARD)
                gpio.setup(daemonActivePin , gpio.OUT)
                gpio.output(daemonActivePin, gpio.LOW)
                super(AutoTap, self).stop()
        
	def run(self):
                daemonActivePin = 8
                
                log_formatter = logging.Formatter('%(message)s')
                logFile = '/tmp/auto.log'
                handler = RotatingFileHandler(logFile, mode='a', maxBytes=5*1024*1024,
                                              backupCount=1, encoding=None, delay=0)
                handler.setFormatter(log_formatter)
                log = logging.getLogger('root')
                log.addHandler(handler)

                gpio.setwarnings(False)
                gpio.setmode(gpio.BOARD)
                gpio.setup(daemonActivePin , gpio.OUT)
                gpio.output(daemonActivePin, gpio.HIGH)
                
                while True:
                        with sql.connect('/var/www/data/autoOn.db') as con:
                                cur = con.cursor()
                                try:
                                        cur.execute("SELECT state FROM Auto")
                                except:
                                        cur.execute("create table Auto(state INT)")
                                        cur.execute("INSERT INTO Auto VALUES(0)")
                                        cur.execute("SELECT state FROM Auto")
                                running = bool(cur.fetchone()[0])
                        if running:
                                # Step Through the code
                                pins = None
                                delay = None
                                totalStates = None
                                with sql.connect('/var/www/data/states.db') as con:
                                        cur = con.cursor()
                                        cur.execute("SELECT current FROM Step")
                                        current = cur.fetchone()[0]
                                        cur.execute("SELECT pin, state FROM Proc WHERE step == '%s'" % current)
                                        pinstate = cur.fetchall()
                                        pins = [i[0] for i in pinstate]
                                        states = [i[1] for i in pinstate]
                                        cur.execute("SELECT delay FROM Time WHERE step == %s" % current)
                                        delay = cur.fetchone()[0]
                                        cur.execute("SELECT Count(*) FROM Time")
                                        totalStates = cur.fetchone()[0]
                                        nextState = (current+1)%totalStates
                                        cur.execute("UPDATE Step SET current = %s" % nextState)
                                if delay == -1:
                                        running = false
                                else:
                                        gpio.setup(pins, gpio.OUT)
                                        log.info("Now in state %s.\n" % current)
                                        for pin, state in pinstate:
                                                gpio.output(pin, state)
                                                log.info("\t%s | %s\n" % (pin,state))
                                                time.sleep(delay / 1000.0)
                                                log.info("  Delay for %s ms\n" % delay)
                        else:
                                # Do nothing
                                time.sleep(0.5)

        
if __name__ == "__main__":
	daemon = AutoTap('/tmp/AutoTap.pid',stderr='/tmp/autoErr.log')
	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			daemon.start()
		elif 'stop' == sys.argv[1]:
			daemon.stop()
  		elif 'restart' == sys.argv[1]:
			daemon.restart()
                elif 'status' == sys.argv[1]:
                        daemon.report()
		else:
			print "Unknown command"
			sys.exit(2)
		sys.exit(0)
	else:
		print "usage: %s start|stop|restart" % sys.argv[0]
		sys.exit(2)
