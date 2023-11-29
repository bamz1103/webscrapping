from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver import chrome
from webdriver_manager.chrome import ChromeDriverManager
import time

options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#s = Service("C:/Users/BAMIDELE TOBI/Documents/selenium/chromedriver-win64./chromedriver.exe")
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://www.ajio.com/s/footwear-4792-56592?query=%3Arelevance%3Al1l3nestedcategory%3AWomen%20-%20Sneakers&curated=true&curatedid=footwear-4792-56592&gridColumns=3")
time.sleep(15)
while True:
    height = driver.execute_script("return document.body.scrollHeight")
    print(height)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    new_height = driver.execute_script("return document.body.scrollHeight")
    if height==new_height:
        break