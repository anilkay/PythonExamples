import urllib.request
import sys
print("How many arguments in "+str(len(sys.argv)))
argument=sys.argv
print(argument[0])
print(argument[1])
Url=argument[1]
doit=True
try:
   print("Try Başlangıcı")
   if Url=="help":
       print("Help İnstruction")
   elif Url.startswith("http"):
       value=urllib.request.urlopen(Url.lower())
       retvalue=value.read().decode("utf-8").strip()
       print(retvalue)
       doit=False
   else :
       Url="http://"+Url
   if doit:
       value = urllib.request.urlopen(Url.lower())
       retvalue = value.read().decode("utf-8").strip()
       print(retvalue)
except:
    print("Can't resolve your Url")
#Http and Https site is work just fine
#python3 /Users/anilkaynar/PycharmProjects/Pingo1/Curl.py heroku.com