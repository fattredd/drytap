#!/bin/bash

# Run this first. It will place all config files and junk

{ crontab -l -u root; echo '@reboot /usr/bin/python /var/www/daemon/autoControl.py start'; } | crontab -u root -

set +e
cd /tmp
wget http://dist.modpython.org/dist/mod_python-3.5.0.tgz
tar -xvf mod_python-3.5.0.tgz
cd mod_python-3.5.0/
./configure --with-python=/usr/bin/python
make
sudo make install

cat /var/www/config/apache >> /etc/apache2/apache2.conf
set -e



