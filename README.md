# Dry Tap Bottler

This is a raspberry pi webserver that works with the Dry Tap Bottling System.  
It is still a WIP, and is currently able to toggle several LEDs

Here's the basic breakdown of how this works:
  
[there will be a diagram here]
  
## Setup / Config
Run config/install.sh to install mod_python, and configure the apache2.conf file.
Everything should work there, but if it doesn't, it shouldn't be hard to manually
follow the install.sh file as a guide.
  
As for config, you'll need to edit index.html, and data/states.db.
In the html file you can set the name of buttons, as well as which pin it'll control/report.

data/states.db contains the automatic steps. when a delay of -1 is reached,
the system will stop and wait for user input to continue. Note that that step will still
need to set the state of at least one pin, or it won't run properly.

## Todo:
- Implement auto mode pauses
- Populate the states.db
- Assign pins to outputs


I have created the Daemon using Sander Marechal's sample found [here](http://web.archive.org/web/20131017130434/http://www.jejik.com/articles/2007/02/a_simple_unix_linux_daemon_in_python/).
