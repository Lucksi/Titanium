#------------------------AUTHOR:Lucksi------------------------#

#-------------------------------------------------------------#
import os
from Core import phishing
from Core import campaign
from Core import services
from Core import config
from Core.Support import Font
from time import sleep
import socket

Network = socket.gethostbyname(socket.gethostname())

def update():
    print(Font.Color.WHITE + "\n[+]" + Font.Color.GREEN + "CHECKING IF THERE IS AN INTERNET CONNECTION")
    sleep(1)
    if Network != "127.0.0.1":
        ris = int(input(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "INTERNET FOUND ARE YOU SURE TO UPDATE TITANIUM(1)YES(2)NO" + Font.Color.GREEN + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->"))
        if ris == 1 :
            os.system("Core/./update.sh")
            exit()
        elif ris == 2 :
            inp = input(Font.Color.WHITE + "\nPRESS ENTER TO CONTINUE")
        else :
            inp = input(Font.Color.WHITE + "\nPRESS ENTER TO CONTINUE")
    else:
        inp = input(Font.Color.RED + "[!]" + Font.Color.WHITE + "SORRY BUT LOOKS LIKE YOU HAVENT AN INTERNET CONNECTION SO IT IS IMPOSSIBILE TO UPDATE\nPRESS ENTER TO CONTINUE")


def agree_banner():
    f = open("Banners/Main.txt", "r")
    banner = f.read()
    f.close()
    print(Font.Color.GREEN + banner)


def check_root():
    if os.getuid() != 0:
        os.system("cls" if os.name == "nt" else "clear")
        agree_banner()
        print(Font.Color.RED + "JUST A SIMPLE SOCIAL ENGIGNERING TOOL:)      CODED BY LUCKSI\n")
        print("YOU MUST EXECUTE THIS PROGRAM AS ROOT TRY TO USE IT WITH SUDO:)")
        exit()
    else:
        os.system("cls" if os.name == "nt" else "clear")


def banner(r):
    f = open("Version/Version.txt", "r", newline=None)
    for line in f:
        r = line.replace("\n", "")
    version = f.read() + r
    f.close()
    os.system("cls" if os.name == "nt" else "clear")
    print(Font.Color.YELLOW + "***************************************************************")
    agree_banner()
    print(Font.Color.WHITE + "JUST A SIMPLE SOCIAL ENGIGNERING TOOL:)    CODED BY LUCKSI\n")
    print(Font.Color.WHITE + "[+]" + Font.Color.GREEN + "VERSION:" + version)
    print(
        Font.Color.YELLOW + "Instagram:lucks_022\nEMAIL:lukege287@gmail.com\nGIT-HUB:Lucksi\nWebsite:https://sosuke.altervista.org")
    print("***************************************************************")


def Main():
    while True:
        banner(r=True)
        try:
            scel = input(
                Font.Color.GREEN + "[*INSERT AN OPTION:*]" + Font.Color.WHITE + "\n(A)PHISHING-MODE(AVAIABLE)\n(B)SERVICES-MODE(AVAIABLE)\n(C)CAMPAIGN-MODE(AVAIABLE)\n(D)CONFIGURATION-FILE\n(E)UPDATE\n(F)EXIT" + Font.Color.GREEN + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->")
            # PHISHING #
            if scel == "a" or scel == "A":
                phishing.Phishing.main()
            # SERVICES-MODE #
            elif scel == "b" or scel == "B":
                services.Services.main()
            # MAILER-MODE #
            elif scel == "c" or scel == "C":
                campaign.Campaign.main()
            # TITANIUM-SERVER #
            elif scel == "d" or scel == "D":
                config.Config.main()          
            # CONFIGURATION-MODE #
            elif scel == "e" or scel == "E":
                os.system("Core/./update.sh")
            # UPDATE #
            elif scel == "f" or scel == "F":
                print(Font.Color.GREEN + "\nTHANKS FOR HAVE USED TITANIUM,HAVE A NICE DAY:)")
                exit()
        except ValueError:
            print(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "OPS LOOKS LIKE YOU PRESS AN INVALID OPTION")   
            inp = input("PRESS ENTER TO CONTINUE...")
            Main()

def agree():
    check_root()
    agree_banner()
    agreement = str(input(
        Font.Color.BLUE + "THIS TOOL DOESN'T PROMOTE ANT TYPE OF ILLEGAL ACTIVITY ITS MADE ONLY FOR EDUCATIONAL PURPOSE AND TESTING,\nI DO NOT TAKE ANY RESPONSABILITY FOR ANY DAMAGE YOU WILL CAUSE.BY USING THIS TOOL YOU ACCEPT THIS CONDITION\nAND REMEMBER WHITH GREAT POWERS COMES GREAT RESPONSBILITES:)" + Font.Color.RED + "\nYES NO" + Font.Color.GREEN + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->"))
    if agreement == "yes" or agree == "YES":
        print(Font.Color.WHITE + "\nTHANK YOU GOOD HACKING:)")
        inp = input("\nPRESS ENTER TO USE TITANIUM")
        os.system("cls" if os.name == "nt" else "clear")
    elif agreement == "no" or agree == "NO":
        print(Font.Color.RED + "YOU MUST ACCEPT THE AGREEMENT TO RUN THIS SCRIPT")
        exit()
    else:
        exit()


if __name__ == "__main__":

    agree()
    try:
        Main()
    except KeyboardInterrupt:
        print(
            Font.Color.RED + "\n[!]" + Font.Color.WHITE + "LOOKS LIKE YOU PRESSED CTRL'C EXIT..." + Font.Color.RED + "[!]")
        exit()
