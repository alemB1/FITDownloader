from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys # nez jel mi treba
from selenium.webdriver.chrome.options import Options # headless
from selenium.webdriver.support.ui import Select
from auxFunctions import auxfunctions
from datetime import date
import json
import time
import datetime # poredjenja radi
import re 
import auxFunctions

def returnDateStr(dateStr):
    sQuery = re.search('\d{2}.\d{2}.\d{4}',dateStr)
    dateFormated = datetime.datetime.strptime(sQuery.group(), '%d.%m.%Y').date()
    return dateFormated
    logFile = open('downloadLogs.txt','a')
    logFile.write(datetime.datetime.today(), "\n", "-------------------------------------------------")
    logFile.writelines(downloadList)
    logFile.write("-------------------------------------------------")
    logFile.close()

f = open('data.json',encoding='utf-8')
dataLoad = json.load(f)
studentID = dataLoad['creds']['brojIndexa']
studentPswd = dataLoad['creds']['lozinka']
studentYear = dataLoad['creds']['godinaStudija']
subjects = dataLoad['predmetiII']
# fetches user login credientials

browserOptions = webdriver.ChromeOptions()
browserOptions.add_argument('--headless') # efficiency vise

# login 
#browser = webdriver.Chrome() # delete later
browser = webdriver.Chrome(options=browserOptions)
browser.get('https://www.fit.ba/student/login.aspx')
browser.find_element(By.NAME, "txtBrojDosijea").send_keys(studentID)
browser.find_element(By.NAME, "txtLozinka").send_keys(studentPswd)
browser.find_element(By.NAME, "btnPrijava").click()
print("Logged in.")
browser.find_element(By.ID, "dok").click()
yearSelect = Select(browser.find_element(By.XPATH, '//*[@id="listGodina"]'))
yearSelect.select_by_visible_text(str(studentYear))

time.sleep(2) 
downloadedFiles = 0
downloadsLogs = []

for subjectLabel in subjects:

    docDropdown = Select(browser.find_element(By.XPATH,'//*[@id="ddlPredmeti"]'))
    docDropdown.select_by_visible_text(subjectLabel)

    documentsArea = browser.find_element(By.ID, 'listDokumentUP');
    label = documentsArea.find_elements(By.ID, 'lbtnNaslov')
    info = documentsArea.find_elements(By.ID,'lblVrsta') 

    #dT = date.today()
    #todaysDate = dT.strftime("%d.%m.%Y") #izbrisi ovo kasnije ovo testa radi
    todaysDate = datetime.date(2023,4,18)
    checkBoxCounter = 3 # checkboxes start at 3 for some reason

    # Check for titles of new documents
    for labelText, docInfo in zip(label,info):
        if(returnDateStr(docInfo.text) == todaysDate):
            print(labelText.text, " was uploaded today, downloading now...")
            checkBoxCounter += 1
            downloadedFiles += 1
            downloadsLogs.append(labelText.text)

    # Check and download new files
    browser.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': True})            
    for n in range(3,checkBoxCounter):
        documentsArea.find_element(By.XPATH, '/html/body/form/div[4]/div[1]/div[4]/table/tbody/tr['+str(n)+']/td/contenttemplate/table/tbody/tr/td[2]/input').click()
        time.sleep(5)
        checkBoxCounter += 1
        
    browser.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': False})  
    documentsArea.find_element(By.XPATH, '//*[@id="lbtnDownloadSelected"]').click()
    # i have to write a wait function

print(downloadedFiles, " files was downloaded")

if(downloadedFiles != 0):
    auxfunctions.downloadsLog(downloadsLogs)

browser.quit()

auxFunctions.moveToFolder()
