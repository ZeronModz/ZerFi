#!/data/data/com.termux/files/usr/bin/bash

# Colors for output
GREEN="\033[1;32m"
YELLOW="\033[1;33m"
RESET="\033[0m"

echo -e "${GREEN}[+] Updating packages...${RESET}"
pkg update -y && pkg upgrade -y

echo -e "${GREEN}[+] Installing required packages...${RESET}"
pkg install root-repo -y
pkg install git tsu python wpa-supplicant pixiewps iw -y

# Check directory and clone
if [ ! -d "ZerFi" ] && [ ! -f "main.py" ]; then
    echo -e "${GREEN}[+] Cloning ZerFi repository...${RESET}"
    git clone https://github.com/ZeronModz/ZerFi
    cd ZerFi || exit
elif [ -d "ZerFi" ]; then
    cd ZerFi || exit
fi

echo -e "${GREEN}[+] Installing Python dependencies...${RESET}"
pip install -r requirements.txt --break-system-packages

chmod +x main.py

echo -e "${GREEN}[+] Setting up 'zerfi' command...${RESET}"

BIN_DIR="$PREFIX/bin"
ZERFI_BIN="$BIN_DIR/zerfi"
SCRIPT_DIR="$(pwd)"

cat > "$ZERFI_BIN" <<EOF
#!/data/data/com.termux/files/usr/bin/bash
cd "$SCRIPT_DIR" || exit

# Update Logic
if [ "\$1" == "update" ]; then
    echo -e "\033[1;32m[+] Update disabled — DevZeron Edition\033[0m"
    exit 0
fi

# Help Logic
if [ "\$1" == "help" ]; then
    python help.py
    exit 0
fi

# Fix Logic
if [ "\$1" == "fix" ]; then
    bash fix.sh
    exit 0
fi

# Contact Logic
if [ "\$1" == "contact" ]; then
    python contact.py
    exit 0
fi

# Menu Logic
if [ "\$1" == "menu" ]; then
    sudo python main.py
    exit 0
fi

# Old Logic
if [ "\$1" == "old" ]; then
    sudo python w1.py -i wlan0 -K
    exit 0
fi

# Run Logic
if [ -z "\$1" ]; then
    sudo python main.py -i wlan0 -K
else
    sudo python main.py "\$@"
fi
EOF

chmod +x "$ZERFI_BIN"

echo -e "\n${GREEN}[✓] Setup complete successfully!${RESET}"
echo -e "${YELLOW}[✓] You don't even need to restart Termux.${RESET}"

echo -e "\n\033[1;36m╔══════════════════════════════════════════════╗\033[0m"
echo -e "\033[1;36m║           📌  READ THIS CAREFULLY            ║\033[0m"
echo -e "\033[1;36m╚══════════════════════════════════════════════╝\033[0m"
echo -e "\033[1;33m  ⚠️  Take a screenshot of the info below now!\033[0m"
echo -e "\033[1;33m     You may need it later. Save it somewhere.\033[0m"

echo -e "\n\033[1;32m  ┌─ Available Commands ──────────────────────┐\033[0m"
echo -e "\033[1;32m  │\033[0m  \033[1;37mzerfi\033[0m         → Run ZerFi (main tool)"
echo -e "\033[1;32m  │\033[0m  \033[1;37mzerfi update\033[0m  → Update ZerFi to latest version"
echo -e "\033[1;32m  │\033[0m  \033[1;37mzerfi help\033[0m    → Show help & usage info"
echo -e "\033[1;32m  │\033[0m  \033[1;37mzerfi fix\033[0m     → Fix root/superuser issues"
echo -e "\033[1;32m  │\033[0m  \033[1;37mzerfi contact\033[0m → Contact the developer (DevZeron)"
echo -e "\033[1;32m  │\033[0m  \033[1;37mzerfi menu\033[0m    → Run ZerFi interactive menu"
echo -e "\033[1;32m  │\033[0m  \033[1;37mzerfi old\033[0m     → Run ZerFi old engine (w1.py)"
echo -e "\033[1;32m  └───────────────────────────────────────────┘\033[0m"

echo -e "\n\033[1;31m  ⚡ IMPORTANT — If 'zerfi' shows:\033[0m"
echo -e "\033[1;37m     \"no superuser binary detected\"\033[0m"
echo -e "\033[1;33m  → First try:   \033[1;37mzerfi fix\033[0m"
echo -e "\033[1;33m  → Still broken? Visit this link for 3 fix methods:\033[0m"
echo -e "\033[1;36m     https://github.com/ZeronModz/fix-termux-root\033[0m"
echo -e "\033[1;33m  → Copy or screenshot that link right now!\033[0m"

echo -e "\n\033[1;36m══════════════════════════════════════════════\033[0m"
echo -e "\033[1;32m  ✅ All done! Type 'zerfi' to get started.\033[0m"
echo -e "\033[1;36m══════════════════════════════════════════════\033[0m\n"
