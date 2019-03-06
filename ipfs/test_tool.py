import sys
import os
from os.path import isfile, join, getsize
import ipfsapi
import datetime
from matplotlib import pylab, mlab

try:
    api = ipfsapi.connect('127.0.0.1', 5001)
except:
    print("Cant connect to node")
    sys.exit(1)

path = input("Folder with files to upload: ")
files = ["{}/{}".format(path, entry) for entry in os.listdir(path) if isfile(join(path, entry))]

if len(files) == 0:
    print("No files in directory")
    sys.exit(1)
else:
    time_size = {}
    for file in files:
        print("adding {}".format(file))
        before = datetime.datetime.now()
        api.add(file)
        after = datetime.datetime.now()
        print(str(after-before))
        delta = after-before
        time_size[getsize(file)] = delta.total_seconds()

list_sizes = list(time_size.keys())
print(list_sizes.sort())

def build_graf(coordlist):

    ylist = list(coordlist.values())
    xlist = list(coordlist.keys())
    xlist.sort()
    ylist.sort()
    print(xlist)
    print(ylist)

    pylab.plot(xlist, ylist)

    pylab.show()

build_graf(time_size)
