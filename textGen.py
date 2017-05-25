#!/usr/bin/env python
import os
import string
import random
import argparse

parser = argparse.ArgumentParser(description='Generate string with a set character count')

parser.add_argument('-n', action="store", dest="charCount", type=int, default=1800, help='Max number of characters in string')
parser.add_argument('-f', action="store", dest="fileName", default="output.txt", help='Name of text file')

argdata=parser.parse_args()

charCount = argdata.charCount
fileName = argdata.fileName

def genWord():
    charSet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890?:.,=+'
    minLength = 5
    maxLength = 30
    length = random.randint(minLength, maxLength)
    return ''.join(map(lambda unused : random.choice(charSet), range(length)))

paragraph = genWord()
parLength = len(paragraph)

while (parLength<charCount):
    paragraph = paragraph + " " + genWord()
    parLength = len(paragraph)

if parLength > charCount:
    x = parLength - charCount
    paragraph = paragraph[:-x]

print ("Text File ",fileName," generated")


#output to file
txtFile = open(fileName,"w+")
txtFile.write(paragraph)
txtFile.close
