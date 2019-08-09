#######################
####Main IMPORTS ######
#######################

import os
import math
import subprocess

###################
### MAIN MENU #####
###################
os.system("clear");
os.system("toilet --gay OS-X UPGRADED");
print("1.OS-UBUNTU");
print("2.OS-KALI");
print("3.CREDITS");
print("4.EXIT");
#######################
### MAIN FUNCTION #####
#######################

selection=int(input("ENTER CHOICE :"))

if selection ==1:
  os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh && bash ubuntu.sh");

if selection ==2:
  os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh");

if selection ==3:
   print("CODED BY ANUBHAB , MAINTEND BY ANUBHAB , REPOSTIORY BY ANLINUX ,PATCH BY ANUBHAB, primarily maintend by anubhab");

if selection ==4:
    exit();
