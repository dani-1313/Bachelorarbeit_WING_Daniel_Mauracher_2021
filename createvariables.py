import board #ermöglicht Zugriff auf Pins vom Board
import busio #unterstützendes Modul für serielle Protokolle
import numpy # Modul für Array oder Matrizen
import csv # Lese/Schreib Möglichkeit für CSV-Formate

i2c = busio.I2C(board.SCL, board.SDA) #I²C Busanbindung aktivieren

import adafruit_ads1x15.ads1015 as ADS #Hersteller Treiber vom ADS1015

from adafruit_ads1x15.analog_in import AnalogIn #Hersteller Treiber vom ADS1015 

ads = ADS.ADS1015(i2c) #die I²C Buswerte mit den Pins verknüpfen und in eine Liste schreiben
chan = AnalogIn(ads, ADS.P0)
list = []


for i in range(50): #in die Liste 50 variablen schreiben mittles einer Schleife
        #print(chan.value, chan.voltage)
        values = chan.voltage
        values = round(values, 3)
        list.append(values)
         
print(list) # die erstellte Liste in ein CSV-File schreiben
with open("/home/pi/Desktop/BA-Arbeit/ADS/valuestest.csv",'w') as myfile:
    write = csv.writer(myfile)
    write.writerow(list)


