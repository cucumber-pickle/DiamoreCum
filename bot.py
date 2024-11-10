import requests
import json
import os
from colorama import *
from datetime import datetime, timedelta
import time
from platform import system as s_name
from os import system as sys
import random
from core.helper import get_headers, countdown_timer, extract_user_data, config


class Diamore:
    def __init__(self) -> None:
        self.session = requests.Session()


    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{message}",
            flush=True
        )

    def set_proxy(self, proxy):
        self.session.proxies = {
            "http": proxy,
            "https": proxy,
        }
        if '@' in proxy:
            host_port = proxy.split('@')[-1]
        else:
            host_port = proxy.split('//')[-1]
        return host_port

    def welcome(self):
        banner = f"""{Fore.GREEN}
 ██████  ██    ██   ██████  ██    ██  ███    ███  ██████   ███████  ██████  
██       ██    ██  ██       ██    ██  ████  ████  ██   ██  ██       ██   ██ 
██       ██    ██  ██       ██    ██  ██ ████ ██  ██████   █████    ██████  
██       ██    ██  ██       ██    ██  ██  ██  ██  ██   ██  ██       ██   ██ 
 ██████   ██████    ██████   ██████   ██      ██  ██████   ███████  ██   ██     
                                            """
        print(Fore.GREEN + Style.BRIGHT + banner + Style.RESET_ALL)
        print(Fore.GREEN + f" Diamore bot")
        print(Fore.RED + f" FREE TO USE = Join us on {Fore.GREEN}t.me/cucumber_scripts")
        print(Fore.YELLOW + f" before start please '{Fore.GREEN}git pull{Fore.YELLOW}' to update bot")
        print(f"{Fore.WHITE}~" * 60)

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
        
    def user_visit(self, query: str):
        url = "https://diamore-propd.smart-ui.pro/user/visit"
        self.headers.update({
            'Content-Type': 'application/json',
            'Content-Length': '0',
            'Authorization': f'Token {query}'
        })

        response = self.session.post(url, headers=self.headers)
        if response.status_code == 201:
            result = response.json()
            if result["message"] == "ok":
                return result
            else:
                return None
        else:
            return None
        
    def user_info(self, query: str):
        url = "https://diamore-propd.smart-ui.pro/user"
        self.headers.update({
            'Content-Type': 'application/json',
            'Content-Length': '0',
            'Authorization': f'Token {query}'
        })

        response = self.session.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    
    def daily(self, query: str):
        url = "https://diamore-propd.smart-ui.pro/daily/rewards"
        self.headers.update({
            'Content-Type': 'application/json',
            'Content-Length': '0',
            'Authorization': f'Token {query}'
        })

        response = self.session.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    
    def claim_daily(self, query: str):
        url = "https://diamore-propd.smart-ui.pro/daily/claim"
        self.headers.update({
            'Content-Type': 'application/json',
            'Content-Length': '0',
            'Authorization': f'Token {query}'
        })

        response = self.session.post(url, headers=self.headers)
        if response.status_code == 201:
            result = response.json()
            if result["message"] == "ok":
                return result
            else:
                return None
        else:
            return None
    
    def refferal(self, query: str):
        url = "https://diamore-propd.smart-ui.pro/referral/recruits/"
        self.headers.update({
            'Content-Type': 'application/json',
            'Content-Length': '0',
            'Authorization': f'Token {query}'
        })

        response = self.session.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    
    def claim_refferal(self, query: str):
        url = "https://diamore-propd.smart-ui.pro/referral/claim"
        self.headers.update({
            'Content-Type': 'application/json',
            'Content-Length': '0',
            'Authorization': f'Token {query}'
        })

        response = self.session.post(url, headers=self.headers)
        if response.status_code == 201:
            result = response.json()
            if result["message"] == "Bonuses claimed":
                return result
            else:
                return None
        else:
            return None
    
    def taps(self, query: str, point: str):
        url = "https://diamore-propd.smart-ui.pro/taps/claim"
        data = json.dumps({ 'amount': str(point) })
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Token {query}'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        if response.status_code == 201:
            result = response.json()
            if result["message"] == "Taps claimed":
                return result
            else:
                return None
        else:
            return None
    
    def ads(self, query: str):
        url = "https://diamore-propd.smart-ui.pro/ads"
        self.headers.update({
            'Content-Type': 'application/json',
            'Content-Length': '0',
            'Authorization': f'Token {query}'
        })

        response = self.session.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    
    def watch_ads(self, query: str):
        url = "https://diamore-propd.smart-ui.pro/ads/watch"
        data = json.dumps({ 'type': 'adsgram' })
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Token {query}'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        if response.status_code == 201:
            result = response.json()
            if result["message"] == "Ad bonus applied!":
                return result
            else:
                return None
        else:
            return None
    
    def quests(self, query: str):
        url = "https://diamore-propd.smart-ui.pro/quests"
        self.headers.update({
            'Content-Type': 'application/json',
            'Content-Length': '0',
            'Authorization': f'Token {query}'
        })

        response = self.session.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    
    def complete_quests(self, query: str, quest_name: str, reward: str, reward_icon: str, retries=3, delay=2):
        url = "https://diamore-propd.smart-ui.pro/quests/finish"
        data = json.dumps({ 'questName': quest_name })
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Token {query}'
        })

        for attempt in range(1, retries + 1):
            try:
                response = self.session.post(url, headers=self.headers, data=data)

                if response.status_code == 504:
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}[ HTTP ERROR ]{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(delay)
                    continue

                result = response.json()

                if result["message"] == "Quest marked as finished":
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Quest{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} {quest_name} {Style.RESET_ALL}"
                        f"{Fore.GREEN + Style.BRIGHT}is Completed{Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Reward{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} {reward} {reward_icon} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                    return
                elif result["message"] == "Quest can not be completed anymore":
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Quest{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} {quest_name} {Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT}Already Completed{Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                    )
                    return
                else:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Quest{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} {quest_name} {Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT}Failed to Complete{Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                    )
                    return

            except requests.RequestException as e:
                self.log(f"{Fore.RED + Style.BRIGHT}An error occurred: {e}{Style.RESET_ALL}")
                return

        self.log(f"{Fore.RED + Style.BRIGHT}Failed to complete quest {quest_name} after {retries} retries{Style.RESET_ALL}")
    
    def process_query(self, query: str):

        visit = self.user_visit(query)
        if visit:
            user = self.user_info(query)
            if user:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {user['first_name']} {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Diamond{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {user['balance']} 💎 {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Pink{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {user['pinkBalance']} 💗 {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
            else:
                self.log(f"{Fore.YELLOW+Style.BRIGHT}[ User Info Not Found ]{Style.RESET_ALL}")

            daily = self.daily(query)
            if daily:
                claim_daily = self.claim_daily(query)
                if claim_daily:
                    self.log(
                        f"{Fore.GREEN+Style.BRIGHT}[ Check-in{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {daily['current']} 💎 {Style.RESET_ALL}"
                        f"{Fore.GREEN+Style.BRIGHT}Claimed ]{Style.RESET_ALL}"
                    )
                else:
                    self.log(f"{Fore.YELLOW+Style.BRIGHT}[ Already Check-in Today ]{Style.RESET_ALL}          ")
            else:
                self.log(f"{Fore.YELLOW+Style.BRIGHT}[ Daily Check-in Not Found ]{Style.RESET_ALL}")

            refferal = self.refferal(query)
            if refferal:
                reward = refferal['totalAvailableBonuses']

                if reward != 0:
                    claim_refferal = self.claim_refferal(query)

                    if claim_refferal:
                        self.log(
                            f"{Fore.GREEN+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {reward} 💎 {Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT}Claimed ]{Style.RESET_ALL}"
                        )
                    else:
                        self.log(f"{Fore.YELLOW+Style.BRIGHT}[ Refferal Bonus Already Claimed ]{Style.RESET_ALL}")
                else:
                    self.log(f"{Fore.YELLOW+Style.BRIGHT}[ No Available Refferal Bonus ]{Style.RESET_ALL}")
            else:
                self.log(f"{Fore.YELLOW+Style.BRIGHT}[ Refferal Not Found ]{Style.RESET_ALL}")

            print(f"{Fore.YELLOW+Style.BRIGHT}[ Do Tap Tap! Wait..... ]{Style.RESET_ALL}", end="\r", flush=True)
            time.sleep(3)

            point = 10000
            # point = random.randint(900, 1000)
            taps = self.taps(query, point)
            if taps:
                self.log(f"{Fore.GREEN+Style.BRIGHT}[ Success Taps ]{Style.RESET_ALL}")
            else:
                self.log(f"{Fore.YELLOW+Style.BRIGHT}[ No Available Chance to Taps ]{Style.RESET_ALL}")

            ads = self.ads(query)
            if ads:
                print(f"{Fore.YELLOW+Style.BRIGHT}[ Getting Ads Info..... ]{Style.RESET_ALL}", end="\r", flush=True)
                time.sleep(1.5)
                max_count = ads['total']
                count = ads['available']
                if count !=0 :
                    self.log(f"{Fore.GREEN+Style.BRIGHT}[ Ads Found! Watching... {count} / {max_count} ]{Style.RESET_ALL}")
                    time.sleep(3)
                    while count > 0:
                        watch_ads = self.watch_ads(query)
                        if watch_ads:
                            self.log(f"{Fore.YELLOW+Style.BRIGHT}Watching Ads Success{Style.RESET_ALL}")

                        print(f"{Fore.YELLOW+Style.BRIGHT}[ Do Tap Tap! Wait..... ]{Style.RESET_ALL}", end="\r", flush=True)
                        time.sleep(3)
                        
                        taps = self.taps(query, point)
                        if taps:
                            self.log(f"{Fore.GREEN+Style.BRIGHT}[ Success Taps ]{Style.RESET_ALL}")
                        else:
                            self.log(f"{Fore.YELLOW+Style.BRIGHT}[ No Available Chance to Taps ]{Style.RESET_ALL}")

                        count -= 1
                else:
                    self.log(f"{Fore.YELLOW+Style.BRIGHT}[ Oh Sorry, Ads have Reached Their Limit ]{Style.RESET_ALL}")
            else:
                self.log(f"{Fore.YELLOW+Style.BRIGHT}[ Ads Not Found ]{Style.RESET_ALL}")

            quests = self.quests(query)
            if quests:
                print(f"{Fore.YELLOW+Style.BRIGHT}[ Checking Quests...... ]{Style.RESET_ALL}", end="\r", flush=True)
                time.sleep(3)
                for quest in quests:
                    if quest:
                        quest_name = quest['name']
                        type_reward = quest['targetBalance']
                        reward = quest['bonusClicks']

                        if type_reward == "balance":
                            reward_icon = "💎"
                        elif type_reward == "pinkBalance":
                            reward_icon = "💗"
                        else:
                            reward_icon = ""

                        print(
                            f"{Fore.YELLOW+Style.BRIGHT}[ Starting Quests...... ]{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} | {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}[{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {quest_name} {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            , end="\r"
                            , flush=True
                        )
                        time.sleep(3)
                        
                        self.complete_quests(query, quest_name, reward, reward_icon)
                        
                    else:
                        self.log(f"{Fore.RED+Style.BRIGHT}[ Quests Not Found ]{Style.RESET_ALL}")
            else:
                self.log(f"{Fore.RED+Style.BRIGHT}[ Quests Not Found ]{Style.RESET_ALL}")
    
    def main(self):
        try:
            with open('query.txt', 'r') as file:
                queries = [line.strip() for line in file if line.strip()]
            with open('proxies.txt', 'r') as file:
                proxies = [line.strip() for line in file if line.strip()]

            while True:
                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Account's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(queries)}{Style.RESET_ALL}"
                )
                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Proxy's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(proxies)}{Style.RESET_ALL}"
                )
                self.log(
                    f"{Fore.CYAN + Style.BRIGHT}-----------------------------------------------------------------------{Style.RESET_ALL}")

                for i, query in enumerate(queries):
                    query = query.strip()
                    if query:
                        self.log(
                            f"{Fore.GREEN + Style.BRIGHT}Account: {Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT}{i + 1} / {len(queries)}{Style.RESET_ALL}"
                        )
                        if len(proxies) >= len(queries):
                            proxy = self.set_proxy(proxies[i])  # Set proxy for each account
                            self.log(
                                f"{Fore.GREEN + Style.BRIGHT}Use proxy: {Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT}{proxy}{Style.RESET_ALL}"
                            )

                        else:
                            self.log(
                                Fore.RED + "Number of proxies is less than the number of accounts. Proxies are not used!")

                    user_info = extract_user_data(query)
                    user_id = str(user_info.get('id'))
                    self.headers = get_headers(user_id)
                    try:
                        self.process_query(query)
                    except Exception as e:
                        self.log(f"{Fore.RED + Style.BRIGHT}An error process_query: {e}{Style.RESET_ALL}")

                    self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}" * 75)
                    account_delay = config['account_delay']
                    countdown_timer(random.randint(min(account_delay), max(account_delay)))

                cycle_delay = config['cycle_delay']
                countdown_timer(random.randint(min(cycle_delay), max(cycle_delay)))

        except KeyboardInterrupt:
            self.log(f"{Fore.RED + Style.BRIGHT}[ EXIT ] Diamore.co - BOT{Style.RESET_ALL}")
        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    if s_name() == 'Windows':
        sys(f'cls && title Diamore bot')
    else:
        sys('clear')
    diamore = Diamore()
    diamore.clear_terminal()
    diamore.welcome()
    diamore.main()
    