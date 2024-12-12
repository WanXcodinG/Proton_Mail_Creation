from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
import json
import time
from bs4 import BeautifulSoup
def driver_start():
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--disable-infobars')
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument("user-data-dir=C:\\Users\\Peniel\\AppData\\Local\\Google\\Chrome\\User Data")
    return webdriver.Chrome(options=chrome_options) 

def get_email_pass(filename)->tuple:
    with open(filename,'r') as file:
        cred = json.load(file)
    return (cred['email'],cred['password'])

email,password = "test_email_job@proton.me","Test_email",#get_email_pass('data.json')
email_info={}

def get_text(email_subject,msg_data,driver):
    try:
        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[data-testid='content-iframe']"))
        )
        driver.switch_to.frame(iframe)

        # Extract the iframe content
        iframe_html_content = driver.page_source
        soup = BeautifulSoup(iframe_html_content, 'html.parser')

        # Locate all <p> tags and concatenate their text
        paragraphs = soup.select('p')
        if paragraphs:
            msg = '\n'.join(p.get_text(strip=True) for p in paragraphs)
            email_info.update({'Subject': email_subject, 'Text': msg})
            print(f"{email_subject}\n{msg}")
        else:
            print("No paragraphs found in the iframe content.")
    except Exception as e:
        print(f'Failed to fetch text\n{e}')

def get_email(driver):
    try:
        driver.get('https://account.proton.me/mail')
        driver_wait = WebDriverWait(driver,30)
        email_field = driver_wait.until(EC.presence_of_element_located((By.ID,"username")))
        password_field = driver_wait.until(EC.presence_of_element_located((By.ID,"password")))
        email_field.clear()
        password_field.clear()
        email_field.send_keys(email)
        password_field.send_keys(password)
        driver_wait.until(EC.element_to_be_clickable((By.XPATH,'//button[text() = "Sign in"]'))).click()
        time.sleep(5)
        driver_wait.until(EC.visibility_of_element_located((By.XPATH, '//span[text()="Official"]'))).click() #change official to the expected text at that location
        #driver.execute_script("arguments[0].click();", first_message)
        time.sleep(3)
        email_subject = driver_wait.until(EC.presence_of_element_located((By.XPATH,'//h1[@data-testid="conversation-header:subject"]')))
        msg_data= driver_wait.until(EC.presence_of_element_located((By.XPATH,'//div[@data-testid="message-content:body"]')))
        get_text(email_subject.text,msg_data,driver)
        
        
    except Exception as exc:
        print(f'Error Encountered\n {exc}')
    #driver_wait.until(EC.presence_of_all_elements_located((By.XPATH)))
    finally:
        input()
        driver.close()
    
def main():
    driver = driver_start()
    get_email(driver)

if __name__ == '__main__':
    main()
    
    