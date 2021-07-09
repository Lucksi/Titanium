import Titanium
from Core.Support import Font
import os


class Services:

    @staticmethod
    def banner():
        f = open("Banners/Service.txt","r")
        banner = f.read()
        f.close()
        os.system("cls" if os.name == "nt" else "clear")
        print(Font.Color.YELLOW + "**************************************************************")
        print(Font.Color.GREEN + banner)
        print(Font.Color.WHITE + "A SIMPLE SOCIAL ENGINEERING TOOL:)     CODED BY LUCKSI")
        print(
            Font.Color.YELLOW + "Instagram:lucks_022\nEMAIL:lukege287@gmail.com\nGIT-HUB:Lucksi\nWebsite:https://sosuke.altervista.org")
        print("**************************************************************")

    @staticmethod
    def start_server():
        os.system("service apache2 start")
        print("NETWORK-SERVICES ENABLED")
        inp = input("PRESS ENTER TO CONTINUE..")

    @staticmethod
    def restart_server():
        os.system("service apache2 restart")
        print("NETWORK-SERVICES RESTARTED")
        inp = input("PRESS ENTER TO CONTINUE...")

    @staticmethod
    def stop_server():
        os.system("service apache2 stop")
        print("NETWORK-SERVICES DISABLED")
        inp = input("PRESS ENTER TO CONTINUE...")

    @staticmethod
    def start_ngrok():
        os.system("Tunnel/./ngrok http 80")

    @staticmethod
    def main():
        try:
            while True:
                Services.banner()
                attiva = int(input(
                    Font.Color.GREEN + "[*INSERT AN OPTION:*]" + Font.Color.WHITE + "\n(1)ACTIVATE-NETWORK-SERVICE\n(2)RESTART-NETWORK-SERVICE\n(3)DISABLE-NETWORK-SERVICE\n(4)ACTIVATE-NGROK-SERVICE\n(5)MAIN-MENU" + Font.Color.GREEN + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->"))
                if attiva == 1:
                    Services.start_server()
                elif attiva == 2:
                    Services.restart_server()
                elif attiva == 3:
                    Services.stop_server()
                elif attiva == 4:
                    Services.start_ngrok()
                elif attiva == 5:
                    inp = input("PRESS ENTER TO CONTINUE...")
                    Titanium.Main()
                else:
                    out = input("OPS LOOKS LIKE YOU PRESSED AN INVALID OPTION PRESS ENTER TO CONTINUE")
        except KeyboardInterrupt:
            inp = input(
                Font.Color.RED + "\n[!]" + Font.Color.WHITE + "LOOKS LIKE YOU HIT CTRL'C YOU WILL BE REDIRECT TO MAIN-MENU ARE YOU SURE (YES)(NO)" + Font.Color.RED + "[!]\n")
            Titanium.Main()
