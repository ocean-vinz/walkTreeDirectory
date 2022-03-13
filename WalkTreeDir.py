#!/usr/bin/python
import os

def checkfiles():
    print("What's the minimum number of files you want to display? (Default is 0)")
    minNumberFiles=input()
    if minNumberFiles == "":
        minNumberFiles="0"
    currentdir=os.getcwd()
    if minNumberFiles.isnumeric():
        print('Checking the amount of files in ' + str(currentdir))
        print()
        for foldername, subfolder, filename in os.walk(currentdir):
            numberoffiles=len(filename)
            if numberoffiles >= int(minNumberFiles):
                print(foldername + ' there are ' + str(numberoffiles) + ' files')
    else:
        print("Please only input an integer/numeric!")


checkfiles()

