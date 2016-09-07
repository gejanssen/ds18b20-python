# Installation
pi@rpi-z:~ $ git clone https://github.com/gejanssen/ds18b20-python
Cloning into 'ds18b20-python'...
remote: Counting objects: 37, done.
remote: Total 37 (delta 0), reused 0 (delta 0), pack-reused 37
Unpacking objects: 100% (37/37), done.
Checking connectivity... done.
pi@rpi-z:~ $ 

# Enable 1 wire
pi@rpi-z:~ $ sudo raspi-config
9       Advanced options
A9	1-Wire
Enable
Finish
Reboot

# ds18b20-python

	gej@rpib3:~/ds18b20 $ ls -l /sys/bus/w1/devices
	total 0
	lrwxrwxrwx 1 root root 0 Mar 12 11:47 28-0000064411f2 -> ../../../devices/w1_bus_master1/28-0000064411f2
	lrwxrwxrwx 1 root root 0 Mar 12 11:47 w1_bus_master1 -> ../../../devices/w1_bus_master1
	gej@rpib3:~/ds18b20 $ 


use 28* as a device

### Usage
	gej@rpib3:~/ds18b20 $ python get1temp.py 28-0000064411f2
	22.125
	gej@rpib3:~/ds18b20 $ 


## Aansluitschema

Aansluitschema van de ds18b20 met de raspberry pi

ds18b20-python


[![badge](https://raw.githubusercontent.com/gejanssen/ds18b20-python/master/raspberry-pi-ds18b20-connections.jpg)](https://raw.githubusercontent.com/gejanssen/ds18b20-python/master/raspberry-pi-ds18b20-connections.jpg)

## Te gebruiken

Als je het met de hand wil doen en niet met raspi-config:

	sudo echo "dtoverlay=w1-gpio" >> /boot/config.txt
	(of raspi-config - enable 1wire)
	git clone https://github.com/gejanssen/ds18b20-python
	cd ds18b20-python
	ls -l /sys/bus/w1/devices
	python gettemp.py 28-nummertje-wat-je-gevonden-hebt.
