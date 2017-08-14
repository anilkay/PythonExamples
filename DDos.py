import os
import sys
a=0
network=""
if len(sys.argv)>1:
    network=sys.argv[1]
while a<255:
    os.system("ping -c 1 "+network+"."+str(a))
    a=a+1