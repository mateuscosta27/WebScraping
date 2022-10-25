
from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.keys import Keys 
options = webdriver.ChromeOptions()
driver = webdriver.Chrome
path = 'C:\\tmp\\Driver\\chromedriver.exe'
driver = webdriver.Chrome(options=options,executable_path=path)
driver.get("https://www.geeksforgeeks.org/") 
ActionChains(driver)\
    .key_down(Keys.CONTROL)\
        .send_keys('P').key_up(Keys.CONTROL).perform()