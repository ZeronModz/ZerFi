#!/usr/bin/env python3
"""
  ███████╗███████╗██████╗ ███████╗██╗
╚══███╔╝██╔════╝██╔══██╗██╔════╝██║
  ███╔╝ █████╗  ██████╔╝█████╗  ██║
 ███╔╝  ██╔══╝  ██╔══██╗██╔══╝  ██║
███████╗███████╗██║  ██║██║     ██║
╚══════╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
"""
import sys

SOCIAL = {
    1: {"name": "Telegram",   "url": "https://t.me/DevZeron"},
    2: {"name": "GitHub",     "url": "https://github.com/ZeronModz"},
    3: {"name": "Telegram Channel", "url": "https://t.me/DevZeron"},
}

HEADER = r"""
╔══════════════════════════════════════╗
║        ZerFi — DevZeron            ║
╚══════════════════════════════════════╝
"""

def show_menu():
    print('\033[1;36m' + HEADER + '\033[0m')
    print('\033[1;33m  Contact DevZeron — Choose a Platform\033[0m\n')
    for k, v in SOCIAL.items():
        print(f'\033[1;36m  [{k}]\033[0m \033[1;32m{v["name"]}\033[0m')
    print('\033[1;36m  [0]\033[0m \033[1;31mExit\033[0m')
    print()

def _safe_input(prompt=''):
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        raise KeyboardInterrupt

def main():
    show_menu()
    while True:
        try:
            ch = _safe_input('\033[1;33m  [\033[1;37m?\033[1;33m] Choose option: \033[0m').strip()
            if ch == '0':
                print('\033[1;36m│\033[0m        \033[1;32mSee you! — DevZeron\033[0m          \033[1;36m│\033[0m')
                break
            n = int(ch)
            if n in SOCIAL:
                info = SOCIAL[n]
                print(f'\033[1;36m│\033[0m')
                print(f'\033[1;36m│\033[0m  \033[1;33m{info["name"]}\033[0m')
                print(f'\033[1;36m│\033[0m  \033[1;37m{info["url"]}\033[0m')
                print(f'\033[1;36m│\033[0m')
                _safe_input('\033[1;33m  Press Enter to continue...\033[0m')
                show_menu()
            else:
                print('\033[1;31m  Invalid option!\033[0m')
        except (ValueError, KeyboardInterrupt):
            print('\n\033[1;36m│\033[0m        \033[1;32mSee you! — DevZeron\033[0m          \033[1;36m│\033[0m')
            break
        except EOFError:
            print()
            break

if __name__ == '__main__':
    main()
