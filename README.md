# ProtonMail Account Creator

This Python automation script creates ProtonMail accounts, solves (or assists with) CAPTCHA, and provides a simple GUI for non-technical users.  
It also supports **email verification workflows**, **multi-provider fallback**, and **OTP forwarding workflows**.

---

## Features

- **ProtonMail Account Automation**  
  Automatically creates ProtonMail accounts with optional headless browser mode.

- **CAPTCHA Handling**  
  - Auto-attempts CAPTCHA solving  
  - If solving fails, pauses and prompts you to complete it manually in a visible browser window

- **Minimal GUI**  
  - Specify number of accounts to create  
  - Built-in kill switch to stop the process  
  - Designed for non-technical users

- **Multi-Provider Email Verification**  
  - Automatically switches between **GuerrillaMail** and **Maildrop** domains  
  - Reduces blocking, improves reliability of registration

- **Email Extraction & Forwarding**  
  - Dumps all received mails from created ProtonMail accounts into local files  
  - Can watch inbox for Gmail OTPs and use those to **register new ProtonMail accounts**

- **Headless / Visible Mode Toggle**  
  Choose whether to show browser during registration by modifying a flag in `settings.py`.

- **Session Management**  
  Created accounts are saved in `proton_accounts.csv` for reuse.

---

## Requirements

- Python 3.7+
- Google Chrome
- ChromeDriver (automatically installed if missing)

---

## Setup & Usage

### For Non-Technical Users

Just run:

- `run_app.bat` (Windows)  
- `run_app.sh` (Linux/macOS)

The script will install everything on first launch and open a GUI for configuration.

### For Developers

1. Clone the repository
2. Install dependencies:

   ```bash
   pip install -r requirements.txt

3. Modify settings.py to your preference:

show_browser_window = False  # True = visible, False = headless
time_to_sleep_before_run_next = 30  # Wait time between account creations


4. Run the script:

python main.py






# Output

Accounts are saved to:
proton_accounts.csv

Email dumps saved to:
mails/ (or similar directory, based on implementation)




# Roadmap / TODO

Integrate 2Captcha for fully automatic CAPTCHA solving

Add email forwarding options

Extend support to Outlook/Yandex




# Disclaimer

This tool is intended for educational and research purposes only.
You are solely responsible for how you use this software. Misuse may violate ProtonMail’s terms or applicable laws.

Do not use this tool for spam, fraud, or other malicious activities.



# License

Licensed under the MIT License. See LICENSE for full terms.


# Contributors

https://github.com/Penivera – Developer & automation logic



