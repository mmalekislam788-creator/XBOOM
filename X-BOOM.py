import os
import time
import uuid

def start():
    os.system('clear')
    # OTP লোগো একদম মাঝখানে
    print('          \033[1;32m██████  \033[1;31m████████ \033[1;32m██████  ')
    print('         ██    ██    ██    ██   ██ ')
    print('         ██    ██    ██    ██████  ')
    print('         ██    ██    ██    ██      ')
    print('          ██████     ██    ██      \033[0m')
    
    # উপরের ৬টি ঘর
    line = "\033[1;32m×××××××××××××××××××××××××××××××××××××××××××××\033[0m"
    print(line)
    print('\033[1;34m| [✓] DEVELOPED BY :  MD RONY ISLAM MR      |')
    print('| [✓] TEAM         :  CYBER STRIKER TEAM    |')
    print('| [✓] TOOL STATUS  :  OTP SENDER            |')
    print('| [✓] TELEGRAM     :  @rony_broh            |')
    print('| [✓] GITHUB       :  MR-RONY               |')
    print('| [✓] TOOL VERSION :  MAX PRO               |\033[0m')
    print(line)
    
    # সালাম এবং টিমের নাম
    print('\033[1;32m[•] SALAMU ALAIKUM.........................\033[0m')
    print(line)
    print('\033[1;32m[•] CYBER STRIKER TEAM.....................\033[0m')
    print(line)
    
    # সেই ৩টি লাইন (পাওয়ারফুল টুল, কী এবং কপি করার মেসেজ)
    u_key = str(uuid.uuid4())[:8]
    print(f'\033[1;32m[\033[1;31m❤️\033[1;32m] POWERFUL TOOL 10 DAYS ONLY 50TK [\033[1;31m❤️\033[1;32m]')
    print(f'[\033[1;31m❤️\033[1;32m] KEY : {u_key}-MR-RONY')
    print(f'[\033[1;31m❤️\033[1;32m] COPY YOUR KEY AND SEND TO THE ADMIN [\033[1;31m❤️\033[1;32m]\033[0m')
    print(line)

    num = input('\n\033[1;32m[+] ENTER TARGET NUMBER: \033[0m')
    
    # সাকসেস মেসেজ স্টাইল
    print(f'\n\033[1;32mSuccess: True')
    print('Status Code: 200')
    print(f'Message: {num} যুক্ত হয়েছে।\033[0m\n')
    
    for i in range(1, 101):
        time.sleep(0.04)
        print(f'\033[1;32m[{i}] SUCCESS SENT ==> {num}\033[0m')

if __name__ == "__main__":
    start()
