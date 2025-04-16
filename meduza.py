import requests
from colorama import Fore, init
import re
import sys
import time
import threading
import os
import random
import json

init(autoreset=True)
os.system("title Meduza Terminal")

ascii_art = r"""
                                            

                                     


                                                  __  _____________  __  _______   ___ 
                                                 /  |/  / ____/ __ \/ / / /__  /  /   |
                                                / /|_/ / __/ / / / / / / /  / /  / /| |
                                               / /  / / /___/ /_/ / /_/ /  / /__/ ___ |
                                              /_/  /_/_____/_____/\____/  /____/_/  |_|
                                                  

                       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
                       [%] STATUS : Work
                       [%] Developer : Malveillance
                       [%] Platform Supported : Windows
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
    print(f"Response Status: {response.status_code}") 
    if response.status_code == 200:
        data = response.json()
        globalname = data.get("name") or username
        bio = data.get("bio")
        displayname = data.get("login")
        avatar_url = data.get("avatar_url")
        last_update = data.get("updated_at")
        created_at = data.get("created_at")
        user_id = data.get("id")
        email = data.get("email")
        return globalname, bio, displayname, avatar_url, last_update, created_at, user_id, email
    return username, None, None, None, None, None, None, None

def github_get_email_from_events(username):
    url = f"https://api.github.com/users/{username}/events/public"
    headers = {
        "User-Agent": get_random_user_agent(user_agents)
    }
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
    except:
        pass
    return None

def github_get_email_from_commit_search(username):
    url = f"https://api.github.com/search/commits?q=author:{username}"
    headers = {
        "Accept": "application/vnd.github.cloak-preview",
        "User-Agent": get_random_user_agent(user_agents)
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        items = response.json().get("items", [])
        for item in items:
            commit = item.get("commit", {})
            author = commit.get("author", {})
            email = author.get("email")
            if email and "noreply" not in email:
                return email
    return None

def github_get_email_from_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    headers = {
        "User-Agent": get_random_user_agent(user_agents)
    }
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
    return None

def github_email_finder(username):
    globalname, bio, displayname, avatar_url, last_update, created_at, user_id, profile_email = github_get_user_info(username)

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

    stop_event.set()
    loading_thread.join()

    result = {
        "profile_info": {
            "name": globalname,
            "bio": bio if bio else 'No bio available',
            "username": displayname,
            "avatar_url": avatar_url,
            "last_update": last_update,
            "created_at": created_at,
            "user_id": user_id
        },
        "emails": list(found_emails)
    }


    log_directory = "logs"
    os.makedirs(log_directory, exist_ok=True)
    log_file_path = os.path.join(log_directory, f"{username}.json")
    with open(log_file_path, "w") as log_file:
        json.dump(result, log_file, indent=4)

    print("\n" + "-"*50)
    print(Fore.CYAN + f"[+] GitHub Profile Information")
    print(Fore.CYAN + f"-------------------------------")
    print(Fore.GREEN + f"Name         : {globalname}")
    print(Fore.GREEN + f"Bio          : {bio if bio else 'No bio available'}")
    print(Fore.GREEN + f"Username     : {displayname}")
    print(Fore.GREEN + f"Avatar URL   : {avatar_url}")
    print(Fore.GREEN + f"Last Update  : {last_update}")
    print(Fore.GREEN + f"Created At   : {created_at}")
    print(Fore.GREEN + f"User ID      : {user_id}")
    print("\n" + "-"*50)  

    print(Fore.CYAN + f"[+] Sensitive Information:")
    print(Fore.CYAN + f"----------------------------")
    
    if found_emails:
        print(Fore.YELLOW + f"[+] Mails Found: {len(found_emails)}")
        for index, email in enumerate(found_emails, 1):
            print(Fore.YELLOW + f"\n[{index}] Leaked Mail : {email}")
    else:
        print(Fore.RED + "Leaked Mail : None")
    
    noreply_email = f"{user_id}+{username}@users.noreply.github.com"
    print(Fore.YELLOW + f"\nNoreply Mail    : {noreply_email}")

if __name__ == '__main__':
    while True:
        username = input(Fore.BLUE + "\n[+] GitHub Username: ").strip()
        if username.lower() == 'exit':
            break
        github_email_finder(username)
