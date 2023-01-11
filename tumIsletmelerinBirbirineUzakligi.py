import numpy as np
import matplotlib.pyplot as plt
import json
import pandas as pd
from numpy.random import randn

# Google Haritalar API
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
rnd = np.random
rnd.seed(0)
myjsonfile = open("konum.json", "r", encoding='utf-8')
jsondata = myjsonfile.read()
obj = json.loads(jsondata)

############################

i = 0
a = 0
mesafeler = []
while i < len(obj):
    ilkKonum = (obj[i]["x"], obj[i]["y"])
    ikinciKonum = (obj[a]["x"], obj[a]["y"])
    x = geodesic(ilkKonum, ikinciKonum).km
    # print(obj[i]["ad"], obj[a]["ad"] + " =" + str(round(x, 3)))
    if a == 42:
        mesafeler.append(
            obj[i]["ad"] + " " + obj[a]["ad"] + " = " + str(round(x, 3))
        )
        print(mesafeler)
        mesafeler.clear()
        i = i+1
        a = 0
    else:
        mesafeler.append(
            obj[i]["ad"] + " " + obj[a]["ad"] + " = " + str(round(x, 3))
        )
        a = a+1
