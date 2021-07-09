import Titanium
import os
from Core.Support import Font
from Core.Campaign import Lists
from Core.Campaign import Spammer
from Core.Campaign import Template


class Campaign:

    @staticmethod
    def banner():
        os.system("cls" if os.name == "nt" else "clear")
        f = open("Banners/Campaign.txt", "r")
        banner = f.read()
        f.close()
        print(Font.Color.YELLOW + "****************************************************************")
        print(Font.Color.GREEN + banner)
        print(Font.Color.WHITE + "JUST A SIMPLE SOCIAL ENGIGNERING TOOL:)     CODED BY LUCKSI")
        print(
            Font.Color.YELLOW + "Instagram:lucks_022\nEMAIL:lukege287@gmail.com\nGIT-HUB:Lucksi\nWebsite:https://sosuke.altervista.org")
        print("*****************************************************************")

    @staticmethod
    def main():
        try:
            Campaign.banner()
            mod = int(input(
                Font.Color.GREEN + "[+INSERT AN OPTION:*]" + Font.Color.WHITE + "\n(1)START-EMAIL-SPAMMER\n(2)TEMPLATE-CREATION\n(3)PHISHING-CAMPAIGN\n(4)CREATING-VICTIM-LIST\n(5)MODIFING-VICTIM-LIST\n(6)MAIN-MENU" + Font.Color.GREEN + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->"))
            if mod == 1:
                Spammer.Spammer.main()
            elif mod == 2:
                Template.Template.creator()
            elif mod == 3:
                Template.Template.custom()
            elif mod == 4:
                Lists.List.creator()
            elif mod == 5:
                Lists.List.modify()
            elif mod == 6:
                inp = input("PRESS ENTER TO CONTINUE...")
                Titanium.Main()
            else:
                out = input("OPS LOOKS LIKE YOU PRESSED AN INVALID OPTION PRESS ENTER TO CONTINUE")
        except KeyboardInterrupt:
            inp = input(
                Font.Color.RED + "\n[!]" + Font.Color.WHITE + "LOOKS LIKE YOU HIT CTRL'C YOU WILL BE REDIRECT TO MAIN-MENU" + Font.Color.RED + "[!]\n")
            Titanium.Main()