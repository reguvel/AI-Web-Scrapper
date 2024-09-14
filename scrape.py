import selenium.webdriver as webdriver #to do automation by running the wesite needed to be scrapped in a browser
from selenium.webdriver.chrome.service import Service #To get the Service methods of webBrowser
#import time
from bs4 import BeautifulSoup# This is  for parsing HTML and XML documents, including those with malformed markup
def scrape_website(website):
    print("Launching chrome browser")

    chrome_driver_path=".\chromedriver-win64\chromedriver.exe"
    options=webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode (no browser UI)
    options.add_argument('--disable-gpu')  # Disable GPU hardware acceleration
    options.add_argument('--no-sandbox')  # Bypass OS security model
    options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
    driver=webdriver.Chrome(service=Service(chrome_driver_path),options=options)

    try:
        driver.get(website)
        print("Page Loaded...")
        html=driver.page_source
        #time.sleep(10)

        return html
    finally:
        driver.quit()

# Using the Soap we can extract and return the content we need using the html parser
def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""
#To exclude the unnecesary data such as Scripts, Styling and extra lines
def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")
    
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    ) 

    return cleaned_content
#We can't send all data to LLm at once as the Token has some limit so split the data before sent.
def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i: i+max_length] for i in range(0, len(dom_content), max_length)
    ]