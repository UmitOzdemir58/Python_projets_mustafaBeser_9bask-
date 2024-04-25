import os
q='c:/windows/system32'

for i in os.walk(q):
    print(i)
    # diğer konular bitince bu bölüme tekrar dön