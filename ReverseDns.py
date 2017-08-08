import urllib.request
import sys
import socket
print("Hmm evet bende bunu hiç düşünememiştim "+str(len(sys.argv)))
deger=1

#print(socket.gethostbyname("ce.istanbul.edu.tr"))
if len(sys.argv)>1:
      while deger<len(sys.argv):
         argument=sys.argv[deger]
         hos=str(argument)
         temp=socket.gethostbyname(hos)
         socket.timeout(20)
         print(argument+": "+temp)
         deger=deger+1

"""
from urllib.parse import urlparse
ParsingObj=urlparse("http://ce.istanbul.edu.tr")
print(dir(ParsingObj))
print(ParsingObj.scheme)
print(str(interObject))
interObject=urllib.request.urlopen("http://ce.istanbul.edu.tr")
print(dir(interObject))
print(interObject.url)
print(interObject.getheader("ip"))
print(interObject.status)
print(interObject.code)
print(dir(interObject.info)) Don't have any solution in requested thing because http response don't have pi address
print(dir(interObject.info.__str__))
#print(interObject.getUrl().hostname)
print(interObject.info.__getattribute__("addr"))"""