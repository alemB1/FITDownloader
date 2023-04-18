import datetime
import re
import os
import json 

def returnDateStr(dateStr):
    sQuery = re.search('\d{2}.\d{2}.\d{4}',dateStr)
    dateFormated = datetime.datetime.strptime(sQuery.group(), '%d.%m.%Y').date()
    return dateFormated

def downloadsLog(downloadList):
    # jebi ti mene ako sam ja ovo pravilno napisao
    logFile = open('downloadLogs.txt','a')
    logFile.write(str(datetime.datetime.today()))
    logFile.writelines(downloadList)
    logFile.close()

def folderSetup():
    f = open('data.json', encoding='utf-8')
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

