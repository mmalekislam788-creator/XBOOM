import os
import time

def banner():
    os.system('clear')
    print("========================================")
    print("        WELCOME TO X-BOOM TOOL          ")
    print("     Created by: mmalekislam788         ")
    print("========================================")

def main():
    banner()
    print("\n[1] SMS Bomber (Testing Mode)")
    print("[2] Exit")
    
    choice = input("\nSelect an option: ")
    
    if choice == '1':
        number = input("Enter Phone Number: ")
        amount = input("Enter SMS Amount: ")
        print(f"\n[+] Starting attack on {number}...")
        for i in range(int(amount)):
            print(f"[!] SMS {i+1} sent successfully!")
            time.sleep(1)
        print("\n[+] Attack Finished!")
    else:
        print("Exiting...")

main()
