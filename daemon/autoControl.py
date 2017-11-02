#!/usr/bin/env python

import sys, time
from daemon import Daemon
import sqlite3 as sql
import RPi.GPIO as gpio

class AutoTap(Daemon):
	def run(self):
                while True:
                        state = None
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
                                        pins = cur.fetchall()
                                        cur.execute("SELECT delay FROM Time WHERE step == %s" % current)
                                        delay = cur.fetchone()[0]
                                        cur.execute("SELECT Count(*) FROM Time")
                                        totalStates = cur.fetchone()[0]
                                        nextState = (current+1)%totalStates
                                        cur.execute("UPDATE Step SET current = %s" % nextState)
                                gpio.setmode(gpio.BOARD)
                                import sys
                                sys.stderr.write("Pins:")
                                sys.stderr.write(type(pins))
                                gpio.setup(pins, gpio.OUT)
                                for pin, state in pins:
                                        #gpio.output(pin, state)
                                        pass
                                time.delay(delay)
                                
                        else:
                                # Do nothing
                                time.sleep(500)
                        

                
if __name__ == "__main__":
	daemon = AutoTap('/tmp/AutoTap.pid',stderr='/tmp/AutoTap.log')
	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			daemon.start()
		elif 'stop' == sys.argv[1]:
			daemon.stop()
		elif 'restart' == sys.argv[1]:
			daemon.restart()
		else:
			print "Unknown command"
			sys.exit(2)
		sys.exit(0)
	else:
		print "usage: %s start|stop|restart" % sys.argv[0]
		sys.exit(2)
