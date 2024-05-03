import time
from datetime import datetime
from colorama import *
import requests
from requests.sessions import session

tiktok_url = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mLink Video Target \033[1;31m: \033[0;37m")

while True:

    proxies = requests.get(url="https://advanced.name/freeproxy/661f6cf3e8bc5").text.split('\r\n') #Update Your Proxy List From This URL (https://advanced.name/freeproxy/)

    for proxy in proxies:

        try:
            now = datetime.now()
            
            current_time = now.strftime("%H:%M:%S")

            req = session().post(tiktok_url, proxies={'http': f'http://{proxy}'})

            print(f' \033[1;34m[{current_time}]' + f' Proxy: {proxy} Report Sent')
            
        except:
        
            print(' \033[1;31mSome Thing Gay Here Its Not Working:) ')
            
            input(' Press Enter to close the program')
            
            exit()
