import os
import time
import base64
from twocaptcha import TwoCaptcha
import settings


class TwoCaptchaSolver:
    def __init__(self):
        self.api_key = settings.TWOCAPTCHA_API_KEY
        if self.api_key == "YOUR_2CAPTCHA_API_KEY_HERE":
            raise ValueError("Please set your 2Captcha API key in settings.py")
        
        self.solver = TwoCaptcha(self.api_key)
        self.timeout = settings.CAPTCHA_TIMEOUT
        self.poll_interval = settings.CAPTCHA_POLL_INTERVAL

    def solve_recaptcha_v2(self, site_key, page_url):
        """
        Solve reCAPTCHA v2 using 2Captcha service
        """
        try:
            print("[2CAPTCHA] Mengirim reCAPTCHA v2 untuk diselesaikan...")
            result = self.solver.recaptcha(
                sitekey=site_key,
                url=page_url,
                timeout=self.timeout,
                polling_interval=self.poll_interval
            )
            print(f"[2CAPTCHA] reCAPTCHA v2 berhasil diselesaikan: {result['code'][:50]}...")
            return result['code']
        except Exception as e:
            print(f"[2CAPTCHA ERROR] Gagal menyelesaikan reCAPTCHA v2: {e}")
            return None

    def solve_recaptcha_v3(self, site_key, page_url, action="submit", min_score=0.3):
        """
        Solve reCAPTCHA v3 using 2Captcha service
        """
        try:
            print("[2CAPTCHA] Mengirim reCAPTCHA v3 untuk diselesaikan...")
            result = self.solver.recaptcha(
                sitekey=site_key,
                url=page_url,
                version='v3',
                action=action,
                score=min_score,
                timeout=self.timeout,
                polling_interval=self.poll_interval
            )
            print(f"[2CAPTCHA] reCAPTCHA v3 berhasil diselesaikan: {result['code'][:50]}...")
            return result['code']
        except Exception as e:
            print(f"[2CAPTCHA ERROR] Gagal menyelesaikan reCAPTCHA v3: {e}")
            return None

    def solve_hcaptcha(self, site_key, page_url):
        """
        Solve hCaptcha using 2Captcha service
        """
        try:
            print("[2CAPTCHA] Mengirim hCaptcha untuk diselesaikan...")
            result = self.solver.hcaptcha(
                sitekey=site_key,
                url=page_url,
                timeout=self.timeout,
                polling_interval=self.poll_interval
            )
            print(f"[2CAPTCHA] hCaptcha berhasil diselesaikan: {result['code'][:50]}...")
            return result['code']
        except Exception as e:
            print(f"[2CAPTCHA ERROR] Gagal menyelesaikan hCaptcha: {e}")
            return None

    def solve_image_captcha(self, image_path_or_base64):
        """
        Solve image-based CAPTCHA using 2Captcha service
        """
        try:
            print("[2CAPTCHA] Mengirim image CAPTCHA untuk diselesaikan...")
            
            if os.path.exists(image_path_or_base64):
                # If it's a file path
                result = self.solver.normal(image_path_or_base64)
            else:
                # If it's base64 encoded image
                result = self.solver.normal(image_path_or_base64)
            
            print(f"[2CAPTCHA] Image CAPTCHA berhasil diselesaikan: {result['code']}")
            return result['code']
        except Exception as e:
            print(f"[2CAPTCHA ERROR] Gagal menyelesaikan image CAPTCHA: {e}")
            return None

    def get_balance(self):
        """
        Get 2Captcha account balance
        """
        try:
            balance = self.solver.balance()
            print(f"[2CAPTCHA] Saldo akun: ${balance}")
            return balance
        except Exception as e:
            print(f"[2CAPTCHA ERROR] Gagal mendapatkan saldo: {e}")
            return None