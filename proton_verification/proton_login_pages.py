from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from proton_verification.base_selenium import BaseSelenium
from settings import proton_login_address
from bs4 import BeautifulSoup
import re
from common.save_in_file import FileHandling
from exceptions.possible_exceptions import GettingVerificationCodeException
import settings

class Proton_login_pages(BaseSelenium):
    def __init__(self):
        super().__init__()                
    
    def get_text(self,email_subject):
        try:
            iframe = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[data-testid='content-iframe']"))
            )
            self.driver.switch_to.frame(iframe)

            # Extract the iframe content
            iframe_html_content = self.driver.page_source
            soup = BeautifulSoup(iframe_html_content, 'html.parser')

            # Locate all <p> tags and concatenate their text
            paragraphs = soup.select('p')
            if paragraphs:
                msg = '\n'.join(p.get_text(strip=True) for p in paragraphs)
                print(f"{email_subject}\n{msg}") #for debuggging
                return re.search(r'\b\d{6}\b', msg).group()
                #email_info={'Subject': email_subject, 'Text': msg}
            else:
                print("No paragraphs found in the iframe content.")
        except Exception as e:
            print(f'Failed to fetch text\n{e}')

    def _get_email(self,email,password):
        for retries in range(5):
            try:
                if (retries +1) == 5:
                    raise GettingVerificationCodeException('Failed To Retrieve Verification Code')
                self.get(proton_login_address)
                email_field = self.wait.until(EC.presence_of_element_located((By.ID,"username")))
                password_field = self.wait.until(EC.presence_of_element_located((By.ID,"password")))
                email_field.clear()
                password_field.clear()
                email_field.send_keys(email)
                password_field.send_keys(password)
                self.wait.until(EC.element_to_be_clickable((By.XPATH,'//button[text() = "Sign in"]'))).click()
                time.sleep(3)
                target=self.wait.until(EC.visibility_of_element_located((By.XPATH, '//span[contains(text(), "Proton Verification Code")]'))) #change official to the expected text at that location
                #driver.execute_script("arguments[0].click();", target)
                if target:
                    try:
                        target.click()
                    except Exception:
                        print('Standard click failed in email trying alternative')
                        self.driver.execute_script("arguments[0].click();", target)
                    email_subject = self.wait.until(EC.presence_of_element_located((By.XPATH,'//h1[@data-testid="conversation-header:subject"]')))
                    FileHandling.one_line_write(settings.used_emails,email)
                    return self.get_text(email_subject.text)
            except Exception as exc:
                print(f'Error Encountered\n {exc}')
                self.driver.refresh()
                time.sleep(3)
            finally:
                #input()
                self.close()
    
    def get_otp(self,email,passwd):
        verification_code = self.multi_thread(self._get_email,[email,passwd])
        return verification_code

            
            

