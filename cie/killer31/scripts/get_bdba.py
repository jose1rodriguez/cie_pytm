from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import shutil
import time

url='https://bdba001.icloud.intel.com/#/groups/32?search=killer&offset=0'

with open('/Users/CIE/Documents/latest_build.txt', 'r') as f:
    latest_build = f.readlines()

#options = Options()
options = webdriver.ChromeOptions()

options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
s=Service('/Users/CIE/Documents/chromedriver_win32/chromedriver.exe')

#driver = webdriver.Chrome(service=s, options=options)
driver = webdriver.Chrome('/Users/CIE/Documents/chromedriver_win32/chromedriver.exe', options=options)

driver.get(url)

time.sleep(2)

username=driver.find_element(By.ID,"username")
username.send_keys("joserod1")

time.sleep(2)

continue_button =driver.find_element(By.XPATH,"//button[text()='Continue']")
continue_button.click()

time.sleep(2)

username=driver.find_element(By.ID,"password")
username.send_keys("Tacos1213!!")

time.sleep(2)

login_button =driver.find_element(By.XPATH,"//button[text()='Log in']")
login_button.click()

time.sleep(5)

build =driver.find_element(By.XPATH,"//span[text()='Killer-"+str(latest_build[0])+"-x64-Release.zip']")
build.click()

time.sleep(2)

results= driver.find_element(By.ID,"btn-result-sidebar-export").click()

time.sleep(1)

results= driver.find_element(By.ID,"result-dd-export-all-known-vulns").click()

time.sleep(2)

download_results=driver.find_element(By.XPATH,"//button[text()='Download']")
download_results.click()

time.sleep(5)

latest_build=latest_build[0].replace('.','')
shutil.copyfile('/Users/CIE/Downloads/killer-'+str(latest_build)+'-x64-releasezip-vulnerabilities.csv', '/Users/CIE/Documents/Release/killer-'+str(latest_build)+'-x64-releasezip-vulnerabilities.csv')

driver.close()
