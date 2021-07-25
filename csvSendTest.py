import requests #ermöglicht HTTP Anforderungen zu versenden

path = "/home/pi/Desktop/BA-Arbeit/ADS/valuestest.csv" # die Datei path versenden an den Link von url
url = 'https://fast-tundra-21451.herokuapp.com/user/5fbd6b40dd1e3e3aa08c9029'

with open(path, 'rb') as f: # die Datei path versenden an den Link von url
    r = requests.put(url, files={'testFile': f})

print(r.text)

