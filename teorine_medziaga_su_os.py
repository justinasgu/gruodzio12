import os
print(os.getcwd())

os.chdir(r"C:\Users\User\Desktop\FOTO\is flasho") #pakeicia vieta is kur bus nuskaitomas failas
print(os.getcwd())
print(os.listdir())
# os.mkdir("waito draugai") #sukuria kataloga
# os.makedirs("asdlkldas/asdasdsd/adsadsadss") #sukuria kataloge kataloga
modifikavimo_laikas = os.stat("02.JPG").st_mtime #duoda duomenis apie pasirinkta objekta is katalogo

import datetime

print(datetime.datetime.fromtimestamp(modifikavimo_laikas))

from datetime import date



