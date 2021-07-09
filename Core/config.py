import Titanium
from Core.Support import Font
import os
import getpass
from configparser import ConfigParser

dest = "Configuration"
nomefile = "Configuration.ini"

class Config:

    @staticmethod
    def banner():
        os.system('cls' if os.name == 'nt' else 'clear')
        f = open("Banners/Config.txt")
        banner = f.read()
        f.close()
        print(
            Font.Color.YELLOW + "****************************************************************")
        print(Font.Color.GREEN + banner)
        print(Font.Color.WHITE + "A SIMPLE SOCIAL ENGINEERING TOOL:)    CODED BY LUCKSI")
        print(
            Font.Color.YELLOW + "Instagram:lucks_022\nEMAIL:lukege287@gmail.com\nGIT-HUB:Lucksi\nWebsite:https://sosuke.altervista.org")
        print("****************************************************************")

    @staticmethod
    def modify_recipient():
        alert = int(input(
            Font.Color.RED + "\n[!]" + Font.Color.WHITE + "ARE YOU SURE TO MODIFY YOUR RECIPIENT EMAIL?(1)YES(2)NO" + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if alert == 1:
            os.chdir(dest)
            if os.path.isfile(nomefile):
                Parser = ConfigParser()
                Parser.read(nomefile)
                recipient = str(input(
                    Font.Color.WHITE + "\nINSERT THE EMAIL-RECIPIENT" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                while recipient == "":
                    recipient = str(input(
                        Font.Color.RED + "\n[!]" + Font.Color.WHITE + "INSERT AN EMAIL" + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                else:
                    Parser.set("Smtp","Email",recipient)
                    with open(nomefile, 'w') as configfile:
                        Parser.write(configfile)
                    print("\nEMAIL CHANGED SUCCESSFULLY")
                    out = input("\nPRESS ENTER TO EXIT")
                    os.chdir("../")
            else:
                inp = input(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "FILE NOT FOUND\n\nPRESS ENTER TO CONTINUE")
                os.chdir("../")

    @staticmethod
    def modify_password():
        alert = int(input(
            Font.Color.RED + "\n[!]" + Font.Color.WHITE + "ARE YOU SURE TO MODIFY YOUR RECIPIENT-EMAIL-PASSWORD?(1)YES(2)NO" + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if alert == 1:
            os.chdir(dest)
            if os.path.isfile(nomefile):
                Parser = ConfigParser()
                Parser.read(nomefile)
                passw = getpass.getpass(
                    Font.Color.WHITE + "\nINSERT THE PASSWORD-RECIPIENT" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->")
                while passw == "":
                    passw = getpass.getpass(
                        Font.Color.RED + "\n[!]" + Font.Color.WHITE + "INSERT A PASSWORD" + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->")
                else:
                    Parser.set("Smtp","Password",passw)
                    with open(nomefile, 'w') as configfile:
                        Parser.write(configfile)
                    print("\nPASSWORD CHANGED SUCCESSFULLY")
                    out = input("\nPRESS ENTER TO EXIT")
                    os.chdir("../")
            else:
                inp = input(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "FILE NOT FOUND\n\nPRESS ENTER TO CONTINUE")
                os.chdir("../")

    @staticmethod
    def modify_destination():
        alert = int(input(
            Font.Color.RED + "\n[!]" + Font.Color.WHITE + "ARE YOU SURE TO MODIFY YOUR DESTINATION-EMAIL?(1)YES(2)NO" + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if alert == 1:
            os.chdir(dest)
            if os.path.isfile(nomefile):
                Parser = ConfigParser()
                Parser.read(nomefile)
                destination = str(input(
                    Font.Color.WHITE + "\nINSERT YOUR DESTINATION-MAIL" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                while destination == "":
                   destination = str(input(
                    Font.Color.WHITE + "\nINSERT YOUR DESTINATION-MAIL" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                else:
                    Parser.set("Smtp","Destination",destination)
                    with open(nomefile, 'w') as configfile:
                        Parser.write(configfile)
                    print("\nEMAIL CHANGED SUCCESSFULLY")
                    out = input("\nPRESS ENTER TO EXIT")
                    os.chdir("../")
            else:
                inp = input(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "FILE NOT FOUND\n\nPRESS ENTER TO CONTINUE")
                os.chdir("../")

    @staticmethod
    def modify_port():
        alert = int(input(
            Font.Color.RED + "\n[!]" + Font.Color.WHITE + "ARE YOU SURE TO MODIFY YOUR SERVER-PORT?(1)YES(2)NO" + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if alert == 1:
            os.chdir(dest)
            if os.path.isfile(nomefile):
                Parser = ConfigParser()
                Parser.read(nomefile)
                port = str(input(
                    Font.Color.WHITE + "\nINSERT YOUR SERVER-PORT" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                while port == "":
                   port = str(input(
                    Font.Color.WHITE + "\nINSERT YOUR SERVER-PORT" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                else:
                    Parser.set("Smtp","Destination",port)
                    with open(nomefile, 'w') as configfile:
                        Parser.write(configfile)
                    print("\nPORT CHANGED SUCCESSFULLY")
                    out = input("\nPRESS ENTER TO EXIT")
                    os.chdir("../")
            else:
                inp = input(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "FILE NOT FOUND\n\nPRESS ENTER TO CONTINUE")
                os.chdir("../")

    @staticmethod
    def modify_server():
        alert = int(input(
            Font.Color.RED + "\n[!]" + Font.Color.WHITE + "ARE YOU SURE TO MODIFY YOUR SMTP-SERVER?(1)YES(2)NO" + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if alert == 1:
            os.chdir(dest)
            if os.path.isfile:
                Parser = ConfigParser()
                Parser.read(nomefile)
                server = str(input(
                        Font.Color.WHITE + "\nINSERT YOUR SMTP-SERVER" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                while server == "":
                    server = str(input(
                    Font.Color.WHITE + "\nINSERT YOUR SMTP-SERVER" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                else:
                    Parser.set("Smtp","Server",server)
                    with open(nomefile, 'w') as configfile:
                        Parser.write(configfile)
                    print("\nSERVER CHANGED SUCCESSFULLY")
                    out = input("\nPRESS ENTER TO EXIT")
                    os.chdir("../")
            else:
                inp = input(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "FILE NOT FOUND\n\nPRESS ENTER TO CONTINUE")
                os.chdir("../")
    @staticmethod
    def modify_path():
        alert = int(input(
            Font.Color.RED + "\n[!]" + Font.Color.WHITE + "ARE YOU SURE TO MODIFY YOUR UPDATE-PATH?(1)YES(2)NO" + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if alert == 1:
            os.chdir(dest)
            if os.path.isfile:
                Parser = ConfigParser()
                Parser.read(nomefile)
                path = str(input(
                        Font.Color.WHITE + "\nINSERT YOUR UPDATE-PATH" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                while path == "":
                    path = str(input(
                        Font.Color.WHITE + "\nINSERT YOUR UPDATE-PATH" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                else:
                    Parser.set("Settings","Path",path)
                    with open(nomefile, 'w') as configfile:
                        Parser.write(configfile)
                    print("\nEMAIL CHANGED SUCCESSFULLY")
                    out = input("\nPRESS ENTER TO EXIT")
                    os.chdir("../")
            else:
                inp = input(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "FILE NOT FOUND\n\nPRESS ENTER TO CONTINUE")
                os.chdir("../")

    @staticmethod
    def modify_update_pass():
        alert = int(input(
            Font.Color.RED + "\n[!]" + Font.Color.WHITE + "ARE YOU SURE TO MODIFY YOUR UPDATE-PASSWORD?(1)YES(2)NO" + Font.Color.RED + "[!]" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
        if alert == 1:
            os.chdir(dest)
            if os.path.isfile :
                Parser = ConfigParser()
                Parser.read(nomefile)
                passw = getpass.getpass(
                        Font.Color.WHITE + "\nINSERT YOUR DESTINATION-MAIL" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->")
                while passw == "":
                    destination = str(input(
                        Font.Color.WHITE + "\nINSERT YOUR DESTINATION-MAIL" + Font.Color.GREEN + "\n\n[#MR.HOLMES#]" + Font.Color.WHITE + "-->"))
                else:
                    Parser.set("Settings","Password",passw)
                    with open(nomefile, 'w') as configfile:
                        Parser.write(configfile)
                        print("\nEMAIL CHANGED SUCCESSFULLY")
                        out = input("\nPRESS ENTER TO EXIT")
                        os.chdir("../")
            else:
                inp = input(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "FILE NOT FOUND\n\nPRESS ENTER TO CONTINUE")
                os.chdir("../")

   
    @staticmethod
    def main():
        while True:
            try:
                Config.banner()
                mod = int(input(
                    Font.Color.GREEN + "[+INSERT AN OPTION:*]" + Font.Color.WHITE + "\n(1)MODIFY-DESTINATION-MAIL\n(2)MODIFY-RECIPIENT-EMAIL\n(3)MODIFY-RECIPIENT-PASSWORD\n(4)MODIFY-SMTP-SERVER\n(5)MODIFY-SMTP-SERVER-PORT\n(6)MODIFY-UPDATE-PATH\n(7)MODIFY-UPDATE-PASSWORD\n(8)MAIN-MENU" + Font.Color.GREEN + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->"))
                if mod == 1:
                    Config.modify_destination()
                elif mod == 2:
                    Config.modify_recipient()
                elif mod == 3:
                    Config.modify_password()
                elif mod == 4:
                    Config.modify_server()
                elif mod == 5:
                    Config.modify_port()
                elif mod == 6:
                    Config.modify_path()
                elif mod == 7:
                    Config.modify_update_pass()
                elif mod == 8:
                    out = input("PRESS ENTER TO EXIT")
                    Titanium.Main()
                else:
                    out = input("OPS LOOKS LIKE YOU PRESSED AN INVALID OPTION PRESS ENTER TO CONTINUE")
                    Config.main()
            except KeyboardInterrupt:
                inp = input(
                    Font.Color.RED + "\n[!]" + Font.Color.WHITE + "LOOKS LIKE YOU HIT CTRL'C YOU WILL BE REDIRECT TO MAIN-MENU PRESS ENTER TO CONTINUE" + Font.Color.RED + "[!]\n")
                Titanium.Main()
