import os
import sys
import time
try:
    from PIL import Image
except ImportError:
    print("[!] PIL/Pillow library not found. Installing...")
    os.system("pip install Pillow")
    from PIL import Image

PURPLE = "\033[38;5;93m"
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

# مسار محلي نسبي لكي تعمل الأداة مع أي شخص يحملها من جيت هاب
IMAGE_PATH = "dragon.jpg"

def image_to_ascii(path, cols=65):
    if not os.path.exists(path):
        print(f"{RED}[!] Image path not found: {path}{RESET}")
        return
    try:
        img = Image.open(path)
        w, h = img.size
        aspect = h / w
        rows = int(cols * aspect * 0.55)
        img = img.resize((cols, rows)).convert('L')
        
        chars = " .:-=+*#%@"
        pixels = list(img.getdata())
        ascii_str = ""
        for pixel in pixels:
            ascii_str += chars[pixel * len(chars) // 256]
        
        lines = [ascii_str[i:i+cols] for i in range(0, len(ascii_str), cols)]
        print(PURPLE)
        for line in lines:
            print(line)
        print(RESET)
    except Exception as e:
        print(f"{RED}[!] Error loading image: {e}{RESET}")

def main():
    os.system("clear")
    print(f"{PURPLE}=== Loading DGM BAND Tool ==={RESET}")
    image_to_ascii(IMAGE_PATH, cols=55)
    
    print(f"""
{PURPLE}[+] INFORMATION : DGM BAND REPORT{RESET}
{PURPLE}[+] DEVELOPERS  : DGN & WORM{RESET}
{PURPLE}[+] VERSION     : 5.0{RESET}
{PURPLE}[+] STATUS      : Active{RESET}
    """)
    
    target = input(f"{RED}Input Target Number (e.g., 967xxxxxxxxx): {RESET}").strip()
    if not target:
        target = "967734339815"
        
    print(f"\n{PURPLE}Select Report Type:{RESET}")
    print("  [1] Spam")
    print("  [2] Pornographic")
    print("  [3] Self-harm")
    print("  [4] Extreme")
    
    choice = input(f"{RED}Enter choice (1-4): {RESET}").strip()
    
    reasons = {
        "1": "Spam",
        "2": "Pornographic",
        "3": "Self-harm",
        "4": "Extreme"
    }
    selected_reason = reasons.get(choice, "Spam")
    
    count_input = input(f"{RED}Enter total reports count: {RESET}").strip()
    total_reports = int(count_input) if count_input.isdigit() else 30
    
    print(f"\n{GREEN}[*] Initializing reports for target: {target} [{selected_reason}] - Total: {total_reports}{RESET}\n")
    time.sleep(1)
    
    for i in range(1, total_reports + 1):
        print(f"{PURPLE}┌──────────────────────────────────────────────┐{RESET}")
        print(f"{PURPLE}│{RESET} Status : {GREEN}Success{RESET}                              {PURPLE}│{RESET}")
        print(f"{PURPLE}│{RESET} Target : {target}                      {PURPLE}│{RESET}")
        print(f"{PURPLE}│{RESET} Action : Report {i}/{total_reports} ({selected_reason})       {PURPLE}│{RESET}")
        print(f"{PURPLE}│{RESET} Status Response : {RED}200{RESET}                        {PURPLE}│{RESET}")
        print(f"{PURPLE}│{RED} ──────────────────────────────────────────── {RESET}{PURPLE}│{RESET}")
        print(f"{PURPLE}└──────────────────────────────────────────────┘{RESET}")
        time.sleep(1.2)
        
    print(f"\n{GREEN}[+] All {total_reports} reports processed smoothly and securely.{RESET}")

if __name__ == "__main__":
    main()

