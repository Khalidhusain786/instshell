# 🔥 ONE-CLICK DEPLOY (Recommended)
curl -sSL https://raw.githubusercontent.com/Khalidhusain786/instshell/main/deploy.sh | bash

# OR MANUAL:
cd /home/kali
rm -rf instshell
git clone https://github.com/Khalidhusain786/instshell.git
cd instshell
chmod +x *
pip install selenium undetected-chromedriver webdriver-manager --break-system-packages
python3 inst.py
