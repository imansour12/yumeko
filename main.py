import sys
import argparse
import pychromecast

parser = argparse.ArgumentParser(prog="Yumeko" , description="An alarm system that connects to a chromecast device and plays a sound when triggered.",epilog="Iyed")
parser.add_argument('-d', "--device", help="The chromecast device name", required=False)
parser.add_argument('-t',  "--time", help="The time to wait before triggering the alarm", required=True)
parser.add_argument('-s',  "--sound", help="The sound to play when the alarm is triggered", required=True)

args = parser.parse_args()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def choose_device():
    print(f"{bcolors.OKBLUE}Searching for chromecast devices on the network...{bcolors.ENDC}")
    services, browser = pychromecast.discovery.discover_chromecasts()
    print(services)
    print(browser.services)
    services = [x for x in services if x is not None]
    if len(services) == 0:
        print(f"{bcolors.FAIL}No chromecast devices found on the network.{bcolors.ENDC}")
        sys.exit(1)
    print(f"{bcolors.OKGREEN}Found {len(services)} chromecast devices on the network.{bcolors.ENDC}")
    #loop through each of them with an index and ask user to choose
    for i, service in enumerate(services):
        print(f"{bcolors.OKCYAN}[{i}] {service.friendly_name}{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}Choose a chromecast device by entering its index number:{bcolors.ENDC}")
    while True:
        try:
            index = int(input())
            if index < 0 or index >= len(services):
                raise ValueError
            break
        except ValueError:
            print(f"{bcolors.FAIL}Invalid index number. Try again:{bcolors.ENDC}")
    return services[index]



def main():
    if args.device is None:
        device = choose_device()
        print(device)


if __name__ == "__main__":
    main()