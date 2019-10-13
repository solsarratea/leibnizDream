import os
import sys

def normalizer(text):
    return text

text = ""
for file in os.listdir(sys.argv[1]):
    if file.endswith(".txt"):
        with open(sys.argv[1] + "/" +file,'r') as f:
            text += normalizer(f.read()) + "\n"

with open("text.txt","w") as f:
    f.write(text)
