import os
import time
klasor='C:/Program Files/Common Files/System'
for i in os.listdir(klasor):
    dosya=os.path.join(klasor,i)
    durum=os.stat(dosya)
    if os.path.isdir(dosya):
        print('<Klasor> ',time.ctime(durum.st_ctime),i)
    elif os.path.isdir(dosya):
        print('<Dosya> ',time.ctime(durum.st_ctime),i)
