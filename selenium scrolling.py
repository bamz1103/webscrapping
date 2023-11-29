from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver import chrome
from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#s = Service("C:/Users/BAMIDELE TOBI/Documents/selenium/chromedriver-win64./chromedriver.exe")
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com/search?q=lions&sca_esv=584679428&tbm=isch&sxsrf=AM9HkKlM770DwVDFQHVnkK2Glnr1AttUsg:1700686714626&source=lnms&sa=X&ved=2ahUKEwjyk__bv9iCAxVJQEEAHanGBQ0Q_AUoAXoECAMQAw&biw=1536&bih=786&dpr=1.25")
height = driver.execute_script("return document.body.scrollHeight")
print(height)
while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")