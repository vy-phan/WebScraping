import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time


def scrape_website(website):
    chrome_drive_path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_drive_path),options=options)

    try:    
        driver.get(website)
        html = driver.page_source
        time.sleep(0.2)
        return html
    finally:    
        driver.quit()

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")    
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser") 

    for script_style in soup(["script","style"]):
        script_style.extract()   

    # get text in html and split to each text is \n
    clean_content = soup.get_text(separator="\n")

    # cach 1 
    clean_content = "\n".join(
        line.strip() for line in clean_content.splitlines() if line.strip()
    )

    # cach 2
    # clean_lines = []
    # for line in clean_content.splitlines():
    #     clean_line = line.strip()
    #     if clean_line:
    #         clean_lines.append(clean_line)
    # clean_content = "\n".join(clean_lines)

    return clean_content

def split_dom_content(dom_content,max_length = 6000):
    return [
        dom_content[i : i+ max_length] for i in range(0,len(dom_content),max_length)
    ]


