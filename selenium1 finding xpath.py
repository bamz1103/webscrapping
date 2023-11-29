from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver import chrome
from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#s = Service("C:/Users/BAMIDELE TOBI/Documents/selenium/chromedriver-win64./chromedriver.exe")
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://www.jumia.com.ng/")

driver.find_element_by_xpath("""/html/body/div[1]/main/div[1]/div[5]/section/div/div/div[2]/article/a/img""")