import os
import requests
from colorama import Fore, Style, init
import socket

init(autoreset=True)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ============================================================
#                         INTERFACE
# ============================================================

def banner():
    rouge = "\033[38;2;255;0;0m"

    texte = [
f"{rouge}██╗    ██╗██╗   ██╗██╗  ████████╗██╗    ████████╗ ██████╗  ██████╗ ██╗     ",
f"{rouge}██║    ██║██║   ██║██║  ╚══██╔══╝██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ",
f"{rouge}██║ █╗ ██║██║   ██║██║     ██║   ██║       ██║   ██║   ██║██║   ██║██║     ",
f"{rouge}██║███╗██║██║   ██║██║     ██║   ██║       ██║   ██║   ██║██║   ██║██║     ",
f"{rouge}╚███╔███╔╝╚██████╔╝███████╗██║   ██║       ██║   ╚██████╔╝╚██████╔╝███████╗",
f"{rouge} ╚══╝╚══╝  ╚═════╝ ╚══════╝╚═╝   ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝",
"",
f"{rouge}            ====== WULTI TOOLBOX ======",
"",
f"{rouge}╭────────────────────────╮   ╭────────────────────────╮   ╭────────────────────────╮",
f"{rouge}│     [1] IP Lookup      │   │      [2] GeoIP+        │   │    [3] Host Lookup     │",
f"{rouge}├────────────────────────┤   ├────────────────────────┤   ├────────────────────────┤",
f"{rouge}│ Analyse une IP         │   │ Géolocalisation        │   │ Analyse un site web    │",
f"{rouge}╰────────────────────────╯   ╰────────────────────────╯   ╰────────────────────────╯",
"",
f"{rouge}╭────────────────────────╮   ╭────────────────────────╮   ╭────────────────────────╮",
f"{rouge}│   [4] Webhook Panel    │   │     [5] Ping Tool      │   │  [6] Username Check    │",
f"{rouge}├────────────────────────┤   ├────────────────────────┤   ├────────────────────────┤",
f"{rouge}│ Envoyer via webhook    │   │ Tester la latence      │   │ Vérifier un pseudo     │",
f"{rouge}╰────────────────────────╯   ╰────────────────────────╯   ╰────────────────────────╯",
    ]

    for line in texte:
        print(line)

# ============================================================
#                         FONCTIONS
# ============================================================

def ip_lookup():
    ip = input("Enter IP: ")
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}")
        data = r.json()

        print(Fore.RED + "\n===== RESULT =====")
        for k, v in data.items():
            print(f"{k}: {v}")
        print(Fore.RED + "==================\n")

    except:
        print("Error while searching IP.")


def geoip_plus():
    ip = input("Enter IP: ")
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}?fields=66846719")
        data = r.json()

        print(Fore.RED + "\n===== GEOIP+ =====")
        for k, v in data.items():
            print(f"{k}: {v}")
        print(Fore.RED + "==================\n")

    except:
        print("Error while searching GeoIP.")


def host_lookup():
    site = input("Enter website (ex: google.com): ")

    try:
        ip = socket.gethostbyname(site)
        r = requests.get(f"http://ip-api.com/json/{ip}?fields=66846719")
        data = r.json()

        print(Fore.RED + "\n===== HOST LOOKUP =====")
        print("Website:", site)
        print("IP:", ip)
        for k, v in data.items():
            print(f"{k}: {v}")
        print(Fore.RED + "=======================\n")

    except:
        print("Error while resolving host.")


def webhook_panel():
    while True:
        clear()
        print(Fore.RED + "===== WEBHOOK PANEL =====")
        print("[1] Send a message")
        print("[2] Send up to 5 messages")
        print("[0] Back")
        print("=========================\n")

        choice = input("Select option > ")

        if choice == "1":
            url = input("Webhook URL: ")
            msg = input("Message: ")
            requests.post(url, json={"content": msg})
            print("Message sent!")
            input("Press Enter...")

        elif choice == "2":
            url = input("Webhook URL: ")
            msg = input("Message: ")
            amount = int(input("How many messages (max 5): "))

            if amount < 1 or amount > 5:
                print("Choose between 1 and 5.")
                input("Press Enter...")
                continue

            for _ in range(amount):
                requests.post(url, json={"content": msg})

            print("Done!")
            input("Press Enter...")

        elif choice == "0":
            break


def ping_tool():
    host = input("IP or website: ")
    os.system(f"ping {host}")


def username_checker():
    username = input("Username: ")

    sites = {
        "GitHub": f"https://github.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}"
    }

    for site, url in sites.items():
        r = requests.get(url)
        if r.status_code == 200:
            print(Fore.RED + f"{site}: FOUND -> {url}")
        else:
            print(f"{site}: Not found")


# ============================================================
#                         MAIN MENU
# ============================================================

while True:
    clear()
    banner()
    choice = input(Fore.RED + "[WULTI] Select Tool > ")

    if choice == "1":
        ip_lookup(); input("Press Enter...")

    elif choice == "2":
        geoip_plus(); input("Press Enter...")

    elif choice == "3":
        host_lookup(); input("Press Enter...")

    elif choice == "4":
        webhook_panel()

    elif choice == "5":
        ping_tool(); input("Press Enter...")

    elif choice == "6":
        username_checker(); input("Press Enter...")

    else:
        print("Invalid option.")
        input("Press Enter...")
