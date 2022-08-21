from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

THE_URL = "http://orteil.dashnet.org/experiments/cookie/"

chrome_driver_path = "/Users/constantin-sebastianiacob/Chrom Driver/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

driver.get(THE_URL)