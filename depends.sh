#!/system/bin/sh
#! copyright anubhab

####################################
##installing Dependencies For OS-X##
####################################
#colors
red='\033[1;31m'
yellow='\033[1;33m'
blue='\033[1;34m'
#main
echo "$red [*] Fixing permissions of termux bin"
chmod +x /data/data/com.termux/files/usr/bin
echo "$blue [*] Updating Apt Cache"
apt-get update -y && apt-get upgrade -y
echo "$blue [*] Installing Dependencies"
apt-get install figlet -y && apt-get install python -y
echo "$red [*] Fixing Permission Of OS-X SCRIPT"
chmod +x main_x.py
echo "$blue All Dependencies Installed And Srcipt is Usable Just Start it with python main_x.py"
