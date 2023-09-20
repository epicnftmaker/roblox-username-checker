


import requests
import json
import threading
import colorama
from colorama import Fore, Back, Style, init
import time


def check_username(username):
    url = 'https://users.roblox.com/v1/usernames/users/'

    payload = {
        "usernames": [username]
    }

    response = requests.post(url, json=payload)
    response_data = json.loads(response.text)

    if response_data.get('data') == []:
        print(Fore.GREEN + 'vaild goodjob homie')
        with open("valid.txt", 'a') as valid_file:
            valid_file.write(username + "\n")
    else:
        print(Fore.RED + 'taken L')

def main(file_path, num_threads):
    threads = []

    with open(file_path, 'r') as file:
        for line in file:
            username = line.strip()  
            
            thread = threading.Thread(target=check_username, args=(username,))
            threads.append(thread)
            thread.start()

            if len(threads) >= num_threads:
                for thread in threads:
                    thread.join()
                threads = []

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    file_path = "usernames.txt"
    print(Fore.MAGENTA + '''
    
  ________              __            
 / ____/ /_  ___  _____/ /_____  _____
/ /   / __ \/ _ \/ ___/ //_/ _ \/ ___/
/ /___/ / / /  __/ /__/ ,< /  __/ /    
\____/_/ /_/\___/\___/_/|_|\___/_/     
                                       

made by epicnftmaker                  
          ''')
    
    time.sleep(2)    
    
    num_threads = int(input(Fore.MAGENTA + "Enter the number of threads: "))

    main(file_path, num_threads)

