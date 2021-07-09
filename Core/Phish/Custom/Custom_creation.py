from Core.Support import Font
import os
import time
from time import sleep


def main():
    print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "CREATION CUSTOM WEB TEMPLATE" + Font.Color.GREEN + "[+]")
    init = input(
        Font.Color.WHITE + "\nINSERT THE NAME OF YOUR  WEB TEMPLATE" + Font.Color.GREEN + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->")

    print(
        Font.Color.WHITE + "\n[+]" + Font.Color.GREEN + "CREATION OF YOUR CUSTOM TEMPLATE FOLDER" + Font.Color.WHITE + "[+]")
    time.sleep(3)
    fold = init
    cfold = os.getcwd() + "/Server/CUSTOM/" + fold
    os.system("mkdir " + cfold)
    name = cfold + "/index.php"
    f = open(name, "a")
    code = input(
            Font.Color.WHITE + "INSERT THE CODE INSERT 'TITANIUM' WHEN YOU FINISH(LEAVE THE FIRST LINE EMPTY:))" +  Font.Color.GREEN + "\n\n[*TITANIUM*]" +  Font.Color.WHITE + "-->")
    while code != "TITANIUM":
            code = input(Font.Color.GREEN + "\n[*NEXT LINE*]" + Font.Color.WHITE + "-->")
            f.write(code + "\n")
    f.close()
    
    f = open(name, "r+")
    code = f.read()
    f.close()
    deleting = "TITANIUM"
    repleacing = ""
    code2 = code.replace(deleting,repleacing)
    f = open(name, "w")
    f.write(code2)
    f.close()
    
    print(
            Font.Color.WHITE + "\n[+]" + Font.Color.GREEN + "FILE CREATED/MODIFIED:" + name + Font.Color.WHITE + "[+]")
    sc = int(input(
            "\n[+]" + Font.Color.WHITE + "WOULD YOU LIKE TO CREATE ANOTHER FILE?(1)YES(2)NO" + Font.Color.GREEN + "[+]" + Font.Color.GREEN + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->"))
    while sc == 1:
            fil = str(input(
            "\n[+]" + Font.Color.WHITE + "INSERT THE NAME OF THE FILE" + Font.Color.GREEN + "[+]" + Font.Color.GREEN + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->"))
            name = cfold + "/" + fil
            f = open(name, "w")
            f.close()
            f = open(name, "a")
            code = input(
                    Font.Color.WHITE + "INSERT THE CODE INSERT 'TITANIUM' WHEN YOU FINISH(LEAVE THE FIRST LINE EMPTY:))" +  Font.Color.GREEN + "\n\n[*TITANIUM*]" +  Font.Color.WHITE + "-->")
            while code != "TITANIUM":
                    code = input(Font.Color.GREEN + "\n[*NEXT LINE*]" + Font.Color.WHITE + "-->")
                    f.write(code + "\n")
            f.close()
            f = open(name, "r+")
            code = f.read()
            f.close()
            deleting = "TITANIUM"
            repleacing = ""
            code1 = code.replace(deleting,repleacing)
            f = open(name, "w")
            f.write(code1)
            f.close()
            print(
                 Font.Color.WHITE + "[+]" + Font.Color.GREEN + "FILE CREATED/MODIFIED:" + name + Font.Color.WHITE + "[+]")
            sc = int(input(
                "\n[+]" + Font.Color.WHITE + "WOULD YOU LIKE TO CREATE ANOTHER FILE?(1)YES(2)NO" + Font.Color.GREEN + "[+]" + Font.Color.GREEN + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->"))
    inp = input(Font.Color.WHITE + "\nPRESS ENTER TO CONTINUE...")