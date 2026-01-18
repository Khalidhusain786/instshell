from utils import *
from rich.console import Console
import platform
console = Console()

def banner():
    """Khalid Husain v1 Banner"""
    console.print("""
[bold cyan]╔══════════════════════════════════════════════════════════════╗[/bold cyan]
[bold cyan]║                      [bold red]KHALID HUSAIN[/bold red] v1                     ║[/bold cyan]
[bold cyan]║              [bold yellow]Advanced Social Media Pentest Tool[/bold yellow]        ║[/bold cyan]
[bold cyan]║                 [green]Authorized Penetration Testing[/green]               ║[/bold cyan]
[bold cyan]╚══════════════════════════════════════════════════════════════╝[/bold cyan]
    """)

# print banner & loading screen
banner()
start()

# select social media
choice = c1()

# advanced password options
def get_advanced_wordlist():
    """Get advanced/fast wordlist with options"""
    console.print("\n[bold yellow]🛡️ PASSWORD OPTIONS 🛡️[/bold yellow]")
    console.print("[bold green]1.[/bold green] Basic Wordlist")
    console.print("[bold green]2.[/bold green] Advanced Combo List (User:Pass)")
    console.print("[bold green]3.[/bold green] RockYou.txt (14M passwords)")
    console.print("[bold green]4.[/bold green] Custom Generated (Fast)")
    console.print("[bold green]5.[/bold green] Hybrid Attack (Wordlist + Rules)")
    
    while True:
        try:
            opt = int(input("\n[bold cyan]Select password option [1-5]: [/bold cyan]"))
            if opt in [1,2,3,4,5]:
                break
            else:
                console.print("[bold red]❌ Invalid option! Choose 1-5[/bold red]")
        except:
            console.print("[bold red]❌ Enter a number![/bold red]")
    
    if opt == 1:
        return get_wordlist()
    elif opt == 2:
        return get_combo_list()
    elif opt == 3:
        return "rockyou.txt"
    elif opt == 4:
        target = get_username()
        return generate_custom_wordlist(target)
    elif opt == 5:
        base_list = get_wordlist()
        return apply_rules(base_list)

#vpn on/off
vpn = c_vpn()

if vpn == 1:
    if "Linux" not in platform.system():
        vpn_error()

def handle_platform(platform_name):
    """Unified handler for all platforms"""
    choice = start_instagram()  # This should be renamed to start_platform()
    
    if choice == 1:  # Brute Force
        username = get_platform_username(platform_name)
        wordlist = get_advanced_wordlist()
        if platform_name == "instagram":
            insta_bruteforce(username, wordlist, vpn)
        elif platform_name == "facebook":
            facebook_bruteforce(username, wordlist, vpn)
        elif platform_name == "gmail":
            gmail_bruteforce(username, wordlist, vpn)
        elif platform_name == "twitter":
            twitter_bruteforce(username, wordlist, vpn)
            
    elif choice == 2:  # Mass Report
        if platform_name == "instagram":
            username = get_username()
            amount = get_amount()
            insta_massreport(username, vpn, amount, 1)
        elif platform_name == "facebook":
            facebook_massreport()
        elif platform_name == "gmail":
            gmail_massreport()
        elif platform_name == "twitter":
            twitter_massreport()
            
    elif choice == 3:  # Phishing
        if platform_name == "instagram":
            insta_phishing()
        elif platform_name == "facebook":
            facebook_phishing()
        elif platform_name == "gmail":
            gmail_phishing()
        elif platform_name == "twitter":
            twitter_phishing()

# Main platform selection with advanced features
if choice == 1:
    handle_platform("instagram")
elif choice == 2:
    handle_platform("facebook")
elif choice == 3:
    handle_platform("gmail")
elif choice == 4:
    handle_platform("twitter")

console.print("\n[bold green]✅ Pentest completed! Check your results.[/bold green]")
