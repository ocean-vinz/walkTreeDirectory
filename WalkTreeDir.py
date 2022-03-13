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
        currentcount=0
        for foldername, subfolder, filename in os.walk(currentdir):
            numberoffiles=len(filename)
            if numberoffiles >= int(minNumberFiles):
                print(foldername + ' there are ' + str(numberoffiles) + ' files')
                if numberoffiles > currentcount:
                    currentcount=numberoffiles
                    highestfolder=foldername
        print()
        print('SUMMARY: ')
        print('Checking starts from this parent folder: ' + str(currentdir))
        print(f'The highest count is inside folder {highestfolder} with the total of {currentcount} files')
    else:
        print("Please only input an integer/numeric!")


checkfiles()

