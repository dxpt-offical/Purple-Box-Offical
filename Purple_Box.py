import os
import platform
import sys
import subprocess
import time
from threading import Thread
from colorama import Fore, Style, init
init()

def main():
    os_type = platform.system() + " " + platform.release()
    print(Fore.MAGENTA + f"OS: {os_type}")
    print(Fore.MAGENTA + "██████  ██    ██ ██████  ██████  ██      ███████     ██████   ██████  ██   ██ ")
    print(Fore.MAGENTA + "██   ██ ██    ██ ██   ██ ██   ██ ██      ██          ██   ██ ██    ██  ██ ██  ")
    print(Fore.MAGENTA + "██████  ██    ██ ██████  ██████  ██      █████       ██████  ██    ██   ███   ")
    print(Fore.MAGENTA + "██      ██    ██ ██   ██ ██      ██      ██          ██   ██ ██    ██  ██ ██  ")
    print(Fore.MAGENTA + "██       ██████  ██   ██ ██      ███████ ███████     ██████   ██████  ██   ██ ")
    print(Fore.MAGENTA + "Enter command or enter 'exit' to exit this program ||")

    while True:
        user_command = input(">> ")
        
        if user_command.lower() == "s -animation --2":
            animate_colors("Переливающийся текст")
        
        elif user_command.lower() == "s -animation --1":
            spinner_animation()

        elif user_command.lower() == "info":
            print(Fore.MAGENTA + "This version created on Python!")
            print(Fore.MAGENTA + "Created by @SEX_KILLS (only tg)")
            print(Fore.MAGENTA + "Version :: 1.1.7")
            print(Fore.MAGENTA + "Check 'Purple Box' on Github!")
        
        elif user_command.lower() == "s gift":
            print(Fore.MAGENTA + "Ты че ахуел, нельзя.")

        elif user_command.lower() == "s exsquad":
            print(Fore.MAGENTA + "Подпишитесь на EX SQUAD :>")

        elif user_command.lower() == "box":
            display_system_info()
        
        elif user_command.lower() == "exit":
            break
        
        elif user_command.lower() == "clear":
            os.system("clear" if os.name == "posix" else "cls")
        
        else:
            execute_command(user_command)

def animate_colors(text):
    colors = ["\033[91m", "\033[93m", "\033[92m", "\033[96m", "\033[94m", "\033[95m"]
    start_time = time.time()
    while time.time() - start_time < 4:
        for color in colors:
            if time.time() - start_time >= 4:
                break
            sys.stdout.write(f"\r{color}{text}")
            sys.stdout.flush()
            time.sleep(0.2)

def spinner_animation():
    spinner = ["|", "/", "-", "\\"]
    start_time = time.time()
    while time.time() - start_time < 4:
        for char in spinner:
            if time.time() - start_time >= 4:
                break
            sys.stdout.write(f"\r{char}")
            sys.stdout.flush()
            time.sleep(0.2)


def display_system_info():
    architecture = "64-bit" if sys.maxsize > 2**32 else "32-bit"
    print(Fore.MAGENTA + f"Архитектура ОС: {architecture}")
    print(Fore.MAGENTA + f"Имя компьютера: {platform.node()}")
    print(Fore.MAGENTA + f"Имя пользователя: {os.getlogin()}")
    print(Fore.MAGENTA + f".NET версия (аналог): {platform.python_version()}")
    total_memory = round(os.sysconf(Fore.MAGENTA + 'SC_PAGE_SIZE') * os.sysconf(Fore.MAGENTA + 'SC_PHYS_PAGES') / (1024**2))
    print(Fore.MAGENTA + f"Общий объем памяти: {total_memory} MB")

def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print("E: " + result.stderr)
    except Exception as e:
        print(Fore.MAGENTA + "E:", e)

if __name__ == "__main__":
    main()
