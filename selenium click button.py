from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver import chrome
from webdriver_manager.chrome import ChromeDriverManager
import time 

options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#s = Service("C:/Users/BAMIDELE TOBI/Documents/selenium/chromedriver-win64./chromedriver.exe")
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://www.tutorialsfreak.com/")
time.sleep(2)
driver.find_element("xpath", """/html/body/div[1]/div[2]/div[2]/section[1]/div/div[1]/div/div/div/div[2]/button""").click()
time.sleep(2)
driver.find_element("xpath", """/html/body/div/div[2]/div[2]/section/div/div[2]/div[1]/div/ul/li[7]/a """).click()