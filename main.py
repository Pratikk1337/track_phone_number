import phonenumbers
import time
import os
from phonenumbers import geocoder
from phonenumbers import carrier

os.system("cls||clear & mode 60,20 & title Phone Number Info Tool")
def menu():
    print(f'''
              \u001b[38;5;45m╔═╗╦ ╦╔═╗╔╗╔╔═╗  ╦╔╗╔╔═╗╔═╗
              \u001b[38;5;51m╠═╝╠═╣║ ║║║║║╣   ║║║║╠╣ ║ ║
              \u001b[38;5;87m╩  ╩ ╩╚═╝╝╚╝╚═╝  ╩╝╚╝╚  ╚═╝
            ''')
menu()

number = input(f"\u001b[38;5;45m[\033[37m√\u001b[38;5;45m]\u001b[38;5;45m\033[37m Enter Phone No.: ")
print(f"\u001b[38;5;45m[\033[37m√\u001b[38;5;45m]\u001b[38;5;45m\033[37m Getting Info, Please Wait..")
time.sleep(2)
os.system("cls||clear & mode 60,20 & title Phone Number Info Tool")
menu()
ch_nmber = phonenumbers.parse(number, "CH")
print(f"\u001b[38;5;45m[\033[37m√\u001b[38;5;45m]\u001b[38;5;45m\033[37m Country: " + geocoder.description_for_number(ch_nmber, "en") + "\n")

service_nmber = phonenumbers.parse(number, "RO")
print(f"\u001b[38;5;45m[\033[37m√\u001b[38;5;45m]\u001b[38;5;45m\033[37m ISP: " + carrier.name_for_number(service_nmber, "en") + "\n")

input()