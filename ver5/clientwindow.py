#clientWindow.py
from tkinter import *
import time
import urllib.request
import os
import sys

if "stream_elements" not in os.listdir(os.getcwd()):
    os.mkdir("stream_elements")

# Takes the web string which looks like
# "stream_elements\p1Name.txt,Alternis|stream_elements\p1Score.txt,0|stream_elements\p2Name.txt,Rocketman|stream_elements\p2Score.txt,0"
def decodeStreamElements(webString):
    splitted = webString.split("|")
    # print(splitted)
    content = []
    for item in splitted:
        content.append(item.split(","))
    return content

# url = 'http://192.168.0.92:9000'
url = f"http://{sys.argv[1]}:{sys.argv[2]}"
#uf = urllib.request.urlopen(url)
#html = uf.read()

# Process the inputs and do something
oldList = []
while True:
    #try:
        #print("Starting request")
        uf = urllib.request.urlopen(url)
        #print("Processing Request")
        html = uf.read()
        if type(html) == type(b""):
            html = html.decode("utf-8")
        html = html[:-1]
        #print(html)
        #print(type(html))
        #print("Things Read")
        content = decodeStreamElements(html)
        #print("Content Fixed")
        for sublist in content:
            directory = sublist[0]
            words = sublist[1]
            with open(directory, 'w') as f:
                f.write(words)
        time.sleep(2)
        if oldList != content:
            print("Updated Info!")
            for item in content:
                print(f"{content[0]}\t{content[1]}")
        else:
            print(".", end = "")
        oldList = content
    #except:
    #    print("WHOOPS, BAD CONNECTION")
