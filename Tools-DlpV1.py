#!/usr/bin/python3
import sys
import subprocess
import time
import pyttsx3
from colorama import Fore, init

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

try: # Import Module
    import requests
    import time
    import random
    import os
    import urllib3
    import json
    import bs4

except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'requests'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'urllib3'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'bs4'])
finally:
    import requests # Post, Get, & Put URL API
    import urllib3  # HTTP client untuk Python
    from bs4 import BeautifulSoup as bs

from time import sleep
from datetime import date
from urllib3.exceptions import *
from bs4 import BeautifulSoup as bs
from pip._vendor.requests import post,get

#Tahun tanggal bulan
today = date.today()

# Mengambil input


def rod2(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.050)

def rod(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.004)

 #warna inisial hit
hijau   =   "\033[1;92m"
putih   =   "\033[1;97m"
abu     =   "\033[1;90m"
kuning  =   "\033[1;93m"
ungu    =   "\033[1;95m"
merah   =   "\033[1;91m"
biru    =   "\033[1;96m"
ungu2   =   "\33[3;47;43m" #Purple
putih2  =   "\033[0;47;90m"
merah2  =   "\033[0;30;91m" 
def track():
    print (f"""
{merah} Tools Tracking / Sosial Engering
⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⢠⡆⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⣷⣄⠀⠀⠀⠀⣾⣷⠀⠀⠀⠀⣠⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢿⠿⠃⠀⠀⠀⠉⠉⠁⠀⠀⠐⠿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣶⣶⣶⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀        [1] seeker
⠀⠀⠀⣠⣶⣿⣿⡿⣿⣿⣿⡿⠋⠉⠀⠀⠉⠙⢿⣿⣿⡿⣿⣿⣷⣦⡀⠀⠀⠀       [2] track ip|by fahad
⠀⢀⣼⣿⣿⠟⠁⢠⣿⣿⠏⠀⠀⢠⣤⣤⡀⠀⠀⢻⣿⣿⡀⠙⢿⣿⣿⣦⠀⠀       [3] track ip 2
{putih}⣰⣿⣿⡟⠁⠀⠀⢸⣿⣿⠀⠀⠀⢿⣿⣿⡟⠀⠀⠈⣿⣿⡇⠀⠀⠙⣿⣿⣷⡄ 
⠈⠻⣿⣿⣦⣄⠀⠸⣿⣿⣆⠀⠀⠀⠉⠉⠀⠀⠀⣸⣿⣿⠃⢀⣤⣾⣿⣿⠟⠁       [4] track fb
⠀⠀⠈⠻⣿⣿⣿⣶⣿⣿⣿⣦⣄⠀⠀⠀⢀⣠⣾⣿⣿⣿⣾⣿⣿⡿⠋⠁⠀⠀       [5] osint
⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀        [6] osint 2
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠿⠿⠿⠿⠿⠿⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀          [7] crimeflare
⠀⠀⠀⠀⠀⠀⠀⢰⣷⡦⠀⠀⠀⢀⣀⣀⠀⠀⠀⢴⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⠟⠁⠀⠀⠀⠘⣿⡇⠀⠀⠀⠀⠙⢷⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠻⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀


""")
    a = input(Fore.RED+"╔═══"+Fore.RED+"[""ROOT"+Fore.WHITE+"@"+Fore.WHITE+"MENU/SE"+Fore.WHITE+"]"+Fore.RED+"\n╚══\x1b[38;2;0;255;189m> "+Fore.RED)
    if a == "1" or a == "seeker" or a == "Seeker" or a == "SEEKER":
      check_input = 1
      os.system("clear")
      print(f"{merah} Seeker")
      os.system("git clone https://github.com/thewhiteh4t/seeker.git")
      os.system("cd seeker")
      print(f"{hijau}kembali dalam 3 detik")
      time.sleep(3)
      os.system("clear")
      track()
    elif a == "2"or a == "track ip" or a == "trackip" or a == "Trackip" or a == "track ip 1":
        check_input = 1
        os.system("clear")
        print(f"{merah}Track-ip By Fahad")
        os.system("git clone https://github.com/fahadsyihab06/Track-ip.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        track()
    elif a == "3"or a == "track ip2" or a == "trackip2" or a == "track ip 2" or a == "track ip2":
        check_input = 1
        os.system("clear")
        print(f"{merah}IPGeoLocation")
        os.system("git clone https://github.com/maldevel/IPGeoLocation.git")
        os.system("cd IPGeoLocation")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        track()
    elif a == "4"or a == "Track fb" or a == "track fb" or a == "TRACK FB":
        check_input = 1
        os.system("clear")
        print(f"{merah}Track FB")
        os.system("git clone https://github.com/warifp/FacebookToolkit.git")
        os.system("cd FacebookToolkit")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        track()
    elif a == "5"or a == "osint" or a == "Osint" or a == "OSINT":
        check_input = 1
        os.system("clear")
        print(f"{merah}OsintGram")
        os.systen("git clone https://github.com/Datalux/Osintgram.git")
        os.system("cd Osintgram")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        track()
    elif a == "6"or a == "OSINT2" or a == "osint2" or a == "Osint2":
        check_input = 1
        os.system("clear")
        print(f"{merah}fbsleepstats")
        os.system("git clone https://github.com/sorenlouv/fb-sleep-stats.git")
        os.system("cd fb-sleep-stats")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        track()
    elif a == "7"or a == "Crimeflare" or a == "CRIMEFLARE" or a == "CrimeFlare":
        check_input = 1
        os.system("clear")
        print(f"{merah}CrimeClare")
        os.system("git clone https://github.com/zidansec/CloudPeler.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        track()
    elif a == "k" or a == "K":
        check_input = 1
        os.system("clear")
        jawab1()
    else:
        print(f"{merah}Ketik Dengan Benar Ngab")
        time.sleep(2.0)
        os.system("clear")
        track()

def theme():
    a = input(f"""
{merah} Password

{merah}[1] {ungu} Termux-OhMyZsh
{merah}[2] {ungu} Theme-me
{merah}[3] {ungu} T-Header

{merah}[k] {ungu} Kembali

{biru}Input:{merah}~# {putih}""")
    if a == "1":
      check_input = 1
      os.system("clear")
      print(f"{ungu} OhMyZsh")
      os.system("git clone https://github.com/Cabbagec/termux-ohmyzsh.git")
      print(f"{hijau}kembali dalam 3 detik")
      time.sleep(3)
      os.system("clear")
      theme()
    elif a == "2":
        check_input = 1
        os.system("clear")
        print(f"{merah} Theme Me")
        os.system("git clone https://github.com/Zidan-ID17/Theme-Me.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        theme()
    elif a == "3" :
        check_input = 1
        os.system("clear")
        print(f"{merah}T Header")
        os.system("git clone https://github.com/remo7777/T-Header.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        theme()
    elif a == "k" or a == "K":
        check_input = 1
        os.system("clear")
        jawab1()
    else: 
        print(f"{merah}Ketik Dengan Benar Ngab")
        time.sleep(2.0)
        os.system("clear")
        theme()
def password():
    a = input(f"""
{merah} Password

{merah}[1] {ungu} Zphisher
{merah}[2] {ungu} Pyphisher
{merah}[3] {ungu} Maxphisher
{merah}[4] {ungu} Password
{merah}[5] {ungu} PassFB

{merah}[k] {ungu} Kembali

{biru}Input:{merah}~# {putih}""")

    if a == "1":
      check_input = 1
      os.system("clear")
      print(f"{ungu} Zphisher")
      os.system("git clone https://github.com/htr-tech/zphisher.git")
      print(f"{hijau}kembali dalam 3 detik")
      time.sleep(3)
      os.system("clear")
      password()    
    elif a == "2":
        check_input = 1
        os.system("clear")
        print(f"{merah} Pyphisher")
        os.system("git clone https://github.com/KasRoudra2/PyPhisher.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        password()

    elif a == "3" :
        check_input = 1
        os.system("clear")
        print(f"{merah}MaxPhisher")
        os.system("git clone https://github.com/jaykali/maskphish.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        password()

    elif a == "4":
        check_input = 1
        os.system("clear")
        print(f"{merah}PwnedOrNot")
        os.system("git clone https://github.com/thewhiteh4t/pwnedOrNot.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        password()

    elif a == "5":
        check_input = 1
        os.system("clear")
        print(f"{merah}PhisherMan")
        os.system("git clone https://github.com/FDX100/Phisher-man.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        password()

    elif a == "k" or a == "K":
        check_input = 1
        os.system("clear")
        jawab1()

    else:
       print(f"{merah}ketik dengan benar")
       time.sleep(2.0)
       os.system("clear")
       password()

def virus():
    a = input(f"""
{merah} MENU VIRUS0
⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠇⡌⡆⠀⠀⠀⠀⠀⠸⢱⠸⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠰⢠⡴⢷⠦⠀⠀⠀⠴⡺⢮⡄⠆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⢃⠂⡔⠁⣀⠤⠀⢤⣀⠈⢂⠑⡐⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡆⠀⢰⢴⢞⠟⡻⣿⢟⠻⡳⡦⡆⢠⢡⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡠⢄⣇⠰⡀⠣⣁⣞⣏⣟⡻⣳⡐⠜⢀⠆⣘⡠⢄⠀⠀⠀⠀
⠀⠀⢀⠔⢸⣿⡿⠳⢬⣐⡂⢎⡯⣿⢽⡹⢐⣂⡥⠞⢿⣿⡇⠢⠀⠀⠀
⠀⠀⠒⠢⢍⡫⡀⠀⣏⡀⠀⠀⠀⠉⠀⠀⠀⠀⣙⠀⢀⢜⡭⠗⠃⠀⠀
⠀⠀⠀⠀⣸⡳⡰⢠⢫⣷⣿⣿⡿⠛⣿⣿⣿⣿⡝⡄⢆⢞⣇⠀⠀⠀⠀
⠀⠀⠀⡰⠁⢒⣇⠋⠾⠻⣿⡿⣳⣤⣾⢿⡿⠛⠷⠙⣸⡒⠊⢆⠀⠀⠀
⠀⠀⡰⢃⣉⣡⣿⣮⣶⣤⣔⠚⢵⢿⡮⠓⣠⣤⣖⣵⣿⣌⣁⡚⢄⠀⠀
⠀⠔⣉⣠⣿⣿⣿⣿⣿⣿⣧⡀⣀⠀⣀⢀⣽⣿⣿⣿⣿⣿⣿⣄⣉⠢⠀
⢸⡉⠀⠈⠉⠙⠛⠛⣿⡏⣿⣣⣿⠤⣶⣜⡿⣸⣿⠛⠛⠋⠉⠁⠀⢈⠇
⠀⠈⠉⠐⠒⠀⠠⠤⠬⠿⠮⣳⠋⠈⠙⣞⠵⠿⠥⠤⠄⠀⠒⠂⠈⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{merah}[1] {ungu}Virus1
{merah}[2] {ungu}Virus2
{merah}[3] {ungu}Virus1
{merah}[4] {ungu}Virus1


{merah}[k] {ungu}Kembali

{biru}Input:{merah}~# {putih}""")
    if a == "1":
      check_input = 1
      os.system("clear")
      print(f"{merah}Vbug")
      os.system("git clone https://github.com/jota01234/Vbug.git")
      print(f"{hijau}kembali dalam 3 detik")
      time.sleep(3)
      os.system("clear")
      virus()
    elif a == "2":
        check_input = 1
        os.system("clear")
        print(f"{merah}Petya")
        os.system("git clone https://github.com/Ravissonce/Petya2.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        virus()
    elif a == "3":
        check_input = 1
        os.system("clear")
        print(f"{merah}Memz")
        os.system("git clone https://github.com/NyDubh3/MEMZ.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        virus()
    elif a == "4":
        check_input = 1
        os.system("clear")
        print(f"{merah}Ah Myth")
        os.system("git clone https://github.com/Morsmalleo/AhMyth.git ")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        virus()
    elif a == "k" or a == "K":
        check_input = 1
        jawab1()
    else:
        print(f"{merah}type correctly")
        time.sleep(2.0)
        os.system("clear")
        virus()
def ddos():
    a = input(f"""
{merah} 
          .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'   DDOS   `98v8P'   MENU    `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             '
{merah}[1] {ungu}DDoS1
{merah}[2] {ungu}DDoS2
{merah}[3] {ungu}DDoS3
{merah}[4] {ungu}DDoS4
{merah}[5] {ungu}DDoS5
{merah}[6] {ungu}DDoS6
{merah}[7] {ungu}DDoS7
{merah}[8] {ungu}DDoS8
{merah}[9] {ungu}DDoS9

{merah}[k] {ungu}Kembali


{biru}Input:{merah}~# {putih}""")
    if a == "1":
      check_input = 1
      os.system("clear")
      print(f"{ungu}DDoS Ripper")
      os.system("git clone https://github.com/palahsu/DDoS-Ripper.git")
      print(f"{hijau}kembali dalam 3 detik")
      time.sleep(3)
      os.system("clear")
      ddos()
    elif a == "2":
        check_input = 1
        os.system("clear")
        print(f"{ungu}DDoS Karma")
        os.system("git clone https://github.com/HyukIsBack/KARMA-DDoS.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        ddos()
    elif a == "3":
        check_input = 1
        os.system("clear")
        print(f"{ungu}DDoS Hammer")
        os.system("git clone https://github.com/cyweb/hammer.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        ddos()
    elif a == "4":
        check_input = 1
        os.system("clear")
        print(f"{ungu}DDoS SlowHttpTest")
        os.system("git clone https://github.com/shekyan/slowhttptest.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        ddos()
    elif a == "5":
        check_input = 1
        os.system("clear")
        print(f"{ungu}DDoS MHD")
        os.system("git clone https://github.com/MatrixTM/MHDDoS.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        ddos()
    elif a == "6":
        check_input = 1
        os.system("clear")
        print(f"{ungu}DDoS Hulk")
        os.system("git clone https://github.com/Hyperclaw79/HULK-v3.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        ddos()
    elif a == "7":
        check_input = 1
        os.system("clear")
        print(f"{ungu}Overload")
        os.system("git clone https://github.com/7zx/overload.git")
        print(f"{hijau}kembali dalam 3 detik")
        ddos()
    elif a == "8":
        check_input = 1
        os.system("clear")
        print(f"{ungu}RootSec")
        os.system("git clone https://github.com/R00tS3c/DDOS-RootSec.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        ddos()
    elif a == "9":
        check_input = 1
        os.system("clear")
        print(f"{ungu}White Ddos")
        os.system("git clone https://github.com/WH1T3-E4GL3/white-ddos.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        ddos()
    elif a == "k" or a == "K":
        check_input = 1 
        jawab1()
    else:
        print(f"{merah}Ketik  dengan benar woila")
        time.sleep(2.0)
        os.system("clear")
        ddos()
def otp():
    a = input(f"""

{biru}                   Menu SpamOTP
                            ,-.
       ___,---.__          /'|`\          __,---,___
    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.
  ,'        |           ~'\     /`~           |        `.
 /      ___//              `. ,'          ,  , \___      \ 
|    ,-'   `-.__   _         |        ,    __,-'   `-.    |
|   /          /\_  `   .    |    ,      _/\          \   |
\  |           \ \`-.___ \   |    / ___,-'/ /           |  /
 \  \           | `._   `\ \  |  / /'   _,' |           /  /
  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'
     ``       /     \    ,='/ \`=.    /     \       ''
             |__   /|\_,--.,-.--,--._/|\   __|
             /  `./  \ \`\ |  |  | /,/ /'\,'  \ 
            /   /     ||--+--|--+-/-|     \   \ 
           |   |     /'\_\_\ | /_/_/`\     |   |
            \   \__, \_     `~'     _/ .__/   /
             `-._,-'   `-._______,-'   `-._,-'
{merah}             [1] spam1            [4]spam4
             [2] spam2(by core)   [5]spam5
             [3] spam3            [6]spam5
{merah}[k] {ungu}Kembali

{biru}Input:{merah}~# {putih}""")
    if a == "1":
      check_input = 1
      os.system("clear")
      print(f"{merah}BtgSpmV2")
      os.system("git clone https://github.com/destroyerLinuxPropaly/Btg-SpamV2.git")
      print(f"{hijau}kembali dalam 3 detik")
      time.sleep(3)
      os.system("clear")
      otp()
    elif a == "2":
        check_input = 1
        os.system("clear")
        print(f"{merah}BocchiSpam")
        os.system("git clone https://github.com/u0-a154/bocchi-penghitam")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        otp()

    elif a == "3":
        check_input = 1
        os.system("clear")
        print(f"{merah} SpamOtp2 {hijau}Janga lupa pip install bahan.txt dari sc spam-wa")
        os.system("git clone https://github.com/TZdev7/spam-wa.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        otp()
    elif a == "6":
        check_input = 1
        os.system("clear")
        print(f"{merah} OTPTerror")
        os.system("git clone https://github.com/Bayu12345677/OTP_TERROR.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        otp()
    elif a == "4":
        check_input = 1
        os.system("clear")
        print(f"{merah}==> Index-SpamV2 <==")
        os.system("git clone https://github.com/AmmarrBN/Index-SpamV2.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        otp()
    elif a == "5":
        check_input = 1
        os.system("clear")
        print(f"{merah}==> TBomb <==")
        os.system("git clone https://github.com/TheSpeedX/TBomb.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        otp()
    elif a == "k" or a == "K":
        check_input = 1
        jawab1()
    else:
        print(f"{merah}Ketik  dengan benar woila")
        time.sleep(2.0)
        os.system("clear")
        otp()

def cam1():
    a = input(f"""
{biru}Menu Camera

{merah}[1] {ungu}Camera
{merah}[2] {ungu}Camera2
{merah}[3] {ungu}Camera3
{merah}[4] {ungu}Camera4 {biru}By Mikael
{merah}[5] {ungu}CamHack {biru}By Core

{merah}[k] {ungu}kembali

{biru}Input:{merah}~# {putih}""")
    if a == "1":
      check_input = 1
      os.system("clear")
      print(f"{kuning} Install CamHacker")
      os.system("git clone https://github.com/KasRoudra/CamHacker")
      os.system("cd CamHacker")
      print(f"{hijau}kembali dalam 3 detik")
      time.sleep(3)
      os.system("clear")
      cam1()
    elif a == "2":
        check_input = 1
        os.system("clear")
        print(f"{kuning} cloning VidPhisher")
        os.system("git clone https://github.com/KasRoudra2/VidPhisher.git")
        os.system("cd VidPhisher")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        cam1()
    elif a == "k" or a == "K":
        check_input = 1
        jawab1()
    elif a == "3":
        check_input = 1
        os.system("clear")
        print(f"{merah}CamPhish")
        os.system("git clone https://github.com/techchipnet/CamPhish.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        cam1()
    elif a == "4":
        check_input = 1
        os.system("clear")
        print(f"{merah}Z Cam")
        os.system("git clone https://github.com/goldeneye121/z-cam.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        cam1()
    elif a == "5":
        check_input = 1
        os.system("clear")
        print(f"{merah}CamHack")
        os.system("git clone https://github.com/u0-a154/camhack-byaddress")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        cam1()
    else:
        print(f"{merah}ketik dengan benar")
        time.sleep(2.0)
        os.system("clear")
        cam1()
def exploit():
    a = input(f"""
{merah} EXPLOIT MENU


{merah}[1] {ungu}ysoserial
{merah}[2] {ungu}traitor
{merah}[3] {ungu}Exploit
{merah}[4] {ungu}Exploit2
{merah}[5] {ungu}Ghost
{merah}[6] {ungu}MetasPloit

{merah}[k] {ungu}Kembali

{biru}Input:{merah}~# {putih}""")
    if a == "1":
      check_input = 1
      os.system("clear")
      print(f"{merah}ysoserial")
      os.system("git clone https://github.com/frohoff/ysoserial.git")
      print(f"{hijau}kembali dalam 3 detik")
      time.sleep(3)
      os.system("clear")
      exploit()
    elif a == "2":
        check_input = 1
        os.system("clear")
        print(f"{merah}Traitor")
        os.system("git clone https://github.com/liamg/traitor.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        exploit()
    elif a == "3":
        check_input = 1
        os.system("clear")
        print(f"{merah}Exploit")
        os.system("git clone https://github.com/kyo1337/revsliderautoexploiter")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        exploit()
    elif a == "4":
        check_input = 1
        os.system("clear")
        print(f"{merah}PhoneSploit")
        os.system("git clone https://github.com/AzeemIdrisi/PhoneSploit-Pro.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        exploit()
    elif a == "5":
        check_input = 1
        os.system("clear")
        print(f"{merah}Ghost")
        os.system("git clone https://github.com/EntySec/Ghost.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        exploit()
    elif a == "6":
        check_input = 1
        os.system("clear")
        print(f"{merah}MetasPloit")
        os.system("git clone https://github.com/rapid7/metasploit-framework.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        exploit()
    elif a == "k" or a == "K":
        check_input = 1
        os.system("clear")
        jawab1()
    else:
        print(f"{merah}Ketik  dengan benar woila")
        time.sleep(2.0)
        os.system("clear")
        exploit()
def ig():
    a = input(f"""{merah}
                 INFORMATING GATHERING MENU
                           _____                   
                       ,-:` \;',`'-,               
       1.Nmap        .'-;_,;  ':-;_,'.     3.SQLmap
       2.webkiller  /;   '/    ,  _`.-\    4.SQLB
                   | '`. (`     /` ` \`|
                   |:.  `\`-.   \_   / |
                   |     (   `,  .`\ ;'|
                    \     | .'     `-'/
                     `.   ;/        .'
                       `'-._____.-'`
                {merah}[k] {ungu}Kembali

{biru}Input:{merah}~# {putih}""")
    if a == "1":
      check_input = 1
      os.system("clear")
      print(f"{merah}Nmap")
      os.system("git clone https://github.com/nmap/nmap.git")
      print(f"{hijau}kembali dalam 3 detik")
      time.sleep(3)
      os.system("clear")
      ig()
    elif a == "2":
        check_input = 1
        os.system("clear")
        print(f"{merah}WebKiller")
        os.system("git clone https://github.com/ultrasecurity/webkiller.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        ig()
    elif a == "3":
        check_input = 1
        os.system("clear")
        print(f"{merah}Sqlmap")
        os.system("git clone https://github.com/sqlmapproject/sqlmap.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        ig()
    elif a == "4":
        check_input = 1
        os.system("clear")
        print(f"{merah}Sqlbatis")
        os.system("git clone https://github.com/mybatis/mybatis-3.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        ig()
    elif a == "k" or a == "K":
        check_input = 1
        os.system("clear")
        jawab1()
    else:
        print(f"{merah}Ketik  dengan benar woila")
        time.sleep(2.0)
        os.system("clear")
        ig()

def deface():
    a = input(f"""
{merah}                   DEFACE MENU
                             /^\/^\ 
    1.deface all tools       \----|
    2.white deface       _---'---~~~~-_
    3.deface null         ~~~|~~L~|~~~~
                             (/_  /~~--
                           \~ \  /  /~
                         __~\  ~ /   ~~----,
                         \    | |       /  \ 
                         /|   |/       |    |
                         | | | o  o     /~   |
                       _-~_  |        ||  \  /
                      (// )) | o  o    \ \---'
                      //_- |  |          \ 
                     //   |____|\______\__\ 
                     ~      |   / |    |
                             |_ /   \ _|
                           /~___|  /____\         
{merah}[k] {ungu}Kembali

{biru}Input:{merah}~# {putih}""")
    if a == "1":
      check_input = 1
      os.system("clear")
      print(f"{merah}FireCrack")
      os.system("git clone https://github.com/Ranginang67/Firecrack.git")
      print(f"{hijau}kembali dalam 3 detik")
      time.sleep(3)
      os.system("clear")
      deface()
    elif a == "2":
        check_input = 1
        os.system("clear")
        print(f"{merah}WhiteDeface")
        os.system("git clone https://github.com/WH1T3-E4GL3/white-deface.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        deface()
    elif a == "3":
        check_input = 1
        os.system("clear")
        print(f"{merah}WhiteDeface")
        os.system("")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        deface()
    elif a == "k" or a == "K":
        check_input = 1
        os.system("clear")
        jawab1()
    else:
        print(f"{merah}Ketik  dengan benar woila")
        time.sleep(2.0)
        os.system("clear")
        deface()

def deep():
    print(f"""{kuning} Perbesar {merah}Layar {kuning}anda! Biar Tidak Ngebug""")
    time.sleep(5.0)
    rod(f"""{merah}

http://3bp7szl6ehbrnitmbyxzvcm3ieu7ba2kys64oecf4g2b65mcgbafzgqd.onion/ - {ungu} UKpassports – real UK passports
{merah}http://lqcjo7esbfog5t4r4gyy7jurpzf6cavpfmc4vkal4k2g4ie66ao5mryd.onion/ - {ungu} USfakeIDs – US fake ID store
{merah}http://k6m3fagp4w4wspmdt23fldnwrmknse74gmxosswvaxf3ciasficpenad.onion/ - {ungu} Uk Guns and Ammo Store
{merah}http://t43fsf65omvf7grt46wlt2eo5jbj3hafyvbdb7jtr2biyre5v24pebad.onion/ - {ungu} EuroGuns
{merah}http://xf2gry25d3tyxkiu2xlvczd3q7jl6yyhtpodevjugnxia2u665asozad.onion/ - {ungu} Peoples Drug Store – The Darkwebs best Drug supplier!
{merah}http://2ln3x7ru6psileh7il7jot2ufhol4o7nd54z663xonnnmmku4dgkx3ad.onion/ - {ungu} Brainmagic – Best Darkweb psychedelics
{merah}http://kl4gp72mdxp3uelicjjslqnpomqfr5cbdd3wzo5klo3rjlqjtzhaymqd.onion/ - {ungu} Smokeables – Finest organic cannabis from the USA
""")
    a = input(f"""{biru}Kembali Ke Menu Utama Ketik{putih} Y/y

Input: {putih}""")
    if a == "y" or a == "Y":
      check_input = 1
      os.system("clear")
      jawab1()
    else:
      print(f"{merah}Ketik Dengan Benar")
      time.sleep(2.0)
      os.system("clear")
      deep()

def net():
    a = input(f"""

⠀⠀⠀⠀⠀⠀⠀⠀⠀                 ⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
{merah}⠀⠀⠀⠀⠀⠀⠀⠀⠀                ⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀          
⠀⠀⠀⠀1.wifi hack       ⠀⠀⠀⢀⣶⣿⣿⡿⠛⠉⠉⠉⠛⢿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀    4.network kathara    
⠀⠀  2.wifi hack2  ⠀⠀⠀⠀⢀⣴⣿⣿⣿⠋⡀ ⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀     5.Router
⠀   3.wifi hack 3 ⣀⣰⣶⣿⣿⣿⣿⣿⣿⣀⣀⣀⣀⣀⣀⣰⣰⣶⣿⣿⣿⣿⣿⣿⣷⣦⣤⣀   6.Network                         
{putih}                ⠉⠉⠉⠉⠈⠉⠛ ⣿⣿⡽⣏  ⠉⠉⠉⠉⠉⣽⣿⠛⠉⠉⠉⠉⠉⠉⠉⠁
⠀⠀⠀⠀⠀⠀⠀⠀                ⠀⠀⠉⠻⣷⣦⣄⣀⣠⣴⣾⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                ⠀⠀⠈⠛⠿⠿⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀
                      {merah} NETWORKS MENU
                         [k] kembali




{biru}Input:{merah}~# {putih}""")
    if a == "1":
      check_input = 1
      os.system("clear")
      print(f"{merah}Wifi Hack")
      os.system("git clone https://github.com/derv82/wifite.git")
      print(f"{hijau}kembali dalam 3 detik")
      time.sleep(3)
      os.system("clear")
      net()
    elif a == "2":
        check_input = 1
        os.system("clear")
        print(f"{merah}Wifi Hacker")
        os.system("git clone https://github.com/esc0rtd3w/wifi-hacker.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        net()
    elif a == "3":
        check_input = 1
        os.system("clear")
        print(f"{merah}Wifi Hacking")
        os.system("git clone https://github.com/ankit0183/Wifi-Hacking.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        net()
    elif a == "4":
        check_input = 1
        os.system("clear")
        print(f"{merah}Kathara")
        os.system("git clone https://github.com/KatharaFramework/Kathara.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        net()
    elif a == "5":
        check_input = 1
        os.system("clear")
        print(f"{merah}React-Router")
        os.system("git clone https://github.com/remix-run/react-router.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        net()
    elif a == "6":
        check_input = 1
        os.system("clear")
        print(f"{merah}NetworkX")
        os.system("git clone https://github.com/networkx/networkx.git")
        print(f"{hijau}kembali dalam 3 detik")
        time.sleep(3)
        os.system("clear")
        net()
    elif a == "k" or a == "K":
        check_input = 1
        os.system("clear")
        jawab1()
    else:
        print(f"{merah}Ketik Dengan Benar")
        time.sleep(2.0)
        os.system("clear")
        net()
def back():
    a = input(f"""{merah}
Kembali Menu Awal Type {putih} Yes
""")
    if a == "yes" or a == "Yes" or a == "YES":
      check_input = 1
      os.system("clear")
      tanya1()
    else:
      print(f"{merah}Ketik Dengan Benar")
      time.sleep(2)
      os.system("clear")
      back()
def tanya1():
    a = input(f"""{merah} PILIH MENU DI BAWAH INI
{ungu} [1] Tools
{ungu} [2] Exit
{ungu} [3] AboutMe

{biru}Input:{merah}~# {putih}""")
    if a == "1":
      check_input = 1
      menuz()
    elif a == "2":
        check_input = 2
        rod2(f"""{merah}selamat tinggal""")
        sys.exit()
    elif a == "3":
        check_input = 1
        os.system("clear")
        rod(f"""{merah}
 █████╗ ██████╗  ██████╗ ██╗   ██╗████████╗
██╔══██╗██╔══██╗██╔═══██╗██║   ██║╚══██╔══╝
███████║██████╔╝██║   ██║██║   ██║   ██║
{putih}██╔══██║██╔══██╗██║   ██║██║   ██║   ██║
██║  ██║██████╔╝╚██████╔╝╚██████╔╝   ██║
╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚═════╝    ╚═╝ {kuning}ME


{merah}  WARNING! KAMI TIDAK BERTANGGUNG JAWAB ATAS PERILAKU ANDA
{biru}╔══════════════════════════════════════════════════════╗
{merah}  Coded By : {ungu}Destroyer                A
{merah}  MyTeacher: {ungu}Mikael                   B
{merah}  Helped Me: {ungu}Core                     O
{merah}  ContactMe: {ungu}+6288980820993           U
{merah}  Region   : {merah}Indo{putih}Nesia        T
{merah}            Thanks To Core And Mikael
{biru}╚══════════════════════════════════════════════════════╝""")
        back()
    else:
        rod2(f"""{merah}Ketik dengan benar""")
        tanya1()
def apikey():
    a = input(f"""{merah}

██╗      ██████╗  ██████╗ ██╗███╗   ██╗
██║     ██╔═══██╗██╔════╝ ██║████╗  ██║
██║     ██║   ██║██║  ███╗██║██╔██╗ ██║
{putih}██║     ██║   ██║██║   ██║██║██║╚██╗██║
███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║
╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝
                                       

{biru}[{merah}!{biru}]{ungu} SILAHKAN LOGIN DENGAN MENGGUNAKAN APIKEY!

{biru}[{hijau}?{biru}]{ungu} TOKEN WEB:{kuning} https://sfile.mobi/22Qm838P9q5

{biru}[{hijau}>{biru}]{putih} :  """)
    if a == "XyabDa190CaHKabAb9138ZbaIqO":
      check_input = 1
      time.sleep(6.0)
      print(f"{biru}[{hijau}✓{biru}]{ungu} TOKEN BENAR (✓)")
      time.sleep(3.0) 
      main()     
    else:
        time.sleep(6.0)
        print(f"{biru}[{merah}X{biru}]{ungu} TOKEN SALAH (X)")
        time.sleep(5.0)
        os.system("clear")
        apikey()
def jawab1():

    os.system("clear")
    print(f"""{merah}
               D E S T R O Y E R  T O O L S V 1 
                          .-==========
                         .-' +    =====
                        /___       ===
                           \_      |
_____________________________)    (______________________________
\___________               .'      `,              _____________/
   \__________`.     |||<   `.      .'   >|||     .'__________/
     \_________`._  |||  <   `-..-'   >  |||  _.'_________/
        \_________`-..|_  _ <      > _  _|..-'_________/
{putih}          \_________   |_|   /  \  |_|   _________/
                      .-\    /    \   /-.
      1.theme       _.'.- `._        _.' -.`._         8.VIRUS
      2.exit      .' .'  /  '``----''`  \  `. `.       9.spam OTP
      3.camera     /  .' .'.'/|..|\`.`. `.  \          10.deface
      4.password   `  /  / .'| |||| |`. \  \  '        11.CCTV
      5.IG         ::_.' .' /| || |\ `. `._::          12.EXPLOIT
      6.network        '``.' | | || | | `.''`          13,DEEPWEB MENU
      7.DDOS           .` .` | || | '. '.              14.SOCIAL ENGERING 
       /\                 `  | `' |  '                   /\ 
      \  /                                              \  /
       \/                     MENU                       \/""")
def menuz():
    jawab1()
    while(True):
        cnc = input(Fore.RED+"╔═══"+Fore.RED+"[""ROOT"+Fore.WHITE+"@"+Fore.WHITE+usernama+Fore.WHITE+"]"+Fore.RED+"\n╚══\x1b[38;2;0;255;189m> "+Fore.RED)
        if cnc == "camera" or cnc == "3" or cnc == "cam" or cnc == "CAMERA":
            check_input = 1
            os.system("clear")
            cam1()
        elif cnc == "social engering" or cnc == "14" or cnc == "SE" or cnc == "SOCIAL ENGERING":
            os.system("clear")
            track()
        elif cnc == "password" or cnc == "PASSWORD" or cnc == "PASS" or cnc == "pass" or cnc == "pw" or cnc == "4":
            os.system("clear")
            password()
        elif cnc == "OTP" or cnc == "spam otp" or cnc == "SPAM OTP" or cnc == "spam" or cnc == "9":
            os.system("clear")
            otp()
        elif cnc == "DDoS" or cnc == "DDOS" or cnc == "ddos" or cnc == "7":
            os.system("clear")
            ddos()
        elif cnc == "VIRUS" or cnc == "Vrus" or cnc == "virus" or cnc == "8":
            os.system("clear")
            virus()
        elif cnc == "network" or cnc == "NET" or cnc == "NETWORK" or cnc == "6":
            os.system("clear")
            net()
        elif cnc == "theme" or cnc == "1" or cnc == "THEME" or cnc == "Theme":
            os.system("clear")
            theme()
        elif cnc == "EXPLOIT" or cnc == "explot" or cnc == "Exploit" or cnc == "12":
            os.system("clear")
            exploit()
        elif cnc == "IG" or cnc == "ig" or cnc == "information gathering" or cnc == "5":
            os.system("clear")
            ig()
        elif cnc == "deface" or cnc == "DEFACE" or cnc == "Deface" or cnc == "10":
            os.system("clear")
            deface()
        elif cnc == "deep" or cnc == "deep web" or cnc == "DEEP WEB" or cnc == "13":
            os.system("clear")
            deep()
        elif cnc == "exit" or cnc == "2" or cnc == "EXIT" or cnc == "Exit":
            print("""{putih} ⸻⸻⸻⸻{kuning} Terima Kasih Sudah Mencoba Script Saya {putih}⸻⸻⸻⸻""")
            time.sleep(2)
            sys.exit()
        else:
           rod2(f"""{merah}Ketik Dengan Benar""")
           os.system("clear")
           jawab1()


        os.system("clear")
def main():

# Teks yang ingin Anda konversi menjadi ucapan
    text = "hello....welcome..to.toolsv1..by .destroyer"

# Inisialisasi mesin TTS
    engine = pyttsx3.init()

# Atur properti suara untuk suara laki-laki dalam bahasa Indonesia
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Gunakan suara laki-laki (index 0)
    engine.setProperty('lang', 'id')  # Atur bahasa menjadi bahasa Indonesia

# Mengucapkan teks
    engine.say(text)

# Tunggu hingga selesai berbicara
    engine.runAndWait()

    print(f"""{merah}

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡴⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                         ⢀⣠⣴⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀                                                       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⢀⣠⣤⣤⣤⣤⣴⣿⣿⣿⣿⣯⣤⣶⣶⣾⣿⣶⣶⣿⣿⣿⣿⣿⡿⠿⠟⠛⠉⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠉⠁⠈⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⠶⠶⠦⠄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⡿⠟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣟⣡⣤⣾⣿⣿⣿⣿⣿⣿⢏⠉⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⡻⢿⣿⣿⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠈⠻⡄⠁⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠈⠙⠻⣿⣆⠀⠀⠀⠀
⠀⠀⠀⠀⢰⣿⣿⣿⣿⡿⠛⠉⠉⠉⠛⠛⠛⠛⠋⠁⠀⠀⠀⠁⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠈⠙⢧⠀⠀⠀
⠀⠀⠀⠀⠀⠙⠿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠙⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⢹⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀⠈⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⢋⣩⡿⠿⠿⠟⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣄⣀⡀⠀⠀⠀⠀⠀⠐⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣾⣿⣿⣿⣿⣿⣿⣿⠻⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢰⣿⣿⣿⣿⣿⣿⣿⣿⡄⠙⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠠⣤⣀⠀⠀⠀⠠⣄⣀⣀⡉⢻⣿⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣦⣤⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀
⠀⢻⡟⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠛⠋⠉⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀
⠀⠀⠃⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠈⠉⠻⢿⣿⣿⣿⣷⡄⠀
⠀⠀⠀⠀⢸⣿⣿⡟⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⣿⣿⣿⣿⣿⣧⣀⣀⡄⠀⠀⠀⠀⠀⠀⠈⣿⡿⣿⣿⣷⠀
⠀⠀⠀⠀⢸⣿⡿⠁⠀⠀⠀⠙⠻⠿⣟⠻⢿⣿⣿⣿⣷⣦⡀⠀⠈⠻⢿⣿⣿⣭⣉⡉⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠸⣿⣿⡄
⠀⠀⠀⠀⣸⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣦⡀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁
⠀⠀⠀⠠⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡟⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀ ⠀ {ungu}Tools-DestroyerV1⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀


       ═══════════════════════════════════════════════════════════════════════
{biru}║ {hijau}Upload  : {kuning}14 maret{biru}                                   ║
{biru}║ {hijau}Date    : {kuning}{today}{biru}                                    ║
{biru}║ {hijau}Version : {kuning}1.2.2 {biru}                                     ║
{biru}║ {hijau}Telegram: {kuning}t.me/DestroyerLinuxPropaly46 {biru}              ║
{biru}║ {hijau}Github  : {kuning}https://github.com/destroyerLinuxPropaly{biru}   ║
{biru}║ {hijau}Inform  : {kuning}update by mikaelz        {biru}                  ║
{biru}╚══════════════════════════════════════════════════════╝ """)
    sys.stdout.write(f"         \x1b]2;tools status => OK | ver = 1.1.2 | private\x07")

    tanya1()



        



usernama = input(f"Masukkan nama anda: ")
apikey()







