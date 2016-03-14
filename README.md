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

![My image](gejanssen.github.com/ds18b20-python/raspberry-pi-ds18b20-connections.jpg)

[![badge](https://raw.githubusercontent.com/gejanssen/ds18b20-python/master/raspberry-pi-ds18b20-connections.jpg)](https://travis-ci.org/chamerling/ds18b20)

Ok.
ok
