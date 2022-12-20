import requests
import random
from colorama import Fore

def main():
  proxies = None
  use_proxy = input(Fore.RESET + Fore.MAGENTA + "[?] Use proxy (y/n): ")
  while True:
    #users = open("usernames.txt")
    #user = random.choice(users.read().splitlines())
    #users.close()
    user = ''.join((random.choice('abcdefghijklmnopqrstuvwxyz1234567890')) for x in range(3))
    if use_proxy.lower == 'y':
      proxie = open('proxies.txt', 'r').read().splitlines()
      prox = random.choice(proxie)
      proxies = {'http://': f'http://{prox}', 'https://': f'http://{prox}'}
    headers = {
      'authority': 'github.com',
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
      'accept-language': 'en-US,en;q=0.6',
      'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Brave";v="108"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'document',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-site': 'none',
      'sec-fetch-user': '?1',
      'sec-gpc': '1',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }
    r = requests.get(f'https://github.com/{user}', headers=headers, proxies=proxies)
    if r.status_code == 404:
      print(Fore.RESET + Fore.GREEN + f"[+] Available: {user}")
      with open("available.txt", "a") as f:
        f.write(user + "\n")

    if r.status_code == 200:
      print(Fore.RESET + Fore.RED + f"[-] Taken: {user}")

main()
