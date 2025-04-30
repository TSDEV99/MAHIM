import requests
import os
import sys
import shutil
import time
from datetime import datetime, timedelta
import random
import threading
import getpass
from datetime import datetime

# Set your expiry date (YYYY, MM, DD)
expiry_date = datetime(2025, 5, 8)

# Get the current date
current_date = datetime.now()

# Check if the script has expired
if current_date > expiry_date:
    print("This script has expired.")
    exit()  # Stops the script
else:
    print("Script is running. Expiry date:", expiry_date)

# Define colors using ANSI escape sequences
RESET = "\033[0m"
BOLD = "\033[1m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_YELLOW = "\033[93m"
WHITE = "\033[97m"
BRIGHT_RED = "\033[91m"
BROWN = "\033[38;5;94m"  # ANSI code for brown color

# ANSI color codes
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"

# Gold ANSI color using 256-color mode (approximate gold shades)
gold_ansi_256 = "\033[38;5;220m"  # Gold-like color (orange-yellow shade)
reset = "\033[0m"

def to_monospace(text):
    result = ''
    for char in text:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 0x1D670 - ord('A'))
        elif 'a' <= char <= 'z':
            result += chr(ord(char) + 0x1D68A - ord('a'))
        elif '0' <= char <= '9':
            result += chr(ord(char) + 0x1D7F6 - ord('0'))
        else:
            result += char
    return result


# Clear the screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Animated typing effect
def type_banner(text, delay=0.005):
    clear_screen()
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Move to a new line at the end

    
def typing_effect(text, delay=0.009):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() 

# Function to show animated loading
def animated_loading(message, duration=3):
    chars = ["|", "-", "|", "-"]
    start_time = time.time()
    while time.time() - start_time < duration:
        for char in chars:
            sys.stdout.write(f"\r{BRIGHT_YELLOW}{BOLD}{message} {char}{RESET}")
            sys.stdout.flush()
            time.sleep(0.2)
    sys.stdout.write("\r" + " " * (len(message) + 2) + "\r")  # Clear line

# gmail_login_manual.py

email = input("Enter Gmail: ")
password = input("Enter Password: ")

if email == "mahim@gmail.com" and password == "Mahim":
    print("Login successful!")
else:
    print("Invalid credentials.")


# Clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

# Display the first banner
today_date = datetime.now().strftime("%m - %d - %Y")

def display_banner():
    banner = f"""
⠀⠀⠀
{gold_ansi_256}
██████████████████████████████████████████████████████████████████████████████████
████████╗ █████╗ ██████╗ ██╗  ██╗    ██████╗ ██████╗  ██████╗ 
╚══██╔══╝██╔══██╗██╔══██╗╚██╗██╔╝    ██╔══██╗██╔══██╗██╔═══██╗
   ██║   ╚█████╔╝██████╔╝ ╚███╔╝     ██████╔╝██████╔╝██║   ██║
   ██║   ██╔══██╗██╔══██╗ ██╔██╗     ██╔═══╝ ██╔══██╗██║   ██║
   ██║   ╚█████╔╝██║  ██║██╔╝ ██╗    ██║     ██║  ██║╚██████╔╝
   ╚═╝    ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ 
██████████████████████████████████████████████████████████████████████████████████
{RESET}
"""
    # center each line based on terminal width
    try:
        width = shutil.get_terminal_size().columns
    except OSError:
        width = 120
    for line in banner.splitlines():
        print(line.center(width))

# determine console width (fallback to 120)
try:
    console_width = shutil.get_terminal_size().columns
except OSError:
    console_width = 120

def center_text(text, width):
    lines = text.split('\n')
    return '\n'.join(line.center(width) for line in lines)

developer_info_raw = f"""
{BOLD}{BRIGHT_BLUE} ☠𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗧𝗢 𝗧𝗛𝗘 𝗞𝗜𝗡𝗚 𝗢𝗙 𝗙𝗨𝗧𝗨𝗥𝗘 𝗦𝗜𝗚𝗡𝗔𝗟 𝗦𝗢𝗙𝗧𝗪𝗔𝗥𝗘 𝗧𝟴𝗥𝗫 𝗣𝗥𝗢☠
{BOLD}{BRIGHT_BLUE} 😈𝐓𝐇𝐄 𝐒𝐎𝐅𝐓𝐖𝐀𝐑𝐄 𝐀𝐍𝐃 𝐓𝐇𝐄 𝐂𝐑𝐄𝐀𝐓𝐎𝐑 𝐁𝐄𝐋𝐈𝐄𝐕𝐄 𝐐𝐔𝐀𝐋𝐈𝐓𝐘 𝐎𝐑 𝐐𝐔𝐀𝐍𝐓𝐈𝐓𝐘😈

{BOLD}{BRIGHT_CYAN} 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 𝗕𝗬 𝗧𝗢𝗪𝗦𝗜𝗙
{BOLD}{BRIGHT_CYAN} 𝗦𝗢𝗙𝗧𝗪𝗔𝗥𝗘 𝗡𝗔𝗠𝗘 :- 𝗧𝟴𝗥𝗫 𝗣𝗥𝗢
{BOLD}{BRIGHT_CYAN} 𝗠𝗔𝗜𝗡 𝗗𝗘𝗩𝗢𝗟𝗣𝗘𝗥 :- 𝗠𝗔𝗛𝗜𝗠 𝗫𝗬𝗭
{BOLD}{BRIGHT_RED} ''𝗛𝗘𝗬 𝗘𝗩𝗘𝗥𝗬𝗢𝗡𝗘 𝗬𝗢𝗨 𝗖𝗔𝗡 𝗕𝗘 𝗞𝗜𝗡𝗚 ... 𝗕𝗨𝗧 𝗬𝗢𝗨 𝗙𝗜𝗥𝗦𝗧 𝗙𝗢𝗟𝗟𝗢𝗪 𝗗𝗜𝗦𝗖𝗜𝗣𝗟𝗜𝗡𝗘''
{BOLD}{BRIGHT_YELLOW} <═══════════════════════>> ۩ 𝗪𝗢𝗥𝗟𝗗 𝗨𝗡𝗜𝗧 𝟭 1 ۩ <<═══════════════════════>

{BOLD}{BRIGHT_CYAN}   ═════════════════════════════════════════════════════════════════════════════════
{BOLD}{WHITE}𝗦𝗜𝗡𝗖𝗘 𝟮𝟬𝟮𝟱
{BOLD}{WHITE} Current Date in Bangladesh :: {today_date}
{BOLD}{BRIGHT_CYAN}   ═════════════════════════════════════════════════════════════════════════════════

{RESET}
"""


# Display banner and developer info
display_banner()
# center each line and print
print(center_text(developer_info_raw, console_width))

# Function to terminate the program after a set time
def terminate_program():
    print(RED + "\nTime's up! The program is terminating." + RESET)
    sys.exit(0)
    
print(f"{BRIGHT_RED}{BOLD}۩ HI THERE WELCOME BACK TO T8RX PRO ۩")
pairs = input(f"\n{BOLD}{WHITE}[☆] ENTER PAIR NAME : ")
selected_pairs = pairs
days = input(f"{BOLD}{BRIGHT_CYAN}[☆] NUMBER OF DAY ANALYSIS : ")
selected_days = days

# Clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

# Display banner and developer info
display_banner()
# center each line and print
print(center_text(developer_info_raw, console_width))

typing_effect(f"\n{BRIGHT_YELLOW}{BOLD}➪Your Pairs Choice : {selected_pairs}{RESET}", delay=0.0009)
animated_loading("DATA LOADING. ....", duration=1)
typing_effect(f"{BRIGHT_YELLOW}{BOLD}➪Your Day Analysis Choice : {selected_days}{RESET}", delay=0.0009)
animated_loading("Send Selection Choice In Api. ....", duration=2)

typing_effect(f"\n{BRIGHT_BLUE}{BOLD}SIGNAL FILTER INPUT: -{RESET}", delay=0.02)

timeframe = input(f"\n{BOLD}{BRIGHT_YELLOW}[☆] ENTER TIMEFRAME (M1, M5, etc.): ")
selected_timeframe = timeframe
percentage = input(f"{BOLD}{BRIGHT_BLUE}[☆] ENTER YOUR ACCURACY RATE: ")
selected_percentage = percentage

# Strategy1 Selection
strategy1_choice = input(f"{WHITE}{BOLD}[☆] ENTER YOUR STRATEGY CHOICE(1: RSI, 2: MACD, 3: ATR, 4: ADX, 5: MOVING AVERAGE 6:ACTIVE ALL): {RESET}")

# Validate Strategy1 choice
if strategy1_choice == "1":
    selected_strategy1 = "RSI"
elif strategy1_choice == "2":
    selected_strategy1 = "MACD"
elif strategy1_choice == "3":
    selected_strategy1 = "ATR"
elif strategy1_choice == "4":
    selected_strategy1 = "ADX"    
elif strategy1_choice == "5":
    selected_strategy1 = "MOVING AVERAGE"
elif strategy1_choice == "6":
    selected_strategy1 = "ACTIVE ALL"
else:
    typing_effect(f"{BRIGHT_MAGENTA}{BOLD}Invalid choice! Defaulting to ACTIVE ALL.{RESET}", delay=0.05)
    selected_strategy1 = "ACTIVE ALL" 

# Strategy Selection
strategy3_choice = input(f"{BRIGHT_MAGENTA}{BOLD}[☆] MARTINGALE COUNT : {RESET}")

# Validate Strategy3 choice
if strategy3_choice == "0":
    selected_strategy3 = "NON MTG"
elif strategy3_choice == "1":
    selected_strategy3 = "1 STEP MAX"
else:
    typing_effect(f"{BRIGHT_MAGENTA}{BOLD}Invalid choice! Defaulting to 00 MARTINGALE.{RESET}", delay=0.05)
    selected_strategy3 = "0"
    
    
# Strategy Selection
strategy9_choice = input(f"{BRIGHT_MAGENTA}{BOLD}[☆] YOUR TIME ZONE : {RESET}")

# Validate Strategy9 choice
if strategy9_choice == "1":
    selected_strategy9 = "UTC +06:00"
elif strategy9_choice == "2":
    selected_strategy9 = "UTC -03:00"
else:
    strategy9_choice = input(f"{BRIGHT_MAGENTA}{BOLD}[☆] YOUR TIME ZONE : {RESET}")
    selected_strategy9 = strategy9_choice   
    
start_time = input(f"{BOLD}{BRIGHT_BLUE}[☆] ENTER START TIME: ")
selected_start_time = start_time
end_time = input(f"{BOLD}{WHITE}[☆] ENTER END TIME : ")
selected_end_time = end_time

animated_loading("LOADING YOUR SIGNAL DATA ....", duration=4)

# Clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

# Display banner and developer info
display_banner()
# center each line and print
print(center_text(developer_info_raw, console_width))
    
typing_effect(f"{BRIGHT_CYAN}{BOLD}SIGNAL MAKING INPUT DETAILS : -{RESET}", delay=0.05)
animated_loading("DATA LOADING. ....", duration=1)
typing_effect(f"{WHITE}{BOLD}  Your Pairs Choice : {selected_pairs}{RESET}", delay=0.01)
animated_loading("DATA LOADING. ....", duration=1)
print(f"{WHITE}{BOLD}  Your Day Analysis Choice : {selected_days}{RESET}")
animated_loading("DATA LOADING. ....", duration=1)
print(f"{WHITE}{BOLD}  Your Timeframe Choice : {selected_timeframe}{RESET}")
animated_loading("DATA LOADING. ....", duration=1)
print(f"{WHITE}{BOLD}  Your Accuracy Choice : {selected_percentage}{RESET}")
animated_loading("DATA LOADING. ....", duration=1)
print(f"{WHITE}{BOLD}  Your Accuracy Filter Choice : {selected_strategy1}{RESET}")
animated_loading("DATA LOADING. ....", duration=1)
print(f"{WHITE}{BOLD}  Start Of The List: {selected_start_time}{RESET}")
animated_loading("DATA LOADING. ....", duration=1)
print(f"{WHITE}{BOLD}  End Of The List : {selected_end_time}{RESET}\n")

api_url = f"https://tahsinshort.top/tahsinpr/apid.php?pair={pairs}&days={days}&{timeframe}=true&percentage={percentage}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def fetch_signals(url, start_time, end_time):
    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        if "signals" in data and isinstance(data["signals"], list):
            start_dt = datetime.strptime(start_time, "%H:%M")
            end_dt = datetime.strptime(end_time, "%H:%M")

            filtered_signals = [
                f"║  {to_monospace(signal['Time'].upper())} {to_monospace(signal['TimeExpiration'].upper())}; " +
                f"{to_monospace(signal['Pair'].upper().replace('_OTC', '-OTC'))} {to_monospace(signal['Direction'].upper())}"
                for signal in data["signals"]
                if start_dt <= datetime.strptime(signal["Time"], "%H:%M") <= end_dt
            ]

            return "\n".join(filtered_signals) if filtered_signals else "NO SIGNALS FOUND WITHIN THE SELECTED TIME RANGE."
        else:
            return "NO SIGNALS FOUND."

    except Exception as e:
        return f"ERROR: {str(e).upper()}"

signals_output = fetch_signals(api_url, start_time, end_time)
print(f"\n{BOLD}{BRIGHT_CYAN}▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭{RESET}")
typing_effect(f"{BOLD}{BRIGHT_CYAN}  ┣ {today_date}{RESET}", delay=0.01)
typing_effect(f"{BOLD}{BRIGHT_CYAN}  ┣ 𝗨𝗧𝗖 +𝟬𝟲:𝟬𝟬  𝗧𝗜𝗠𝗘𝗙𝗥𝗔𝗠𝗘: {selected_timeframe}{RESET}", delay=0.01)
typing_effect(f"{BOLD}{BRIGHT_CYAN}  ┣ 𝗧𝗜𝗠𝗘𝗙𝗥𝗔𝗠𝗘: {selected_timeframe}{RESET}", delay=0.01)
typing_effect(f"{BOLD}{BRIGHT_CYAN}  ┣ 𝟭 𝗦𝗧𝗘𝗣 𝗠𝗧𝗚{RESET}", delay=0.01)
typing_effect(f"{BOLD}{BRIGHT_CYAN}  ┣ ☠ APOLLO BELIEVE QUALITY ☠{RESET}", delay=0.01)
print(f"{BOLD}{BRIGHT_CYAN}▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭▭{RESET}")
animated_loading("LOADING DATA. ....", duration=4)
animated_loading("ANALYSIS YOUR PAIRS . ....", duration=1)
animated_loading("APPLIED ALL SETTING AND FILTER. ....", duration=1)
animated_loading("COLLECTING SIGNAL FROM TOWSIF API. ....", duration=2)
animated_loading("YOUR SIGNALS COMING WITHING 5 SEC. ....", duration=4)
print(f"\n{BOLD}{BRIGHT_BLUE}╔═━━━━━━━━━━ ◣◆◢ ━━━━━━━━━━═╗{RESET}")
print(f"\n{WHITE}{BOLD}")
print(signals_output)
print(f"\n{BOLD}{BRIGHT_BLUE}╚═━━━━━━━━━━ ◣◆◢ ━━━━━━━━━━═╝{RESET}")
print(f"\n{BRIGHT_YELLOW}{BOLD}------------------------------------------------------------{RESET}")
print(f"{BRIGHT_YELLOW}{BOLD}       ➪𝙳𝚘𝚓𝚒 𝙰𝚟𝚘𝚒𝚍 - 𝙰𝚟𝚘𝚒𝚍 𝙶𝚊𝚙 𝚄𝚙/𝙳𝚘𝚠𝚗 ⓘ{RESET}")
print(f"{BRIGHT_YELLOW}{BOLD}       ➪𝙰𝚟𝚘𝚒𝚍 𝙰𝚏𝚝𝚎𝚛 𝙰 𝙱𝚒𝚐 𝙲𝚊𝚗𝚍𝚎𝚕 𝙾𝚙𝚙𝚘𝚜𝚒𝚝𝚎 𝚃𝚛𝚎𝚗𝚍 ⓘ{RESET}")
print(f"{BRIGHT_YELLOW}{BOLD}       ➪𝚃𝚊𝚔𝚎 𝚂𝚎𝚏𝚝𝚢 𝙼𝚊𝚛𝚐𝚒𝚗 𝙸𝚏 𝙿𝚘𝚜𝚜𝚒𝚋𝚕𝚎 ⓘ{RESET}")
print(f"{BRIGHT_YELLOW}{BOLD}       ➪𝙰𝚟𝚘𝚒𝚍 𝙱𝟸𝙱 𝟹 𝙾𝚙𝚙𝚘𝚜𝚒𝚝𝚎 𝚅𝚎𝚛𝚢 𝚑𝚎𝚊𝚕𝚝𝚑𝚢 𝙲𝚊𝚗𝚍𝚎𝚕 ⓘ{RESET}")
print(f"\n{BRIGHT_YELLOW}{BOLD}------------------------------------------------------------{RESET}")
print(f"\n{BOLD}{BRIGHT_MAGENTA}         ======╡T8RX SIGNALS LIST END╞======{RESET}")
print(f"\n{BOLD}{BRIGHT_CYAN}            ♡♡THANKS FOR USEING T8RX SOFT♡♡{RESET}")
print(f"\n{BOLD}{BRIGHT_CYAN}              PRESS 《 C 》 FOR COPY SIGNALS{RESET}")
# Copy to clipboard using Termux API
while True:
    choice = input(f"{BOLD}{BRIGHT_CYAN}TYPE《C》~~~~~》》:").strip().upper()
    
    if choice == 'C':
        os.system(f'echo "{signals_output}" | termux-clipboard-set')
        print(f"{BOLD}{BRIGHT_CYAN} Signals copied to clipboard!{RESET}")
    
timer = threading.Timer(120, terminate_program)
timer.start()
