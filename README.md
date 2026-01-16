# instshell

#termux  

pkg update && pkg install chromium python
pip install undetected-chromedriver selenium
python3 instasuperfast.py

#kali 

cd /home/kali && rm -rf instshell && git clone https://github.com/Khalidhusain786/instshell.git && cd instshell && chmod +x * && pip install -q selenium undetected-chromedriver --break-system-packages && python3 inst.py

# Termux
pkg install tor chromium python
pip install -r requirements.txt

# Kali
apt install tor chromium python3-pip
pip3 install undetected-chromedriver selenium requests stem

# TOR Shadow (optional)
sudo apt install tor stem -y && tor &

# RUN SUPERNOVA
python3 supernova_inst.py
