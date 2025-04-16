![image](https://github.com/user-attachments/assets/7fd38170-ea2d-4854-a36a-bf93ddda52c8)


```
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

---

## 🖥️ Supported Platforms

- Windows (fully supported)

---

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/malveillance-fr/Meduza.git
   cd Meduza
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
[+] GitHub Profile Information
-------------------------------
Name         : John Doe
Bio          : Open source enthusiast 🚀
Username     : johndoe
Avatar URL   : https://avatars.githubusercontent.com/u/12345678
Last Update  : 2024-06-01T10:00:00Z
Created At   : 2018-03-12T14:32:00Z
User ID      : 12345678

[+] Sensitive Information:
----------------------------
Email        : johndoe@example.com
```

---

## 🛑 Disclaimer

This tool is intended for **educational and ethical use only**. Accessing or attempting to retrieve private information without consent is strictly prohibited and may be illegal. The developer is not responsible for any misuse.

---

## 👨‍💻 Developer

- Name: **Malveillance**
- Tool: **Meduza**
- Status: `Working ✅`

---

## 📌 License

This project is open-source and available under the [MIT License](LICENSE).
