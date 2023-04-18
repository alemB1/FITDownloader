import json
import os

f = open('FITDownloader/data.json', encoding='utf-8')
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

