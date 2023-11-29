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
#driver.save_screenshot("C:/Users/BAMIDELE TOBI/Pictures/Screenshots/tutorial.png")
driver.find_element("xpath", """/html/body/div/div[2]/div[2]/section[1]/div/div[1]/div/div/div/div[3]/span/img""").screenshot("C:/Users/BAMIDELE TOBI/Pictures/Screenshots/girl.png")