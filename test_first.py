import random
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

def test_register():

    chrome_options = ChromeOptions()


    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")


    service = ChromeService(ChromeDriverManager().install())  # Use ChromeService
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # chrome_options: ChromeOptions = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    # service_obj = Service("chromedriver")
    email = os.environ.get("EMAIL")
    random_email = str(random.randint(1,10000))
    driver.get("http://seleniumdemo.com/?page_id=7")
    driver.find_element(By.ID, "reg_email").send_keys(email)
    driver.find_element(By.ID, "reg_password").send_keys("testttt123!!!!!")
    driver.find_element(By.NAME, "register").click()
