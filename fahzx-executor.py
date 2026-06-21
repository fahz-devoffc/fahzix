#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# FahzX Executor v2 - Skull, FAHZX name, and DDoS launcher menu
# Now includes option to execute ddos.py with target URL

import os
import sys
import platform
import subprocess

def set_terminal_title(title):
    """Set terminal title cross-platform."""
    try:
        if os.name == 'nt':
            os.system(f'title {title}')
        else:
            sys.stdout.write(f"\033]0;{title}\007")
            sys.stdout.flush()
    except Exception:
        pass

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    skull = r"""
                           .-"-.
                          /|6 6|\
                         {/(_0_)\}
                          _/ ^ \_
                         (/ /^\ \)-'
                          ""' '""
    """
    fahzx_name = r"""
    ########     ###     ##   ##   ########   ##   ##
    ##          ## ##    ##   ##      ##       ## ##
    ######     ##   ##   #######      ##        ###
    ##         #######   ##   ##      ##       ## ##
    ##        ##     ##  ##   ##   ########   ##   ##
    """
    print("=" * 60)
    print("       FAHZX EXECUTOR v2.0 - Armed")
    print("=" * 60)
    print(skull)
    print(fahzx_name)
    print("=" * 60)
    print("   Terminal : Fahzx Terminal")
    print("   System   :", platform.system(), platform.release())
    print("=" * 60)

def run_ddos():
    """Launch ddos.py with target URL from user input."""
    target = input("\n[?] Target URL (e.g., https://example.com): ").strip()
    if not target:
        print("[!] No target, cancelling.")
        return
    script_path = os.path.join(os.path.dirname(__file__), "ddos.py")
    if not os.path.exists(script_path):
        print(f"[!] ddos.py not found at {script_path}. Make sure it's in the same folder.")
        return
    print(f"[*] Launching DDoS attack on {target}...\n")
    try:
        subprocess.run([sys.executable, script_path, target], check=False)
    except Exception as e:
        print(f"[!] Failed to execute ddos.py: {e}")

def main():
    set_terminal_title("Fahzx Terminal")
    clear_screen()
    show_banner()
    while True:
        print("\n--- MENU ---")
        print("1. Run DDoS Attack (ddos.py)")
        print("2. Exit")
        choice = input(">> ").strip()
        if choice == '1':
            run_ddos()
        elif choice == '2':
            print("[*] Exiting... Stay dangerous.")
            break
        else:
            print("[!] Pick 1 or 2, bro.")

if __name__ == "__main__":
    main()
