![image](https://github.com/user-attachments/assets/ec3e9446-7c60-4b50-8fe7-3c67c43b8540)



# 🪼 Meduza - GitHub Email & Profile Lookup Tool

**Meduza** is a powerful command-line tool designed to fetch public (and sometimes sensitive) GitHub user information, including email addresses when available. It uses multiple techniques to increase the chances of locating a valid, non-noreply email address associated with a GitHub username.

---

## ⚙️ Features

- 🔍 Fetch GitHub account details:
  - Name
  - Bio
  - Username
  - Avatar URL
  - Account creation date
  - Last update
  - User ID

- 📧 Attempts to extract email using multiple methods:

  - Public events
  - GitHub commit history
  - External email resolver (`emailaddress.github.io`)
  - Repositories and associated commits

88% chance of extracting a mail
---

## 🖥️ Supported Platforms

- Windows (fully supported)

---

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/malveillance-fr/Meduza.git
   cd Meduza-Main-3.0
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python meduza.py
   ```

---

## 🧠 Usage

Once launched, you’ll be prompted to enter a GitHub username. Meduza will then attempt to retrieve as much information as possible, including potential email addresses.

To exit the program, simply type:
```
exit
```

---

## 📜 Example Output

```
--------------------------------------------------
[+] GitHub Profile Information
-------------------------------
Name............: Google
Username............: google
Avatar URL............: https://avatars.githubusercontent.com/u/1342004?v=4
Last Update............: 2024-08-09T17:36:18Z
Created At............: 2012-01-18T01:30:18Z
User ID............: 1342004

--------------------------------------------------
[+] Sensitive Information:
----------------------------
Leaked Mail............: 3

[1]............: mail@exemple.com
[2]............: mail@exemple.com
[3]............: mail@exemple.com

Noreply Mail............:1342004+google@users.noreply.github.com

--------------------------------------------------
[+] Advanced Search:
----------------------------
Phone Number............: None
Other Mails............: 5

[1]............: mail@exemple.com
[2]............: mail@exemple.com
[3]............: mail@exemple.com
[4]............: mail@exemple.com
[5]............: mail@exemple.com

```

---

## 🛑 Disclaimer

This tool is intended for **educational and ethical use only**. Accessing or attempting to retrieve private information without consent is strictly prohibited and may be illegal. The developer is not responsible for any misuse.

---

## 👨‍💻 Developer

- Name: **KAZAM**
- Tool: **Meduza**
- Status: `Working ✅`

---

Only 60 request per hour.

---
## 📌 License

This project is open-source and available under the [MIT License](LICENSE).
