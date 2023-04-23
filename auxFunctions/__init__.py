import os
import shutil
import json
import time
from datetime import date
from pathlib import Path

def moveToFolder():
    downloadPath = '/Users/belko/Downloads/' # change this
    foldersPath = 'C:/Users/belko/Desktop/'

    year1 = {'DL':'Digitalna logika',
            'EJ I':'Engleski jezik I',
            'EJ II':'Engleski jezik II', 
            'MAT I':'Matematika I',
            'MAT II':'Matematika II',
            'OS':'Operativni sistemi', 
            'PR I':'Programiranje I',
            'PR II':'Programiranje II',
            'RI':'Računarstvo i informatika',
            'UM':'Uvod u marketing',
            'WRD':'Web razvoj i programiranje'
            }

    year2 = {'ADS':'Analiza i dizajn softvera','BP II':'Baze podataka II',
                'BP I':'Baze podataka I',
                'ENG III':'Engleski jezik III',
                'KGR':'Kompjuterska grafika',
                'MAT III':'Matematika III',
                'PS':'Primijenjena statistika',
                'RM':'Računarske mreže I',
                'SPA':'Strukture podataka i algoritmi'}

    def checkDate(itemDate):
        dateNames = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        currentDate = date.today()
        itemDateFormated = itemDate.split()
        
        for m in dateNames:
            if(m == itemDateFormated[1]):
                itemDateFormated[1] = str(dateNames.index(m)+1)

        itemDateFormated = itemDateFormated[1]+"-"+itemDateFormated[2]
        currentDate = str(currentDate.month) +'-' + str(currentDate.day)

        return (itemDateFormated == currentDate)


    for item in os.listdir(downloadPath):
        # stavi provjera godine iz json fajla
        fileMDate = time.ctime(os.path.getmtime(downloadPath+item))
        if(checkDate(fileMDate) == True):
            print(item)
            for key, value in year2.items():
                if((key in item) and Path(foldersPath+value+item).is_file() == False):
                    shutil.move(downloadPath+item, foldersPath + value)
                    #print(downloadPath+item, "   ", foldersPath+value)
                    print(item, " successfully moved to ", foldersPath+value)    

def FolderSetup():
    f = open('c:/Users/belko/Desktop/New folder/data.json', encoding='utf-8')
    folderNames = json.load(f)
    yearOfStudy = ""

    # selecting the appropriate json list
    if(folderNames['creds']['godinaStudija'] == 1):
        yearOfStudy = 'predmetiI'

    elif(folderNames['creds']['godinaStudija'] == 2):
        yearOfStudy = 'predmetiII'

    elif(folderNames['creds']['godinaStudija'] == 3):
        yearOfStudy = 'predmetiIII'    

    else:
        print("Error in json file -> ['creds'], check json setup and try again.")
        print("Further execution terminated.")
        quit()

    subjectList = folderNames[yearOfStudy]
    desktopPath = 'C:/Users/belko/Desktop'

    for item in subjectList:
        newPath = desktopPath+"/"+item
        if(os.path.exists(newPath) == False):
            os.mkdir(newPath)
        else:
            print(item + " already exists")

def checkIfDownloaded(downloadPath):
    # fix downloadPath - stavi ime predmeta plus datum
    isExisting = os.path.exists(downloadPath)
    return isExisting
