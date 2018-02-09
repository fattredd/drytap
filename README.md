# Dry Tap Bottler

This is a raspberry pi webserver that works with the Dry Tap Bottling System.  

![Final Product](/img/product.png)

Here's the basic breakdown of how this works:
  
![Flow Chart](/img/flowchart.png)
  
## Setup / Config
Run config/install.sh to install mod_python, and configure the apache2.conf file.
Everything should work there, but if it doesn't, it shouldn't be hard to manually
follow the install.sh file as a guide.
  
As for config, you'll need to edit index.html, and data/states.db.
In the html file you can set the name of buttons, as well as which pin it'll control/report.

data/states.db contains the automatic steps. when a delay of -1 is reached,
the system will stop and wait for user input to continue. Note that that step will still
need to set the state of at least one pin, or it won't run properly.
  
### States.db:
| Pin | Purpose  |
| --- | -------- |
|  11 | __I__ ndexing |
|  13 | __F__ illing  |
|  15 | __P__ inching |
|  19 | __C__ apping  |

| State | __I__ | __F__ | __P__ | __C__ | Delay |
| ----- | ----- | ----- | ----- | ----- | ----- |
|     0 |   0   |   0   |   0   |   0   |    -1 |
|     1 |   1   |   0   |   0   |   0   |  2000 |
|     2 |   1   |   1   |   0   |   1   |  1000 |
|     3 |   1   |   1   |   1   |   0   | 10000 |
|     4 |   1   |   1   |   0   |   0   |   500 |
|     5 |   1   |   0   |   0   |   0   |  1000 |
|     6 |   0   |   0   |   0   |   0   |   500 |

  
I have created the Daemon using Sander Marechal's sample found [here](http://web.archive.org/web/20131017130434/http://www.jejik.com/articles/2007/02/a_simple_unix_linux_daemon_in_python/).  

## Mechanical System

The vast majority of the mechanical ocumentation can be found in our [report](/report.pdf), but here are a few basics.  
  
Here are some pictures of the mechanisms. This one is the filling area taken from down the queue.  
![Filling area and queue](/img/fill.png)  
  
This one is the capping press, taken from the opposite side of the machine.  
![Capping Press](/img/press.png)  
  
  
### Price Breakdown
![Price Breakdown](/img/cost.png)  

