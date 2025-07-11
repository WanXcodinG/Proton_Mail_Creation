#from proton_verification.fetch_otp import proton_login_pages
import os
import sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
from common.save_in_file import FileHandling
from proton_verification.proton_login_pages import Proton_login_pages
import settings
from datetime import datetime

def test_automation(email,passwd):
    login= Proton_login_pages()
    otp=login.get_otp(email,passwd)
    return otp
def test_read_file():
    file = FileHandling(settings.filename,settings.headers)
    data =file.filter_data()
    email,password = data[0]
    time= datetime.utcnow()
    return email,password,time.strftime("%d:%m:%Y-%H:%M:%S")

#print(test_automation())
def test_write(data):
    file = FileHandling(settings.filename,settings.headers)
    file.add_to_file(data)
    #FileHandling.one_line_write(settings.used_emails,data[0])
    return FileHandling.one_line_read(settings.used_emails)


email,passwd,_ = test_read_file()   
print(test_automation(email,passwd))

print('Completed')





