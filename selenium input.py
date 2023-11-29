from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver import chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time 

options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#s = Service("C:/Users/BAMIDELE TOBI/Documents/selenium/chromedriver-win64./chromedriver.exe")
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://www.tutorialsfreak.com/")
time.sleep(2)
driver.find_element("xpath", """/html/body/div/div[2]/header/nav/div/div[2]/div/div[7]/button""").click()
time.sleep(2)
ph_no = driver.find_element("xpath", """/html/body/div[3]/div/div/div[1]/div[2]/div[3]/form/div/input""")
ph_no.send_keys("1234567890")
driver.find_element("xpath", """/html/body/div[3]/div/div/div[1]/div[2]/div[3]/form/button""").click()


