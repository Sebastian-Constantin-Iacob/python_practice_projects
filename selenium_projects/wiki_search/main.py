from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

THE_URL = "https://www.wikipedia.org/"

chrome_driver_path = "/Users/constantin-sebastianiacob/Chrom Driver/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

driver.get(THE_URL)
search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

driver.quit()
