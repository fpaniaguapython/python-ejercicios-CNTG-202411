import time
import datetime

ini = time.time()
time.sleep(5)
fin = time.time()
print(ini)#1731690270.704353
print(fin)#1731690275.7052257
print(fin-ini)#5.000872611999512
print(datetime.date.fromtimestamp(ini))#2024-11-15
print(datetime.datetime.fromtimestamp(ini))#2024-11-15 18:05:20.215774
#datetime.time