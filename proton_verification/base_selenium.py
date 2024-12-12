from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from concurrent.futures import ThreadPoolExecutor

class BaseSelenium:
    def __init__(self):
        self.chrome_options = ChromeOptions()
        self.chrome_options.add_argument('--disable-infobars')
        #self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--incognito')
        self.chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        self.driver= webdriver.Chrome(options=self.chrome_options)
        self.wait= WebDriverWait(self.driver,60)
        
    def get(self,url:str):
        self.driver.get(url)
    
    def close(self):
        self.driver.quit()
        print('Selenium stopped In Background') 
    
    def multi_thread(self,fun_pointer,args):
        with ThreadPoolExecutor() as executor:
            future = executor.submit(fun_pointer,args[0],args[1])
            result = future.result()
            return result