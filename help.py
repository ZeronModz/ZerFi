#!/usr/bin/env python3
# ─────────────────────────────────────────────
#  ZerFi Help Guide — by DevZeron (Redesigned)
#  Run: zerfi help
# ─────────────────────────────────────────────

import sys
import os
import time
import random

# ── Colors (256-color ANSI) ──
R  = '\033[38;5;196m'
G  = '\033[38;5;46m'
Y  = '\033[38;5;226m'
B  = '\033[38;5;27m'
M  = '\033[38;5;201m'
C  = '\033[38;5;51m'
W  = '\033[38;5;255m'
RS = '\033[0m'

# ── Extended neon palette ──
G1  = '\033[38;5;34m'
G2  = '\033[38;5;40m'
G3  = '\033[38;5;46m'
C1  = '\033[38;5;30m'
C2  = '\033[38;5;43m'
C3  = '\033[38;5;51m'
M1  = '\033[38;5;53m'
M2  = '\033[38;5;127m'
M3  = '\033[38;5;201m'
Y1  = '\033[38;5;100m'
Y2  = '\033[38;5;184m'
Y3  = '\033[38;5;226m'
R1  = '\033[38;5;52m'
R2  = '\033[38;5;160m'
R3  = '\033[38;5;196m'
GR  = '\033[38;5;242m'
DIM = '\033[38;5;239m'
BO  = '\033[1m'

# ── Symbols ──
OK   = f'{G3}[{W}+{G3}]{RS}'
INFO = f'{C3}[{W}i{C3}]{RS}'
WARN = f'{Y3}[{W}!{Y3}]{RS}'
TIP  = f'{M3}[{W}\u2605{M3}]{RS}'
CMD  = f'{C3}[{W}>{C3}]{RS}'

LINE  = C3 + '\u2501' * 52 + RS
LINE2 = C1 + '\u2500' * 52 + RS

# ── Box-drawing chars (for use inside f-string expressions) ──
BOX_H  = '\u2550'
BOX_TL = '\u2554'
BOX_TR = '\u2557'
BOX_BL = '\u255a'
BOX_BR = '\u255d'
BOX_V  = '\u2551'

# ── Animation helpers ──

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def type_text(text, delay=0.03):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

def type_text_inline(text, delay=0.03):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)

def spinner(duration=0.8, message=''):
    chars = ['\u280b', '\u2819', '\u2839', '\u2838', '\u283c', '\u2834', '\u2826', '\u2827', '\u2807', '\u280f']
    end = time.time() + duration
    i = 0
    while time.time() < end:
        sys.stdout.write(f'\r  {C3}{message}{RS} {Y3}{chars[i % len(chars)]}{RS} ')
        sys.stdout.flush()
        time.sleep(0.06)
        i += 1
    n = len(message) + 6
    sys.stdout.write('\r' + ' ' * n + '\r')
    sys.stdout.flush()

def transition():
    spinner(0.5, 'Loading')
    time.sleep(0.08)

def fade_clear():
    sys.stdout.write('\033[?25l')
    for _ in range(3):
        print()
        time.sleep(0.05)
    clear()
    sys.stdout.write('\033[?25h')

def pause():
    print()
    sys.stdout.write(f'  {INFO} {GR}Press Enter to go back to menu...{RS}')
    sys.stdout.flush()
    try:
        input()
    except (KeyboardInterrupt, EOFError):
        print()
        sys.stdout.write('\033[?25h')
        sys.exit(0)

# ── Gradient Banner ──

BANNER_LINES = [
    "███████╗███████╗██████╗ ███████╗██╗",
    "╚══███╔╝██╔════╝██╔══██╗██╔════╝██║",
    "  ███╔╝ █████╗  ██████╔╝█████╗  ██║",
    " ███╔╝  ██╔══╝  ██╔══██╗██╔══╝  ██║",
    "███████╗███████╗██║  ██║██║     ██║",
    "╚══════╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝",
]

BANNER_GRAD = [G1, G1, G2, G3, C2, C3]

def gradient_banner():
    BOX_W = 52
    DASH_W = BOX_W - 2
    INNER_W = BOX_W - 4

    # Top border
    print(f'{C3}{BOX_TL}{BOX_H * DASH_W}{BOX_TR}{RS}')

    # Spacer
    print(f'{C3}{BOX_V}{RS}{" " * INNER_W}{C3}{BOX_V}{RS}')

    # Banner lines with gradient
    for i, line in enumerate(BANNER_LINES):
        c = BANNER_GRAD[i]
        padded = '  ' + line
        padded = padded.center(INNER_W - 2)
        print(f'{C3}{BOX_V}{RS} {c}{padded}{RS} {C3}{BOX_V}{RS}')

    # Spacer
    print(f'{C3}{BOX_V}{RS}{" " * INNER_W}{C3}{BOX_V}{RS}')

    # Subtitle with gradient
    sub = 'Help Guide \u2014 v2.0'
    dev = '\u2605  DevZeron'
    print(f'{C3}{BOX_V}{RS} {C2}{sub.center(INNER_W - 2)}{RS} {C3}{BOX_V}{RS}')
    print(f'{C3}{BOX_V}{RS} {M3}{dev.center(INNER_W - 2)}{RS} {C3}{BOX_V}{RS}')

    # Spacer
    print(f'{C3}{BOX_V}{RS}{" " * INNER_W}{C3}{BOX_V}{RS}')

    # Bottom border
    print(f'{C3}{BOX_BL}{BOX_H * DASH_W}{BOX_BR}{RS}')

# ── Menu ──

def show_menu():
    fade_clear()
    gradient_banner()
    print()
    print(f'  {C3}{LINE}{RS}')
    type_text_inline(f'  {Y3}What do you want to know? Pick a number:{RS}', 0.02)
    print(f'  {C3}{LINE}{RS}')
    print()

    opts = [
        (' 1', 'What is ZerFi? Introduction'),
        (' 2', 'How to Install / Setup'),
        (' 3', 'What is an Interface & how to find it'),
        (' 4', 'All Attack Modes explained'),
        (' 5', 'Full Command List (A-Z)'),
        (' 6', 'Usage Examples (Copy-Paste ready)'),
        (' 7', 'Troubleshooting common errors'),
        (' 8', 'Important warnings & rules'),
        (' 9', 'Available zerfi commands (quick reference)'),
        (' 0', 'Exit'),
    ]

    for num, desc in opts:
        ty = f'  {G3}{num}{RS}  {W}\u2192{RS}  {GR}{desc}{RS}'
        type_text_inline(ty + '\n', 0.005)

    print()
    print(f'  {C3}{LINE}{RS}')
    print()
    sys.stdout.write(f'  {C3}Your choice: {RS}')
    sys.stdout.flush()
    return input().strip()

# ─────────────────────── Section 1 ───────────────────────

def section_intro():
    fade_clear()
    gradient_banner()
    print()
    print(f'  {C3}{LINE}{RS}')
    type_text(f'  {Y3}1. What is ZerFi \u2014 Introduction{RS}', 0.025)
    print(f'  {C3}{LINE}{RS}')
    print()

    print(f'''  {INFO} {W}ZerFi{RS} is a WPS (Wi-Fi Protected Setup)
     security testing tool that runs in Termux.

  {INFO} It lets you test WPS vulnerabilities
     on your own router.''')
    print()
    print(f'  {C2}{LINE2}{RS}')
    type_text_inline(f'  {Y3}  What is WPS?{RS}', 0.02)
    print()
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'''  WPS is a router feature that allows
  connecting to WiFi using an 8-digit PIN.
  Many older routers have PINs that can be
  easily extracted \u2014 that's what ZerFi tests.''')
    print()
    print(f'  {C2}{LINE2}{RS}')
    type_text_inline(f'  {Y3}  What can ZerFi do?{RS}', 0.02)
    print()
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  {G3}\u2714{RS} Pixie Dust Attack    \u2014 fast PIN extraction')
    print(f'  {G3}\u2714{RS} Bruteforce Attack    \u2014 try all PINs step by step')
    print(f'  {G3}\u2714{RS} Network Scanner      \u2014 scan nearby WiFi networks')
    print(f'  {G3}\u2714{RS} Session Save/Resume  \u2014 pause & resume attacks')
    print(f'  {G3}\u2714{RS} HTML/CSV/JSON Report \u2014 save results to file')
    print()
    print(f'  {TIP} {M3}Only test your own network \u2014 never others\'.{RS}')
    pause()

# ─────────────────────── Section 2 ───────────────────────

def section_install():
    fade_clear()
    gradient_banner()
    print()
    print(f'  {C3}{LINE}{RS}')
    type_text(f'  {Y3}2. How to Install / Setup{RS}', 0.025)
    print(f'  {C3}{LINE}{RS}')
    print()

    print(f'  {INFO} Run these commands one by one in Termux:')
    print()
    print(f'  {C2}{LINE2}{RS}')
    type_text_inline(f'  {Y3}  Step 1 \u2014 Update Termux packages{RS}', 0.02)
    print()
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  {CMD} {C3}pkg update && pkg upgrade{RS}')
    print()
    print(f'  {C2}{LINE2}{RS}')
    type_text_inline(f'  {Y3}  Step 2 \u2014 Install required packages{RS}', 0.02)
    print()
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  {CMD} {C3}pkg install python root-repo{RS}')
    print(f'  {CMD} {C3}pkg install wpa-supplicant pixiewps{RS}')
    print(f'  {CMD} {C3}pkg install wireless-tools iw{RS}')
    print()
    print(f'  {C2}{LINE2}{RS}')
    type_text_inline(f'  {Y3}  Step 3 \u2014 Run ZerFi{RS}', 0.02)
    print()
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  {CMD} {C3}cd /path/to/zerfi/folder{RS}')
    print(f'  {CMD} {C3}python main.py -i wlan0{RS}')
    print()
    print(f'  {C2}{LINE2}{RS}')
    type_text_inline(f'  {Y3}  Step 4 \u2014 Make sure you have root access{RS}', 0.02)
    print()
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  ZerFi requires root to run.')
    print(f'  In Termux:')
    print()
    print(f'  {CMD} {C3}su{RS}        \u2190 get root')
    print(f'  {CMD} {C3}python main.py -i wlan0{RS}')
    print()
    print(f'  {TIP} {M3}Without root you will see: "Run it as root" error.{RS}')
    pause()

# ─────────────────────── Section 3 ───────────────────────

def section_interface():
    fade_clear()
    gradient_banner()
    print()
    print(f'  {C3}{LINE}{RS}')
    type_text(f'  {Y3}3. What is an Interface & how to find it{RS}', 0.025)
    print(f'  {C3}{LINE}{RS}')
    print()

    print(f'''  {INFO} Interface is the name of your WiFi card.
     Usually it is: {G3}wlan0{RS}, {G3}wlan1{RS}, or {G3}wlan2{RS}''')
    print()
    print(f'  {C2}{LINE2}{RS}')
    type_text_inline(f'  {Y3}  Commands to find your interface:{RS}', 0.02)
    print()
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  {CMD} {C3}ip link show{RS}')
    print(f'     \u2193 Shows all network interfaces')
    print()
    print(f'  {CMD} {C3}iwconfig{RS}')
    print(f'     \u2193 Shows only WiFi interfaces')
    print()
    print(f'  {CMD} {C3}iw dev{RS}')
    print(f'     \u2193 Detailed WiFi info')
    print()
    print(f'  {C2}{LINE2}{RS}')
    type_text_inline(f'  {Y3}  Output will look like this:{RS}', 0.02)
    print()
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  {W}2: wlan0: <BROADCAST,MULTICAST,UP>{RS}')
    print(f'       \u2191')
    print(f'       {G3}This is your interface name{RS}')
    print()
    print(f'  {C2}{LINE2}{RS}')
    type_text_inline(f'  {Y3}  Use it in ZerFi like this:{RS}', 0.02)
    print()
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  {CMD} {C3}python main.py -i wlan0{RS}')
    print(f'                   {Y3}\u2191{RS}')
    print(f'               {Y3}replace with your interface name{RS}')
    print()
    print(f'  {WARN} {Y3}Some devices may use wlan1 or a different name')
    print(f'     instead of wlan0.{RS}')
    pause()

# ─────────────────────── Section 4 ───────────────────────

def section_attacks():
    fade_clear()
    gradient_banner()
    print()
    print(f'  {C3}{LINE}{RS}')
    type_text(f'  {Y3}4. All Attack Modes Explained{RS}', 0.025)
    print(f'  {C3}{LINE}{RS}')
    print()

    print(f'  {C2}{LINE2}{RS}')
    print(f'  {G3}  \u2605 Pixie Dust Attack  (-K){RS}')
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  {INFO} The fastest attack. Extracts the PIN offline')
    print(f'     from the router\'s WPS handshake data.')
    print(f'     Can finish in just a few seconds if successful.')
    print()
    print(f'  {CMD} {C3}python main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -K{RS}')
    print()
    print(f'  {G3}\u2714{RS} Very fast   {R3}\u2718{RS} Doesn\'t work on all routers')
    print()
    print(f'  {C2}{LINE2}{RS}')
    print(f'  {G3}  \u2605 Bruteforce Attack  (-B){RS}')
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  {INFO} Tries all possible PINs one by one (up to 11000).')
    print(f'     Has a chance to work on any WPS-enabled router.')
    print()
    print(f'  {CMD} {C3}python main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -B{RS}')
    print()
    print(f'  {G3}\u2714{RS} Works on more routers')
    print(f'  {R3}\u2718{RS} Can take a very long time (hours)')
    print()
    print(f'  {C2}{LINE2}{RS}')
    print(f'  {G3}  \u2605 Auto Scan + Attack  (no BSSID){RS}')
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  {INFO} Scans and lists all nearby WPS networks.')
    print(f'     You pick one, then the attack starts.')
    print()
    print(f'  {CMD} {C3}python main.py -i wlan0 -K{RS}')
    print()
    print(f'  {C2}{LINE2}{RS}')
    print(f'  {G3}  \u2605 Push Button Connect  (--pbc){RS}')
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  {INFO} Attempts to connect when you press the')
    print(f'     WPS button on the router.')
    print()
    print(f'  {CMD} {C3}python main.py -i wlan0 --pbc{RS}')
    pause()

# ─────────────────────── Section 5 ───────────────────────

def section_commands():
    fade_clear()
    gradient_banner()
    print()
    print(f'  {C3}{LINE}{RS}')
    type_text(f'  {Y3}5. Full Command Argument List (A-Z){RS}', 0.025)
    print(f'  {C3}{LINE}{RS}')
    print()

    print(f'  {Y3}  \u2500\u2500\u2500 Required \u2500\u2500\u2500{RS}')
    print(f'  {G3}-i{RS}, {G3}--interface{RS}   WiFi interface name (e.g. wlan0)')
    print()
    print(f'  {Y3}  \u2500\u2500\u2500 Target \u2500\u2500\u2500{RS}')
    print(f'  {G3}-b{RS}, {G3}--bssid{RS}       Router MAC address (AA:BB:CC:DD:EE:FF)')
    print(f'  {G3}-p{RS}, {G3}--pin{RS}         Try a specific PIN')
    print()
    print(f'  {Y3}  \u2500\u2500\u2500 Attack Mode \u2500\u2500\u2500{RS}')
    print(f'  {G3}-K{RS}, {G3}--pixie-dust{RS}  Run Pixie Dust attack')
    print(f'  {G3}-F{RS}, {G3}--pixie-force{RS} Pixie Dust full range (slower but stronger)')
    print(f'  {G3}-B{RS}, {G3}--bruteforce{RS}  Run Bruteforce attack')
    print(f'  {G3}--pbc{RS}             Push Button Connect')
    print()
    print(f'  {Y3}  \u2500\u2500\u2500 Timing \u2500\u2500\u2500{RS}')
    print(f'  {G3}-d{RS}, {G3}--delay{RS}       Delay between attempts (seconds)')
    print(f'  {G3}-t{RS}, {G3}--timeout{RS}     WPS response wait time [10s]')
    print(f'  {G3}-T{RS}, {G3}--m57-timeout{RS} M5/M7 message timeout [0.40s]')
    print(f'  {G3}--lock-delay{RS}     Wait time when router is locked [60s]')
    print(f'  {G3}--fail-wait{RS}      Pause after 10 failures (seconds)')
    print(f'  {G3}--recurring-delay{RS} Pause Y seconds every X attempts (X:Y)')
    print()
    print(f'  {Y3}  \u2500\u2500\u2500 Bruteforce Control \u2500\u2500\u2500{RS}')
    print(f'  {G3}-g{RS}, {G3}--max-attempts{RS} Max number of attempts [0=unlimited]')
    print(f'  {G3}-L{RS}, {G3}--ignore-locks{RS} Ignore router lock and keep going')
    print(f'  {G3}-M{RS}, {G3}--mac-changer{RS}  Change MAC address on each attempt')
    print()
    print(f'  {Y3}  \u2500\u2500\u2500 Session \u2500\u2500\u2500{RS}')
    print(f'  {G3}--list-sessions{RS}   Show saved sessions')
    print(f'  {G3}--resume-session{RS}  Resume a previous session (provide BSSID)')
    print()
    print(f'  {Y3}  \u2500\u2500\u2500 Output / Report \u2500\u2500\u2500{RS}')
    print(f'  {G3}--html-report{RS}     Generate HTML report')
    print(f'  {G3}--report-format{RS}   Report format: html / txt / csv / json')
    print(f'  {G3}--detailed-report{RS} Include more details in report')
    print(f'  {G3}--json-output{RS}     Save results to JSON file')
    print(f'  {G3}--csv-output{RS}      Save results to CSV file')
    print(f'  {G3}--log-file{RS}        Log all activity to a file')
    print()
    print(f'  {Y3}  \u2500\u2500\u2500 Network Scan \u2500\u2500\u2500{RS}')
    print(f'  {G3}--vuln-list{RS}       File with list of vulnerable devices')
    print(f'  {G3}--auto-vuln-list{RS}  Auto-add cracked devices to vuln list')
    print(f'  {G3}-r{RS}, {G3}--reverse-scan{RS} Reverse the network list order')
    print(f'  {G3}--detect-weak-algo{RS} Detect routers with weak WPS algorithm')
    print(f'  {G3}--signal-analysis{RS}  Analyze signal strength before attack')
    print(f'  {G3}--check-vuln{RS}       Show vulnerability report before attack')
    print(f'  {G3}--pixie-list{RS}       Show all Pixie Dust vulnerable routers')
    print(f'  {G3}--list-all-models{RS}  Show all router models in database')
    print()
    print(f'  {Y3}  \u2500\u2500\u2500 Quick Launch \u2500\u2500\u2500{RS}')
    print(f'  {G3}zerfi{RS}              Run with default settings (wlan0 + Pixie Dust)')
    print(f'  {G3}zerfi menu{RS}         Open ZerFi interactive menu (no auto-attack)')
    print(f'  {G3}zerfi old{RS}          Run old engine (w1.py) with wlan0')
    print(f'  {G3}zerfi update{RS}       Update ZerFi to latest version')
    print(f'  {G3}zerfi help{RS}         Show this help guide')
    print(f'  {G3}zerfi fix{RS}          Fix root/superuser issues')
    print(f'  {G3}zerfi contact{RS}      Contact the developer')
    print()
    print(f'  {Y3}  \u2500\u2500\u2500 Android / Termux \u2500\u2500\u2500{RS}')
    print(f'  {G3}--dts{RS}              Don\'t touch Android WiFi settings')
    print(f'  {G3}--mtk-wifi{RS}         Enable MediaTek WiFi driver')
    print(f'  {G3}--handle-rfkill{RS}    Auto-unblock if rfkill is blocking WiFi')
    print(f'  {G3}--iface-down{RS}       Bring interface down after finishing')
    print()
    print(f'  {Y3}  \u2500\u2500\u2500 Other \u2500\u2500\u2500{RS}')
    print(f'  {G3}-v{RS}, {G3}--verbose{RS}      Show detailed debug output')
    print(f'  {G3}-l{RS}, {G3}--loop{RS}         Restart scan after finishing')
    print(f'  {G3}-X{RS}, {G3}--show-pixie-cmd{RS} Show the pixiewps command used')
    print(f'  {G3}--no-colors{RS}        Disable colored output')
    print(f'  {G3}--pin-algo{RS}         Choose a specific PIN algorithm')
    print(f'  {G3}--write-legacy{RS}     Also save in legacy format')
    print(f'  {G3}-h{RS}, {G3}--help{RS}         Show help')
    pause()

# ─────────────────────── Section 6 ───────────────────────

def section_examples():
    fade_clear()
    gradient_banner()
    print()
    print(f'  {C3}{LINE}{RS}')
    type_text(f'  {Y3}6. Usage Examples (Copy-Paste ready){RS}', 0.025)
    print(f'  {C3}{LINE}{RS}')
    print()

    print(f'  {C2}{LINE2}{RS}')
    print(f'  {G3}  Quick start \u2014 Scan and pick a network:{RS}')
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  {CMD} {C3}python main.py -i wlan0 -K{RS}')
    print(f'     \u2193 Scans nearby WPS networks, pick one, runs Pixie Dust')
    print()
    print(f'  {CMD} {C3}python main.py -i wlan0 -B{RS}')
    print(f'     \u2193 Scans nearby WPS networks, pick one, runs Bruteforce')
    print()
    print(f'  {C2}{LINE2}{RS}')
    print(f'  {G3}  Attack a specific router:{RS}')
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  {CMD} {C3}python main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -K{RS}')
    print(f'     \u2193 Runs Pixie Dust directly on that router')
    print()
    print(f'  {CMD} {C3}python main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -B{RS}')
    print(f'     \u2193 Runs Bruteforce directly on that router')
    print()
    print(f'  {C2}{LINE2}{RS}')
    print(f'  {G3}  Two attacks \u2014 Pixie first, then Bruteforce if it fails:{RS}')
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  {CMD} {C3}python main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -K{RS}')
    print(f'     \u2193 If Pixie Dust fails:')
    print(f'  {CMD} {C3}python main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -B{RS}')
    print()
    print(f'  {C2}{LINE2}{RS}')
    print(f'  {G3}  Slow attack to avoid router lockout:{RS}')
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  {CMD} {C3}python main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -B -d 2{RS}')
    print(f'     \u2193 2 second delay between each attempt')
    print()
    print(f'  {CMD} {C3}python main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -B --recurring-delay 10:30{RS}')
    print(f'     \u2193 Pause 30 seconds after every 10 attempts')
    print()
    print(f'  {C2}{LINE2}{RS}')
    print(f'  {G3}  Attack with MAC changing:{RS}')
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  {CMD} {C3}python main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -B -M{RS}')
    print()
    print(f'  {C2}{LINE2}{RS}')
    print(f'  {G3}  Resume a previous session:{RS}')
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  {CMD} {C3}python main.py --list-sessions{RS}')
    print(f'     \u2193 View saved sessions')
    print()
    print(f'  {CMD} {C3}python main.py -i wlan0 --resume-session AA:BB:CC:DD:EE:FF{RS}')
    print(f'     \u2193 Continue attack from where you left off')
    print()
    print(f'  {C2}{LINE2}{RS}')
    print(f'  {G3}  Generate reports:{RS}')
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  {CMD} {C3}python main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -K --html-report{RS}')
    print(f'  {CMD} {C3}python main.py -i wlan0 -K --html-report --report-format json{RS}')
    print()
    print(f'  {C2}{LINE2}{RS}')
    print(f'  {G3}  Browse the database:{RS}')
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  {CMD} {C3}python main.py --pixie-list{RS}')
    print(f'     \u2193 Which routers are Pixie Dust vulnerable')
    print()
    print(f'  {CMD} {C3}python main.py --list-all-models{RS}')
    print(f'     \u2193 All router models in the database')
    print()
    print(f'  {C2}{LINE2}{RS}')
    print(f'  {G3}  Safe usage on Android / Termux:{RS}')
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  {CMD} {C3}python main.py -i wlan0 -K --dts{RS}')
    print(f'     \u2193 Won\'t change Android WiFi settings')
    print()
    print(f'  {CMD} {C3}python main.py -i wlan0 -K --handle-rfkill{RS}')
    print(f'     \u2193 Auto-unblocks WiFi if rfkill is blocking it')
    print()
    print(f'  {C2}{LINE2}{RS}')
    print(f'  {G3}  Signal analysis before attacking:{RS}')
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  {CMD} {C3}python main.py -i wlan0 --signal-analysis -B{RS}')
    print()
    print(f'  {C2}{LINE2}{RS}')
    print(f'  {G3}  Verbose mode (see everything):{RS}')
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  {CMD} {C3}python main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -K -v{RS}')
    pause()

# ─────────────────────── Section 7 ───────────────────────

def section_troubleshoot():
    fade_clear()
    gradient_banner()
    print()
    print(f'  {C3}{LINE}{RS}')
    type_text(f'  {Y3}7. Troubleshooting Common Errors{RS}', 0.025)
    print(f'  {C3}{LINE}{RS}')
    print()

    print(f'  {C2}{LINE2}{RS}')
    print(f'  {R3}  \u2718  "Run it as root" error{RS}')
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  Cause: Running without root access')
    print(f'  Fix:')
    print(f'  {CMD} {C3}su{RS}')
    print(f'  {CMD} {C3}python main.py -i wlan0 -K{RS}')
    print()
    print(f'  {C2}{LINE2}{RS}')
    print(f'  {R3}  \u2718  "Unable to up interface" error{RS}')
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  Cause: Wrong interface name or WiFi is off')
    print(f'  Fix:')
    print(f'  {CMD} {C3}ip link show{RS}          \u2190 find the correct interface name')
    print(f'  {CMD} {C3}ip link set wlan0 up{RS}  \u2190 bring the interface up')
    print()
    print(f'  {C2}{LINE2}{RS}')
    print(f'  {R3}  \u2718  wpa_supplicant error / crash{RS}')
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  Cause: A previous instance is still running')
    print(f'  Fix:')
    print(f'  {CMD} {C3}pkill wpa_supplicant{RS}')
    print(f'  {CMD} {C3}python main.py -i wlan0 -K{RS}')
    print()
    print(f'  {C2}{LINE2}{RS}')
    print(f'  {R3}  \u2718  "WiFi is rfkill blocked" error{RS}')
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  Cause: WiFi is blocked by rfkill')
    print(f'  Fix:')
    print(f'  {CMD} {C3}python main.py -i wlan0 -K --handle-rfkill{RS}')
    print(f'  or:')
    print(f'  {CMD} {C3}rfkill unblock wifi{RS}')
    print()
    print(f'  {C2}{LINE2}{RS}')
    print(f'  {R3}  \u2718  No WPS networks found{RS}')
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  Try:')
    print(f'  \u2022 Move closer to the router')
    print(f'  \u2022 Turn Location off on Android')
    print(f'  \u2022 Toggle WiFi off and back on')
    print(f'  \u2022 Run with {C3}--dts{RS} flag')
    print()
    print(f'  {C2}{LINE2}{RS}')
    print(f'  {R3}  \u2718  Pixie Dust always failing{RS}')
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  Cause: Router is not Pixie Dust vulnerable')
    print(f'  Fix: Try Bruteforce instead')
    print(f'  {CMD} {C3}python main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -B{RS}')
    print()
    print(f'  {C2}{LINE2}{RS}')
    print(f'  {R3}  \u2718  Router keeps locking{RS}')
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  Fix 1 \u2014 Slow down:')
    print(f'  {CMD} {C3}python main.py -i wlan0 -b ... -B -d 3{RS}')
    print()
    print(f'  Fix 2 \u2014 Increase lock delay:')
    print(f'  {CMD} {C3}python main.py -i wlan0 -b ... -B --lock-delay 120{RS}')
    print()
    print(f'  Fix 3 \u2014 Change MAC on each attempt:')
    print(f'  {CMD} {C3}python main.py -i wlan0 -b ... -B -M{RS}')
    print()
    print(f'  {C2}{LINE2}{RS}')
    print(f'  {R3}  \u2718  pixiewps: command not found{RS}')
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  {CMD} {C3}pkg install pixiewps{RS}')
    print()
    print(f'  {C2}{LINE2}{RS}')
    print(f'  {R3}  \u2718  ImportError / ModuleNotFoundError{RS}')
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  {CMD} {C3}pkg install python{RS}')
    print(f'  {CMD} {C3}pip install -r requirements.txt{RS}  \u2190 if the file exists')
    pause()

# ─────────────────────── Section 8 ───────────────────────

def section_warnings():
    fade_clear()
    gradient_banner()
    print()
    print(f'  {C3}{LINE}{RS}')
    type_text(f'  {Y3}8. Important Warnings & Rules{RS}', 0.025)
    print(f'  {C3}{LINE}{RS}')
    print()

    print(f'  {R3}\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2557{RS}')
    print(f'  {R3}\u2551{RS}   {Y3}\u26a0{RS}  Read carefully \u2014 this is important!   {R3}\u2551{RS}')
    print(f'  {R3}\u255a\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u255d{RS}')
    print()
    print(f'  {C2}{LINE2}{RS}')
    print(f'  {R3}  What NOT to do:{RS}')
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  {R3}\u2718{RS} Do not attack someone else\'s router or network')
    print(f'  {R3}\u2718{RS} Do not test any network without permission')
    print(f'  {R3}\u2718{RS} Do not run this on public WiFi or unknown networks')
    print(f'  {R3}\u2718{RS} Do not use this tool for illegal activity')
    print()
    print(f'  {C2}{LINE2}{RS}')
    print(f'  {G3}  What you SHOULD do:{RS}')
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  {G3}\u2714{RS} Only test your own or authorized networks')
    print(f'  {G3}\u2714{RS} Set up your own lab environment for learning')
    print(f'  {G3}\u2714{RS} Keep your router updated and disable WPS')
    print(f'  {G3}\u2714{RS} Use this tool for educational purposes only')
    print()
    print(f'  {C2}{LINE2}{RS}')
    print(f'  {Y3}  Legal notice:{RS}')
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  Attacking someone else\'s network without')
    print(f'  permission is {R3}illegal and punishable by law{RS}')
    print(f'  in most countries.')
    print()
    print(f'  This tool is built strictly for {G3}educational')
    print(f'  and authorized security testing{RS} purposes.')
    print()
    print(f'  {C2}{LINE2}{RS}')
    print(f'  {M3}  Developer:{RS}')
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  {W}DevZeron (Hasan){RS}')
    print(f'  GitHub  : {C3}ZeronModz{RS}')
    print(f'  Website : {C3}https://ZeronModz.netlify.app{RS}')
    print()
    print(f'  {TIP} {M3}DevZeron \u2014 Stay safe, stay ethical.{RS}')
    pause()

# ─────────────────────── Section 9 ───────────────────────

def section_zerfi_commands():
    fade_clear()
    gradient_banner()
    print()
    print(f'  {C3}{LINE}{RS}')
    type_text(f'  {Y3}9. Available zerfi Commands \u2014 Quick Reference{RS}', 0.025)
    print(f'  {C3}{LINE}{RS}')
    print()

    print(f'  {C2}{LINE2}{RS}')
    print(f'  {G3}  \u2500\u2500\u2500 Basic Commands \u2500\u2500\u2500{RS}')
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  {G3}zerfi{RS}')
    print(f'  \u2193 Run ZerFi with default settings')
    print(f'     (interface: wlan0, attack: Pixie Dust)')
    print()
    print(f'  {G3}zerfi menu{RS}')
    print(f'  \u2193 Open ZerFi interactive menu without auto-attack')
    print(f'     (runs: sudo python main.py)')
    print()
    print(f'  {G3}zerfi old{RS}')
    print(f'  \u2193 Run the old ZerFi engine (w1.py)')
    print(f'     (runs: sudo python w1.py -i wlan0 -K)')
    print()
    print(f'  {C2}{LINE2}{RS}')
    print(f'  {G3}  \u2500\u2500\u2500 Tool Management \u2500\u2500\u2500{RS}')
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  {G3}zerfi update{RS}')
    print(f'  \u2193 Fetch & install latest updates from GitHub')
    print()
    print(f'  {G3}zerfi help{RS}')
    print(f'  \u2193 Open this help guide')
    print()
    print(f'  {G3}zerfi fix{RS}')
    print(f'  \u2193 Fix root / superuser issues in Termux')
    print()
    print(f'  {G3}zerfi contact{RS}')
    print(f'  \u2193 Contact the developer (DevZeron)')
    print()
    print(f'  {C2}{LINE2}{RS}')
    print(f'  {G3}  \u2500\u2500\u2500 With Arguments (Advanced) \u2500\u2500\u2500{RS}')
    print(f'  {C2}{LINE2}{RS}')
    print()
    print(f'  {G3}zerfi -i wlan0 -b AA:BB:CC:DD:EE:FF -K{RS}')
    print(f'  \u2193 Pixie Dust on a specific router')
    print()
    print(f'  {G3}zerfi -i wlan0 -b AA:BB:CC:DD:EE:FF -B{RS}')
    print(f'  \u2193 Bruteforce on a specific router')
    print()
    print(f'  {G3}zerfi -i wlan0 -K --dts{RS}')
    print(f'  \u2193 Pixie Dust without touching Android WiFi settings')
    print()
    print(f'  {TIP} {M3}For full argument list, see option 5 (Command List).{RS}')
    pause()

# ── Main ──

def main():
    try:
        sys.stdout.write('\033[?25l')

        handlers = {
            '1': section_intro,
            '2': section_install,
            '3': section_interface,
            '4': section_attacks,
            '5': section_commands,
            '6': section_examples,
            '7': section_troubleshoot,
            '8': section_warnings,
            '9': section_zerfi_commands,
        }

        while True:
            choice = show_menu()
            if choice == '0':
                fade_clear()
                spinner(0.6, 'Exiting')
                print()
                print(f'  {M3}\u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510{RS}')
                print(f'  {M3}\u2551{RS}   {C3}\u2605{RS}  {W}DevZeron \u2014 Thanks for using ZerFi!{RS}  {C3}\u2605{RS}   {M3}\u2551{RS}')
                print(f'  {M3}\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518{RS}')
                print()
                sys.stdout.write('\033[?25h')
                sys.exit(0)
            elif choice in handlers:
                transition()
                handlers[choice]()
            else:
                print()
                print(f'  {WARN} {Y3}Invalid choice! Please try again.{RS}')
                time.sleep(1)

    except KeyboardInterrupt:
        print()
        print(f'\n  {Y3}Goodbye!{RS}')
        sys.stdout.write('\033[?25h')
        sys.exit(0)
    except Exception:
        sys.stdout.write('\033[?25h')
        sys.exit(1)

if __name__ == '__main__':
    main()
