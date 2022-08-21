# Get a list of up and coming events and the dates
from selenium import webdriver
from selenium.webdriver.common.by import By

THE_URL = "https://www.python.org/"
main_dict = {}

chrome_driver_path = "/Users/constantin-sebastianiacob/Chrom Driver/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

driver.get(THE_URL)
item = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
value_list = item.text.split("\n")
print(value_list)

driver.quit()
