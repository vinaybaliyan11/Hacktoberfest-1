from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import re
import os.path
from os import path
import sqlite3
import schedule
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
import discord_webhook


opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_argument("--start-maximized")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
  })



URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=281001&date=08/05/2021"

#put your teams credentials here
CREDS = {'pincode' : '281001', 'age': 20}
CREDS2 = {
	'State' : "Uttar Pradesh",
	'Dis' : "Mathura"
}

age = -1


def start_browser():

	global driver	
	
	driver = webdriver.Chrome(r"C:\Users\suraj\OneDrive\Desktop\An\chromedriver")
	driver.get(URL)

	WebDriverWait(driver,10000).until(EC.visibility_of_element_located((By.TAG_NAME,'body')))
	find_slot()

	
def find_slot():
	srch = driver.find_elements_by_class_name("mat-input-element")[0]
	srch.click()
	srch.send_keys(CREDS["pincode"])
	time.sleep(1)
	
	if(age<18):
		'''discord_webhook'''
	elif(age<=44):
		srch = driver.find_elements_by_id("flexRadioDefault1")[0]
		srch.click()
	else:
		srch = driver.find_elements_by_id("flexRadioDefault3")[0]
		srch.click()

	srch = driver.find_elements_by_class_name("pin-search-btn")[0]
	srch.click()
	time.sleep(5)

	srch = driver.find_elements_by_class_name("available-para")
	if(len(srch)!=0):
		print(srch[0].get_attribute("innerText"))	
		'''discord webhook'''
	else:
		print("vaccines available")
		time.sleep(5)
		count=0
		vavail=1
		y=[]
		while(vavail):
			path="body > app-root > div > app-home > div.maplocationblock.bs-section > div > appointment-table > div > div > div > div > div > div > div > div > div > div > div:nth-child(2) > form > div > div > div.col-padding.matlistingblock > div > div > div > div:nth-child"
			path += "("+ str(vavail) + ")"
			
			try:
				xx=driver.find_element_by_css_selector(path)
				temp = list(xx.get_attribute("innerText").split("\n"))[0]
				y.append(temp)
				count+=1
				vavail+=1
			except:
				break
		
		print(y)
		print("Total vaccinantion centres available",count)







if __name__=="__main__":
	# joinclass("Maths","15:13","15:15","sunday")
	op = 3

	if(op==3):
		
		age = CREDS['age']

		start_browser()
	
	
	
	



'''
body > app-root > div > app-home > div.maplocationblock.bs-section > div > appointment-table > div > div > div > div > div > div > div > div > div > div > div:nth-child(2) > form > div > div > div.col-padding.matlistingblock > div > div > div > div:nth-child(1)

body > app-root > div > app-home > div.maplocationblock.bs-section > div > appointment-table > div > div > div > div > div > div > div > div > div > div > div:nth-child(2) > form > div > div > div.col-padding.matlistingblock > div > div > div > div:nth-child(2)
body > app-root > div > app-home > div.maplocationblock.bs-section > div > appointment-table > div > div > div > div > div > div > div > div > div > div > div:nth-child(2) > form > div > div > div.col-padding.matlistingblock > div > div > div > div:nth-child(3)'''