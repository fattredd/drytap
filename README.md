# Dry Tap Bottler

This is a raspberry pi webserver that works with the Dry Tap Bottling System.  
It is still a WIP, and is currently able to toggle several LEDs

Here's the basic breakdown of how this works:
  
[there will be a diagram here]
  
## Config
You should only need to edit index.html. There you can set the name of buttons
as well as which pin it'll control/report.

## Todo:
- Create an auto mode
 - Steps through a certain sequence
 - Stops afterwards

I have created the Daemon using Sander Marechal's sample found [here](http://web.archive.org/web/20131017130434/http://www.jejik.com/articles/2007/02/a_simple_unix_linux_daemon_in_python/).
