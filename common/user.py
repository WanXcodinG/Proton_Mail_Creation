from email_services.mailbox_interface import EmailBox
from reg_values_generators.generators import return_user_data
from common.save_in_file import FileHandling
import settings
from proton_verification.proton_login_pages import Proton_login_pages


class User:
    def __init__(self):
        self.email_interface = EmailBox()
        self.proto_interface = Proton_login_pages()
        self.__nickname = None
        self.__password = None
        self.__proton_mail = None
        self.__proton_pass = None

    def generate_new_user(self):
        self.__nickname, self.__password = return_user_data()

    def get_another_domain(self):
        self.email_interface.get_another_domain()
        
    def email_for_verification(self):
        file = FileHandling(settings.filename,settings.headers)
        used_mails = FileHandling.one_line_read(settings.used_emails)
        login_info = file.filter_data(used_mails)
        self.__proton_mail,self.__proton_pass = login_info[0]
    
    @property
    def proton_mail_for_verification(self):
        return self.__proton_mail
    @property
    def nickname(self):
        return self.__nickname

    @property
    def password(self):
        return self.__proton_pass

    @property
    def full_email_name_for_verification(self):
        return self.nickname + self.email_interface.email_domain

    @property
    def verification_code(self):
        #return self.email_interface.get_verification_code(self.nickname)
        return self.proto_interface.get_otp(self.__proton_mail,self.__proton_pass)
