import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service

def scrape_website(website):
    print("Launching chrome browser...")

    chrome_driver_path=""
    options = webdriver.Chrome