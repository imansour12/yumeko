import sys
import argparse
import pychromecast

parser = argparse.ArgumentParser(prog="Yumeko" , description="An alarm system that connects to a chromecast device and plays a sound when triggered.",epilog="Iyed")
parser.add_argument('-d', "--device", help="The chromecast device name", required=False)
parser.add_argument('-t',  "--time", help="The time to wait before triggering the alarm", required=True)
parser.add_argument('-s',  "--sound", help="The sound to play when the alarm is triggered", required=True)

args = parser.parse_args()

def choose_device():
    # Discover available Chromecast devices
    services, browser = pychromecast.discovery.discover_chromecasts()
    # Print the services found
    print(services)

def main():
    if args.device is None:
        device = choose_device()
        print(device)


if __name__ == "__main__":
    main()