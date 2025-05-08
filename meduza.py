import requests
from colorama import Fore, init
import re
import sys
import meduza
import time
import threading
import os
import random
import json
from bs4 import BeautifulSoup


init(autoreset=True)
os.system("title Meduza Terminal")

ascii_art = r"""
 ┳┳┓┏┓┳┓┳┳┏┓┏┓
 ┃┃┃┣ ┃┃┃┃┏┛┣┫
 ┛ ┗┗┛┻┛┗┛┗┛┛┗
┏┳┓┏┓┳┓┳┳┓┳┳┓┏┓┓
 ┃ ┣ ┣┫┃┃┃┃┃┃┣┫┃
 ┻ ┗┛┛┗┛ ┗┻┛┗┛┗┗┛

                                         

                         ___      ___   _______  ________   ____  ____  ________        __      
                        |"  \    /"  | /"     "||"      "\ ("  _||_ " |("      "\      /""\     
                         \   \  //   |(: ______)(.  ___  :)|   (  ) : | \___/   :)    /    \    
                         /\\  \/.    | \/    |  |: \   ) ||(:  |  | . )   /  ___/    /' /\  \   
                        |: \.        | // ___)_ (| (___\ || \\ \__/ //   //  \__    //  __'  \  
                        |.  \    /:  |(:      "||:       :) /\\ __ //\  (:   / "\  /   /  \\  \ 
                        |___|\__/|___| \_______)(________/ (__________)  \_______)(___/    \___)
                                                                        
                       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                       [%] STATUS : Work
                       [%] Developer : KAZAM
                       [%] Platform Supported : Windows
                       [%] REQUESTS PER HOUR : 60
                       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

                                 🪼 >> Meduza is a powerful GitHub lookup tool. << 🪼
"""

print(Fore.YELLOW + ascii_art)

def slowprint(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
    print()

def loading_animation(stop_event):
    chars = "|/-\\"
    i = 0
    while not stop_event.is_set():
        print(Fore.YELLOW + f"\r[~] Grabbing account info... {chars[i % len(chars)]}", end="")
        time.sleep(0.1)
        i += 1
    print("\r", end="")

def load_user_agents_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            user_agents = file.readlines()
            user_agents = [ua.strip() for ua in user_agents if ua.strip()]
        if not user_agents:
            raise ValueError("The file is empty or does not contain valid User Agents.")
        return user_agents
    except Exception as e:
        print(Fore.RED + f"Error loading User Agents: {e}")
        return []

def get_random_user_agent(user_agents):
    if not user_agents:
        return None
    return random.choice(user_agents)

user_agents_file_path = "githubapi/useragents.txt"
user_agents = load_user_agents_from_file(user_agents_file_path)

if not user_agents:
    print(Fore.RED + "No valid User Agent found, the program will stop.")
    sys.exit(1)

def github_get_user_info(username):
    url = f"https://api.github.com/users/{username}"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": get_random_user_agent(user_agents)
    }
    response = requests.get(url, headers=headers)
    print(f"[/] Response Status: {response.status_code}\n")
    if response.status_code == 200:
        data = response.json()
        globalname = data.get("name") or username
        displayname = data.get("login")
        avatar_url = data.get("avatar_url")
        last_update = data.get("updated_at")
        created_at = data.get("created_at")
        user_id = data.get("id")
        email = data.get("email")
        return globalname, displayname, avatar_url, last_update, created_at, user_id, email
    return username, None, None, None, None, None, None

def github_get_email_from_events(username):
    url = f"https://api.github.com/users/{username}/events/public"
    headers = {
        "User-Agent": get_random_user_agent(user_agents)
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            events = response.json()
            for event in events:
                if event.get('type') == 'PushEvent':
                    commits = event.get('payload', {}).get('commits', [])
                    for commit in commits:
                        author = commit.get('author', {})
                        email = author.get('email')
                        if email and 'noreply' not in email:
                            return email
    except requests.RequestException as e:
        print(Fore.RED + f"Error fetching events for {username}: {e}")
    return None

def github_get_email_from_emailaddress_site(username):
    try:
        url = f"https://emailaddress.github.io/?user={username}"
        response = requests.get(url)
        if "Good news!" in response.text:
            emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", response.text)
            for email in emails:
                if "noreply" not in email:
                    return email
    except requests.RequestException as e:
        print(Fore.RED + f"Error fetching email from emailaddress.github.io for {username}: {e}")
    return None

def github_get_email_from_commit_search(username):
    url = f"https://api.github.com/search/commits?q=author:{username}"
    headers = {
        "Accept": "application/vnd.github.cloak-preview",
        "User-Agent": get_random_user_agent(user_agents)
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            items = response.json().get("items", [])
            for item in items:
                commit = item.get("commit", {})
                author = commit.get("author", {})
                email = author.get("email")
                if email and "noreply" not in email:
                    return email
    except requests.RequestException as e:
        print(Fore.RED + f"Error searching commits for {username}: {e}")
    return None

def github_get_email_from_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    headers = {
        "User-Agent": get_random_user_agent(user_agents)
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            repos = response.json()
            for repo in repos:
                commits_url = repo['commits_url'].replace('{/sha}', '')
                commits_headers = {
                    "User-Agent": get_random_user_agent(user_agents)
                }
                commits_response = requests.get(commits_url, headers=commits_headers)
                if commits_response.status_code == 200:
                    commits = commits_response.json()
                    for commit in commits:
                        author = commit.get("commit", {}).get("author", {})
                        email = author.get("email")
                        if email and "noreply" not in email:
                            return email
    except requests.RequestException as e:
        print(Fore.RED + f"Error fetching repos for {username}: {e}")
    return None

def github_get_emails_from_patch_commits(username):
    patch_emails = set()
    url = f"https://api.github.com/users/{username}/repos"
    headers = {
        "User-Agent": get_random_user_agent(user_agents)
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            repos = response.json()
            for repo in repos:
                commits_url = repo['commits_url'].replace('{/sha}', '')
                commits_headers = {
                    "User-Agent": get_random_user_agent(user_agents)
                }
                commits_response = requests.get(commits_url, headers=commits_headers)
                if commits_response.status_code == 200:
                    commits = commits_response.json()
                    for commit in commits:
                       
                        if 'files' in commit:
                            for file in commit['files']:
                                if file['filename'].endswith('.patch'):
                                    
                                    patch_url = file['patch_url']
                                    patch_response = requests.get(patch_url, headers=commits_headers)
                                    if patch_response.status_code == 200:
                                        patch_content = patch_response.text
                                      
                                        matches = re.findall(r'<([^>]+)>', patch_content)
                                       
                                        email_matches = [match for match in matches if '@' in match]
                                        patch_emails.update(email_matches)
    except requests.RequestException as e:
        print(Fore.RED + f"Error fetching patch commits for {username}: {e}")
    return list(patch_emails)

def github_advanced_search(username, repos):
    phone_numbers = set()
    pro_emails = set()

    phone_pattern = re.compile(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b')
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

    for repo in repos:
        readme_url = f"https://raw.githubusercontent.com/{username}/{repo}/master/README.md"
        try:
            response = requests.get(readme_url)
            if response.status_code == 200:
                readme_content = response.text
                phone_numbers.update(phone_pattern.findall(readme_content))
                emails = email_pattern.findall(readme_content)
                filtered_emails = [email for email in emails if 'example' not in email.lower() and 'exemple' not in email.lower()]
                pro_emails.update(filtered_emails)
        except requests.RequestException as e:
            print(Fore.RED + f"Error fetching README for {repo}: {e}")

    return list(phone_numbers), list(pro_emails)

def obfuscate_email(email):
    if email:
        local, domain = email.split('@')
        local_obf = local[0] + '*' * (len(local) - 1)

        domain_parts = domain.split('.')
        if len(domain_parts) > 1:
            domain_name = domain_parts[0]
            domain_extension = '.'.join(domain_parts[1:])
            domain_obf = domain_name[0] + '*' * (len(domain_name) - 1) + '.' + domain_extension
        else:
            domain_obf = domain_parts[0]

        return local_obf + '@' + domain_obf
    return email

def github_email_finder(username):
    globalname, displayname, avatar_url, last_update, created_at, user_id, profile_email = github_get_user_info(username)

    stop_event = threading.Event()
    loading_thread = threading.Thread(target=loading_animation, args=(stop_event,))
    loading_thread.start()

    methods = [
        github_get_email_from_events,
        github_get_email_from_emailaddress_site,
        github_get_email_from_commit_search,
        github_get_email_from_repos
    ]

    found_emails = set()
    for method in methods:
        email = method(username)
        if email:
            found_emails.add(email)

    if profile_email:
        found_emails.add(profile_email)

    repos_url = f"https://api.github.com/users/{username}/repos"
    headers = {
        "User-Agent": get_random_user_agent(user_agents)
    }
    response = requests.get(repos_url, headers=headers)
    repos = [repo['name'] for repo in response.json()] if response.status_code == 200 else []

    phone_numbers, pro_emails = github_advanced_search(username, repos)
    patch_emails = github_get_emails_from_patch_commits(username)

    stop_event.set()
    loading_thread.join()

    result = {
        "profile_info": {
            "name": globalname,
            "username": displayname,
            "avatar_url": avatar_url,
            "last_update": last_update,
            "created_at": created_at,
            "user_id": user_id
        },
        "emails": list(found_emails),
        "advanced_search": {
            "phone_numbers": phone_numbers,
            "pro_emails": pro_emails,
            "patch_emails": patch_emails
        }
    }

    log_directory = "logs"
    os.makedirs(log_directory, exist_ok=True)
    log_file_path = os.path.join(log_directory, f"{username}.json")
    with open(log_file_path, "w") as log_file:
        json.dump(result, log_file, indent=4)

    print("\n" + "-"*50)
    print(Fore.CYAN + f"[+] GitHub Profile Information")
    print(Fore.CYAN + f"-------------------------------")
    print(Fore.GREEN + f"Name{Fore.WHITE}............: {Fore.GREEN}{globalname}")
    print(Fore.GREEN + f"Username{Fore.WHITE}............: {Fore.GREEN}{displayname}")
    print(Fore.GREEN + f"Avatar URL{Fore.WHITE}............: {Fore.GREEN}{avatar_url}")
    print(Fore.GREEN + f"Last Update{Fore.WHITE}............: {Fore.GREEN}{last_update}")
    print(Fore.GREEN + f"Created At{Fore.WHITE}............: {Fore.GREEN}{created_at}")
    print(Fore.GREEN + f"User ID{Fore.WHITE}............: {Fore.GREEN}{user_id}")
    print("\n" + "-"*50)

    print(Fore.CYAN + f"[+] Sensitive Information:")
    print(Fore.CYAN + f"----------------------------")

    if found_emails:
        print(Fore.YELLOW + f"Leaked Mail{Fore.WHITE}............: {Fore.YELLOW}{len(found_emails)}\n")
        for index, email in enumerate(found_emails, 1):
            print(Fore.YELLOW + f"[{index}]{Fore.WHITE}............: {Fore.YELLOW}{email}")
        print(Fore.YELLOW + f"\nObfuscated Mail{Fore.WHITE}............:\n")
        for index, email in enumerate(found_emails, 1):
            obfuscated_email = obfuscate_email(email)
            print(Fore.YELLOW + f"[{index}]{Fore.WHITE}............: {Fore.YELLOW}{obfuscated_email}")
    else:
        print(Fore.RED + "\nLeaked Mail{Fore.WHITE}............: None\n")

    noreply_email = f"{user_id}+{username}@users.noreply.github.com"
    print(Fore.YELLOW + f"\nNoreply Mail{Fore.WHITE}............:{Fore.YELLOW}{noreply_email}\n")
    obfuscated_noreply_email = obfuscate_email(noreply_email)
    print(Fore.YELLOW + f"\nObfuscated Noreply Mail{Fore.WHITE}............:{Fore.YELLOW}{obfuscated_noreply_email}")

    print("\n" + "-"*50)
    print(Fore.CYAN + f"[+] Advanced Search:")
    print(Fore.CYAN + f"----------------------------")

    if phone_numbers:
        print(Fore.YELLOW + f"Phone Numbers{Fore.WHITE}............: {Fore.YELLOW}{len(phone_numbers)}\n")
        for index, phone in enumerate(phone_numbers, 1):
            print(Fore.YELLOW + f"[{index}]{Fore.WHITE}............: {Fore.YELLOW}+{phone}")
    else:
        print(Fore.RED + "Phone Number............: None\n")

    if pro_emails:
        print(Fore.YELLOW + f"\nOther Mails{Fore.WHITE}............: {Fore.YELLOW}{len(pro_emails)}\n")
        for index, pro_email in enumerate(pro_emails, 1):
            print(Fore.YELLOW + f"[{index}]{Fore.WHITE}............: {Fore.YELLOW}{pro_email}")

    if patch_emails:
        print(Fore.YELLOW + f"\nPatch Emails{Fore.WHITE}............: {Fore.YELLOW}{len(patch_emails)}\n")
        for index, patch_email in enumerate(patch_emails, 1):
            print(Fore.YELLOW + f"[{index}]{Fore.WHITE}............: {Fore.YELLOW}{patch_email}")
    else:
        print(Fore.RED + "Other Mails............: None")
        print(Fore.RED + "Patch Emails............: None")

if __name__ == '__main__':
    while True:
        username = input(Fore.BLUE + "\n[+] GitHub Username: ").strip()
        if username.lower() == 'exit':
            break
        github_email_finder(username)
