import urllib.request
import sys
import time
argument=sys.argv
Url=argument[1]
if Url == "help":
    print("Help İnstruction")
elif Url.startswith("http"):
    print("")
else:
    Url = "http://" + Url
def ping(url):
    nf=urllib.request.urlopen(url)
    start = time.time()
    page = nf.read()
    end = time.time()
    nf.close()
    return round((end-start)*1000,3)
try:
   print(str(ping(Url))+" Miliseconds")
except:
    print("Yaz bakalım")

