import os
import time

# BANNER
print("\n*******************************")
print("*     Log Managment System    *")
print("*                             *")
print("*     v.1 | @alperen_ae       *")
print("*                             *")
print("*******************************\n")

print("1- Apache access.log")
print("2- Nginx access.log ")
print("3- SSH access.log ")
contr = input("\nChoise Option: ")

if contr == "1":
  print("\n[+] For Stop ctrl + c or z")
  time.sleep(3)
  show_log = True
  while show_log:
    os.system("cat /var/log/apache2/access.log")
    time.sleep(10)

elif contr == "2":
    print("\n[+] For Stop ctrl + c or z")
    time.sleep(3)
    show_log = True
    while show_log:
      os.system("cat /var/log/nginx/access.log")
      time.sleep(10)



elif contr == "3":
    print("\n[+] For Stop ctrl + c or z")
    time.sleep(3)
    show_log = True
    while show_log:
      os.system("cat /var/log/auth.log")
      time.sleep(10)
