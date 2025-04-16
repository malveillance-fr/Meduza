

                                        __  _____________  __  _______   ___ 
                                       /  |/  / ____/ __ \/ / / /__  /  /   |
                                      / /|_/ / __/ / / / / / / /  / /  / /| |
                                     / /  / / /___/ /_/ / /_/ /  / /__/ ___ |
                                    /_/  /_/_____/_____/\____/  /____/_/  |_|
                                         


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Meduza is a powerful tool that can find almost any public email associated with a GitHub user by searching through commits, profiles, and other public sources.

Features

- Search for emails via GitHub public events
- Search for emails in GitHub commits
- Search for emails through GitHub user profiles
- Multiple email retrieval methods supported
- Simple command-line interface

Installation

1. Clone this repository to your local machine.

   git clone https://github.com/yourusername/meduza.git

2. Install the required dependencies with pip.

   pip install -r requirements.txt

3. The script is now ready to be used.

Usage

1. Run the main script `meduza.py` from your terminal or command line.

   python meduza.py

2. When prompted, enter the GitHub username whose email you wish to search.

3. The program will show the user’s public email if available.

   [+] GitHub Username: octocat  
   octocat --> octocat@example.com

4. Type `exit` to quit the script.

Search Methods

The script uses several methods to attempt to find an email associated with a GitHub user:

- GitHub Public Events: Searches through the commits made by the user.
- GitHub Profile: Directly searches the user’s public profile.
- EmailAddress GitHub Site: Searches for emails via a third-party site based on GitHub.
- Commit Search: Searches in the public commits associated with the user.

Configuration Files

The `config` folder contains essential configuration files to customize the script’s behavior. You can modify these files to adjust the program's settings to your needs.

Credits

- Main Developer: Malveillance (https://github.com/malveillance-fr)
- Third-party Libraries Used:
  - requests: For making HTTP requests to the GitHub API.
  - colorama: For displaying messages with colors in the terminal.
  - re: For regular expressions used to extract emails.

License

This project is licensed under the MIT License. You are free to use, modify, and distribute it as long as you comply with the terms of the license.
