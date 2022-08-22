from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/constantin-sebastianiacob/Chrom Driver/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
