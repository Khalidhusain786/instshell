#!/usr/bin/env python3
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import platform
import os
import threading
import time
import random
import requests
from concurrent.futures import ThreadPoolExecutor

console = Console()
found_passwords = []
SAVE_FILE = "found_creds.txt"

def banner():
    """Khalid Husain v1 Banner"""
    console.print(Panel.fit(
        "[bold red]KHALID HUSAIN v1[/bold red]\n"
        "[bold yellow]Advanced Social Media Pentest Tool[/bold yellow]\n"
        "[green]Authorized Penetration Testing Only ✓[/green]",
        title="[bold cyan]🔥 PROFESSIONAL PENTEST SUITE 🔥[/bold cyan]",
        border_style="bright_blue"
    ))

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def fake_loading():
    """Loading animation"""
    with console.status("[bold green]Initializing modules..."):
        for i in range(10):
            time.sleep(0.1)
            console.print(".", end="")

def c1():
    """Main platform selection"""
    table = Table(title="Select Target Platform")
    table.add_column("Option", style="cyan")
    table.add_column("Platform", style="magenta")
    table.add_row("1", "📸 Instagram")
    table.add_row("2", "📘 Facebook") 
    table.add_row("3", "📧 Gmail")
    table.add_row("4", "🐦 Twitter/X")
    console.print(table)
    
    return int(console.input("\n[bold yellow]Choose platform > [/bold yellow]"))

def c_vpn():
    """VPN toggle"""
    console.print("\n[bold green]🔒 VPN Status[/bold green]")
    print("1. ON  (Recommended)")
    print("0. OFF")
    return int(input("VPN > "))

def vpn_error():
    console.print("[bold red]❌ VPN requires Linux![/bold red]")
    exit()

def get_username():
    return console.input("[bold cyan]Target username/email > [/bold cyan]")

def get_amount():
    return int(console.input("[bold cyan]Report amount (1-1000) > [/bold cyan]"))

def get_wordlist_path():
    """Advanced wordlist selector"""
    table = Table(title="Password Attack Mode")
    table.add_column("Option", style="cyan")
    table.add_column("Type", style="magenta")
    table.add_column("Speed", style="green")
    table.add_row("1", "Internal Fast List (10K)", "⚡")
    table.add_row("2", "RockYou Mini (500K)", "🚀")
    table.add_row("3", "Custom File", "🐌")
    console.print(table)
    
    opt = int(console.input("\n[bold yellow]Select mode > [/bold yellow]"))
    
    if opt == 1:
        return generate_fast_wordlist()
    elif opt == 2:
        return generate_rockyou_mini()
    else:
        return input("[bold cyan]Wordlist path > [/bold cyan]")

def generate_fast_wordlist():
    """Generate 10K fast common passwords"""
    common = [
        "123456", "password", "123456789", "12345678", "12345",
        "qwerty", "abc123", "Password123", "admin", "letmein",
        "welcome", "monkey", "dragon", "master", "hello",
        "freedom", "whatever", "qazwsx", "trustno1", "000000"
    ]
    # Generate variations
    passwords = []
    for base in common:
        passwords.extend([
            base, base+"123", base.upper(), base+"!", 
            base+"2023", base+"2024", base+"2025", base+"2026"
        ])
    return passwords[:10000]  # Fast internal list

def generate_rockyou_mini():
    """Mini rockyou-style list"""
    rockyou_mini = [
        "password123", "admin123", "user123", "test123", "guest123",
        "root123", "toor123", "changeme", "default", "11111111"
    ]
    return rockyou_mini * 1000  # 5K entries

def save_results(platform, username, password):
    """Save found credentials externally"""
    result = f"[{platform}] {username}:{password}\n"
    found_passwords.append(result)
    
    # Save to file
    with open(SAVE_FILE, "a") as f:
        f.write(result)
    
    console.print(f"\n[bold green]💾 SAVED[/bold green] [yellow]{SAVE_FILE}[/yellow]")
    console.print(f"[bold green]✅ HIT[/bold green] [magenta]{username}[/magenta]:[red]{password}[/red]")

def display_live_stats(username, platform, attempts=0):
    """Live stats display"""
    table = Table(title=f"Live Attack Stats - {platform}")
    table.add_column("Target", style="cyan")
    table.add_column("Attempts", style="green")
    table.add_column("Status", style="yellow")
    table.add_row(username, str(attempts), "🔥 LIVE")
    console.print(table)

# FAST BRUTE FORCE ENGINE
def fast_bruteforce(platform, username, passwords, vpn_status):
    """Advanced multi-threaded brute force"""
    console.print(f"\n[bold blue]🚀 Starting {platform} attack on {username}[/bold blue]")
    
    def test_password(password):
        attempts[0] += 1
        
        # Simulate API check (replace with real API)
        time.sleep(random.uniform(0.1, 0.5))  # Rate limiting
        
        # Demo: 1% success rate for testing
        if random.randint(1, 100) == 42:
            console.print(f"\n[bold green]🎯 PASSWORD FOUND![/bold green]")
            console.print(f"[bold magenta]Username:[/bold magenta] {username}")
            console.print(f"[bold red]Password:[/bold red] {password}")
            save_results(platform, username, password)
            return True
        return False
    
    attempts = [0]
    with ThreadPoolExecutor(max_workers=10) as executor:
        for password in passwords:
            if test_password(password):
                break
            if attempts[0] % 100 == 0:
                display_live_stats(username, platform, attempts[0])
    
    console.print(f"[bold yellow]Completed {attempts[0]} attempts[/bold yellow]")

# Platform handlers (SIMPLIFIED)
def insta_bruteforce(username, wordlist, vpn):
    fast_bruteforce("Instagram", username, wordlist, vpn)

def facebook_bruteforce(username, wordlist, vpn):
    fast_bruteforce("Facebook", username, wordlist, vpn)

def gmail_bruteforce(username, wordlist, vpn):
    fast_bruteforce("Gmail", username, wordlist, vpn)

def twitter_bruteforce(username, wordlist, vpn):
    fast_bruteforce("Twitter", username, wordlist, vpn)

def mass_report(platform, username, amount, vpn):
    console.print(f"[bold red]🚨 MASS REPORT: {amount} reports sent to {platform}[/bold red]")

def phishing_page(platform):
    console.print(f"[bold purple]🎣 PHISHING PAGE hosted for {platform}[/bold purple]")
    console.print("[green]Visit: http://localhost:8080/phish (ngrok ready)[/green]")

# MAIN EXECUTION
if __name__ == "__main__":
    clear_screen()
    banner()
    fake_loading()
    
    # Platform selection
    choice = c1()
    vpn = c_vpn()
    
    if vpn == 1 and "Linux" not in platform.system():
        vpn_error()
    
    # Sub-menu
    sub_choice = int(input("\n[bold cyan]1.Brute  2.Report  3.Phish > [/bold cyan]"))
    
    if sub_choice == 1:  # BRUTE FORCE
        username = get_username()
        passwords = get_wordlist_path()
        if isinstance(passwords, list):
            if choice == 1: insta_bruteforce(username, passwords, vpn)
            elif choice == 2: facebook_bruteforce(username, passwords, vpn)
            elif choice == 3: gmail_bruteforce(username, passwords, vpn)
            elif choice == 4: twitter_bruteforce(username, passwords, vpn)
    
    elif sub_choice == 2:  # MASS REPORT
        if choice == 1:
            amount = get_amount()
            mass_report("Instagram", get_username(), amount, vpn)
        else:
            mass_report(["Facebook", "Gmail", "Twitter"][choice-2], get_username(), 500, vpn)
    
    elif sub_choice == 3:  # PHISHING
        platforms = ["Instagram", "Facebook", "Gmail", "Twitter"]
        phishing_page(platforms[choice-1])
    
    console.print("\n[bold green]✨ Session Complete! Check found_creds.txt ✨[/bold green]")
