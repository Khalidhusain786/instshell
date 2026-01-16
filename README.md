# instshell

#termux  

pkg update && pkg install chromium python
pip install undetected-chromedriver selenium
python3 instasuperfast.py

#kali 

cd /home/kali && rm -rf instshell && git clone https://github.com/Khalidhusain786/instshell.git && cd instshell && chmod +x * && pip install -q selenium undetected-chromedriver --break-system-packages && python3 inst.py
