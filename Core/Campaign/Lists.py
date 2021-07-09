from Core.Support import Font
import os 

class List:
    
    @staticmethod
    def creator():
        name = input(
            Font.Color.GREEN + "\n[+]" +  Font.Color.WHITE + "CREATING A NEW VICTIM LIST INSERT A NAME WITHOUT'.txt'" +  Font.Color.GREEN + "\n\n[*TITANIUM*]" +  Font.Color.WHITE + "-->")
        nomefile = "Phishing/Vict_list/" + name + ".txt"
        f = open(nomefile, "w")
        f.close()
        print(
            Font.Color.WHITE + "\n[+]" +  Font.Color.GREEN + "FILE CREATED:" + nomefile +  Font.Color.WHITE + "[+]")
        inp = input(Font.Color.WHITE + "\nPRESS ENTER TO CONTINUE...")

    @staticmethod
    def modify():
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "LISTING LISTS" + Font.Color.GREEN + "[+]")
        path = "Phishing/Vict_list/"
        i = 1
        files = os.listdir(path)
        print("#########################")
        for f in files:
            convI = str(i) + ")"
            print( Font.Color.GREEN + "[+]" +  Font.Color.WHITE + "(" + convI + f +  Font.Color.GREEN)
            i = i + 1
        print("#########################")
        name = input(
            Font.Color.WHITE + "\n[+]" +  Font.Color.GREEN + "INSERT A LIST NAME WITHOUT'.txt'" +  Font.Color.WHITE + "[+]" +  Font.Color.GREEN + "\n\n[*TITANIUM*]" +  Font.Color.WHITE + "-->")
        nomefile = "Phishing/Vict_list/" + name + ".txt"
        if os.path.isfile(nomefile):
            os.remove(nomefile)
            f = open(nomefile, "w")
        else:
            f = open(nomefile, "w")
        f = open(nomefile, "a+")
        cont = str(input(
            Font.Color.WHITE + "\n[+]" +  Font.Color.GREEN + "INSERT AN EMAIL ADDRESS?(Y)YES(N)NO" +  Font.Color.WHITE + "[+]" +  Font.Color.GREEN + "\n\n[*TITANIUM*]" +  Font.Color.WHITE + "-->"))
        while cont == "y" or cont == "Y":
            email = input(
                Font.Color.GREEN + "\n[+]" +  Font.Color.WHITE + "INSERT THE EMAIL" +  Font.Color.GREEN + "[+]" +  Font.Color.GREEN + "\n\n[*TITANIUM*]" +  Font.Color.WHITE + "-->")
            f.write(email + "\n")
            print("\nEMAIL INSERTED CORRECTLY")
            cont = str(input(
                Font.Color.WHITE + "\n[+]" +  Font.Color.GREEN + "INSERT ANOTHER EMAIL ADDRESS?(Y)YES(N)NO" +  Font.Color.GREEN + "\n\n[*TITANIUM*]" +  Font.Color.WHITE + "-->"))
        else:
            f.close()
            print(
                Font.Color.WHITE + "\n[+]" +  Font.Color.GREEN + "FILE MODIFIED:" + nomefile +  Font.Color.WHITE + "[+]")
            inp = input( Font.Color.WHITE + "\nPRESS ENTER TO CONTINUE...")
