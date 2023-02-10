import sqlite3, colorama, os
from pystyle import Anime, Colors, Center, Colorate
from colorama import Fore
colorama.init(autoreset=True)

logo = """
██████  ██████      ███████ ███████  █████  ██████   ██████ ██   ██ ███████ ██████  
██   ██ ██   ██     ██      ██      ██   ██ ██   ██ ██      ██   ██ ██      ██   ██ 
██   ██ ██████      ███████ █████   ███████ ██████  ██      ███████ █████   ██████  
██   ██ ██   ██          ██ ██      ██   ██ ██   ██ ██      ██   ██ ██      ██   ██ 
██████  ██████      ███████ ███████ ██   ██ ██   ██  ██████ ██   ██ ███████ ██   ██ 
                                                                                    
                                                                                
"""
Anime.Fade(text=Center.Center(logo), color=Colors.black_to_green, mode=Colorate.Vertical, time=2)

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def search(path, table, string):
    if not os.path.exists(path):
        print(f"{Fore.LIGHTRED_EX}[\] This file or directory does not exists! ({path})")
        exit()
    try:
        con = sqlite3.connect(path)
        cur = con.cursor()
        cnt = 0
        for row in cur.execute(f"SELECT * FROM {table}"):
            for i in row:
                if string == i:
                    cnt += 1
                    print(f"{Fore.LIGHTGREEN_EX}[+] FOUND: {row}")
                elif string in i:
                    cnt += 1
                    print(f"{Fore.LIGHTYELLOW_EX}[~] MAYBE FOUND: {row}")
        if cnt == 0:
            print(f"{Fore.LIGHTRED_EX}[-] STRING `{string}` NOT FOUND IN TABLE `{table}` ({path})")
        else:
            print(f"{Fore.LIGHTGREEN_EX}[#] x{str(cnt)} STRING `{string}` FOUND IN TABLE `{table}` ({path})")
    except sqlite3.Error as er:
        print(f"{Fore.LIGHTRED_EX}[\] An error occurred! ({path}): {er}")

if __name__ == "__main__":
    clear()
    choice = input(f"{Fore.LIGHTMAGENTA_EX}One or multiples files? (1: one/2: multiples): ")
    clear()
    if choice == ("1" or "01"):
        path = input(f"{Fore.LIGHTMAGENTA_EX}Drag the database here: ")
        choicet = input(f"{Fore.LIGHTMAGENTA_EX}One or multiples tables? (1: one/2: multiples):")
        count = 0
        if choicet == ("1" or "01"):
            string = input(f"{Fore.LIGHTMAGENTA_EX}Enter the string you want to search: ")
            table = input(f"{Fore.LIGHTMAGENTA_EX}Enter the name of the table: ")
            search(path, table, string)
        else:
            count += 1
            while(True):
                string = input(f"{Fore.LIGHTMAGENTA_EX}(x{count}) Enter the string you want to search: ")
                table = input(f"{Fore.LIGHTMAGENTA_EX}(x{count}) Enter the name of the table: ")
                search(path, table, string)
    elif choice == ("2" or "02"):
        clear()
        folder = input(f"{Fore.LIGHTMAGENTA_EX}Drag the folder with the databases on it here: ")
        choicet = input(f"{Fore.LIGHTMAGENTA_EX}One or multiples tables? (1: one/2: multiples):")
        count = 0
        if choicet == ("1" or "01"):
            string = input(f"{Fore.LIGHTMAGENTA_EX}Enter the string you want to search: ")
            table = input(f"{Fore.LIGHTMAGENTA_EX}Enter the name of the table: ")
            for file in os.listdir(folder):
                search(f"{folder}/{file}", table, string)
        elif choicet == ("2" or "02"):
            clear()
            for file in os.listdir(folder):
                count = 0
                number = input(f"{Fore.LIGHTMAGENTA_EX}Enter the number of time you wanna search in the db ({file}): ")
                for i in range(int(number)):
                    count += 1
                    string = input(f"{Fore.LIGHTMAGENTA_EX}(x{count}) ({file}) Enter the string you want to search: ")
                    table = input(f"{Fore.LIGHTMAGENTA_EX}(x{count}) ({file}) Enter the name of the table: ")
                    search(f"{folder}/{file}", table, string)
        else:
            print(f"{Fore.LIGHTRED_EX}Invalid choice")
            exit()
    else:
        print(f"{Fore.LIGHTRED_EX}Invalid choice")
        exit()
