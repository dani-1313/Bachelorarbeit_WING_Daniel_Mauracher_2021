import time #Zeitmodul für Datum, Uhrzeit etc.
import os #Modul zum erstellen, entfernen oder Umbenennen von Dateien
import requests #HTTP-Anforderungen versenden

Zeit = time.strftime('%Y-%m-%d_%H:%M:%S',time.localtime()) #aktuelles Datum mit Uhrzeit erstellen und String erstellen
Zeit = str(Zeit)
'print(Zeit)'

#die CSV Datei mit den Varaiblen umbenennen mit aktueller Zeit und Datum
os.rename(r"/home/pi/Desktop/BA-Arbeit/ADS/valuestest.csv",r"/home/pi/Desktop/BA-Arbeit/ADS/valuestest"+ str(Zeit)+".csv")

#die umbenannte CSV Datei versenden an die nächste Schnittstelle 
path = r"/home/pi/Desktop/BA-Arbeit/ADS/valuestest"+ str(Zeit)+".csv"
url = 'https://fast-tundra-21451.herokuapp.com/user/5fd8cbf53f23c92bfc9b07ac'

with open(path, 'rb') as f:
    r = requests.put(url, files={'testFile': f})

print(r.text)

# die CSV Datei wieder zurück benennen wie am Anfang
os.rename(r"/home/pi/Desktop/BA-Arbeit/ADS/valuestest"+ str(Zeit)+".csv",r"/home/pi/Desktop/BA-Arbeit/ADS/valuestest.csv")