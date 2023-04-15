from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # nez jel mi treba
from selenium.webdriver.chrome.options import Options # headless
from selenium.webdriver.support.ui import Select
from auxFunctions import auxfunctions
import os # morat cu micati fajlove
import json
import time
import datetime # poredjenja radi
import re 

def returnDateStr(dateStr):
    sQuery = re.search('\d{2}.\d{2}.\d{4}',dateStr)
    dateFormated = datetime.datetime.strptime(sQuery.group(), '%d.%m.%Y').date()
    return dateFormated

    # jebi ti mene ako sam ja ovo pravilno napisao
    logFile = open('downloadLogs.txt','a')
    logFile.write(datetime.datetime.today(), "\n", "-------------------------------------------------")
    logFile.writelines(downloadList)
    logFile.write("-------------------------------------------------")
    logFile.close()

f = open('data.json',encoding='utf-8')
dataLoad = json.load(f)
studentID = dataLoad['creds']['brojIndexa']
studentPswd = dataLoad['creds']['lozinka']
subjects = dataLoad['predmetiII']
# fetches user login credientials

browserOptions = webdriver.ChromeOptions()
browserOptions.add_argument('--headless') # efficiency vise

# login 
browser = webdriver.Chrome() # delete later
# browser = webdriver.Chrome(options=browserOptions) add later
# browser = webdriver.Chrome()
browser.get('https://www.fit.ba/student/login.aspx')
browser.find_element(By.NAME, "txtBrojDosijea").send_keys(studentID)
browser.find_element(By.NAME, "txtLozinka").send_keys(studentPswd)
browser.find_element(By.NAME, "btnPrijava").click()

browser.find_element(By.ID, "dok").click()
# replace this with builtin function of selenium WhileLoads
time.sleep(2) 
downloadedFiles = []

for subjectLabel in subjects:

    docDropdown = Select(browser.find_element(By.XPATH,'//*[@id="ddlPredmeti"]'))
    docDropdown.select_by_visible_text(subjectLabel)

    documentsArea = browser.find_element(By.ID, 'listDokumentUP'); # stavio sam ovo jer hocu samo u tom podrucju da nalazim elemente
    label = documentsArea.find_elements(By.ID, 'lbtnNaslov')
    info = documentsArea.find_elements(By.ID,'lblVrsta') 

    todaysDate = datetime.date(2023,4,5) #izbrisi ovo kasnije ovo testa radi

    checkBoxCounter = 3 # 
    for labelText, docInfo in zip(label,info):
        if(returnDateStr(docInfo.text) == todaysDate):
            browser.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': True})            
            print(labelText.text, " was uploaded today, downloading now...", checkBoxCounter)
            documentsArea.find_element(By.XPATH, '/html/body/form/div[4]/div[1]/div[4]/table/tbody/tr['+str(checkBoxCounter)+']/td/contenttemplate/table/tbody/tr/td[2]/input').click()
            documentsArea.find_element(By.XPATH, '//*[@id="lbtnDownloadSelected"]').click()            
            documentsArea.find_element(By.XPATH, '/html/body/form/div[4]/div[1]/div[4]/table/tbody/tr['+str(checkBoxCounter)+']/td/contenttemplate/table/tbody/tr/td[2]/input').click()
            checkBoxCounter += 1
            browser.execute_cdp_cmd('Emulation.setScriptExecutionDisabled', {'value': False})  
            time.sleep(2)
            


auxfunctions.downloadsLog(downloadedFiles)
browser.quit()
