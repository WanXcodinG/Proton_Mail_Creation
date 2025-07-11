filename = 'proton_accounts.csv'

# If this parameter is True you can see how all registration works in browser step by step
show_browser_window = True  # True or False

# waiting between creating emails
time_to_sleep_before_run_next = 50  # seconds

# Please wait a few minutes before sending email alert (in register_with_temporary_email method)
time_to_slee_if_exception_in_alert_occurred = 10  # seconds

# protonmail domain
protonmail_domain = '@proton.me'

# If you want to open this file in ms excel, leave ';'
csv_delimiter =';'

# How many accounts can app create by 1 session
max_accounts_count = 5

protonmail_registration_address = "https://account.proton.me/signup?plan=free&billing=24&currency=EUR&language=en"

proton_login_address= 'https://account.proton.me/mail'

#csv file headers
headers=['protonmail address', 'protonmail password', 'date and time']

#Read email file
used_emails='used_email.csv'

# 2Captcha API Key - Ganti dengan API key Anda
TWOCAPTCHA_API_KEY = "YOUR_2CAPTCHA_API_KEY_HERE"

# 2Captcha timeout settings
CAPTCHA_TIMEOUT = 300  # 5 minutes
CAPTCHA_POLL_INTERVAL = 10  # Check every 10 seconds
