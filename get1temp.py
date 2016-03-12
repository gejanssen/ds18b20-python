#get1temp
version = "v1.0"
import sys

#commandline variabele check (ik controleer alleen maar of er een variable meegegeven wordt)
try:
    _serialnum=(sys.argv[1])
except:
    print ("Manier van opstarten: 'get1temp.py {serienummer van de 1wire ds1820 of ds18b20}'")
    print ("Programma afgebroken.")
    sys.exit()

# het daadwerkelijk ophalen en vertalen van de gegevens
for i in range(5):
#       _serialnum="28-0000045c4c55"
        filename="/sys/bus/w1/devices/"+_serialnum+"/w1_slave"
        tfile= open(filename)
        text = tfile.read()
        tfile.close()
        secondline = text.split("\n")[1]
        temperaturedata= secondline.split(" ")[9]
        global temperature
        temperature = float(temperaturedata[2:])
        temperature = temperature / 1000
        print temperature
        firstline = text
        ccrrcc = firstline.split(" ")[11]
        ccrrcc = (ccrrcc[:3]) #take only first 3 characters
        global noflag
        noflag = 0
        if ccrrcc == 'YES':
            break
        else:
            print ' Oops er ging iets mis'
