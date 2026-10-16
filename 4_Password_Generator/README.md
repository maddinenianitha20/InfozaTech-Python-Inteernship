# 🔐 Password Generator Using Python

## 📌 Project Description
A Python application that generates random passwords based on user preferences. Users can customize the password length and choose whether to include letters, numbers, and symbols.

## ✨ Features
- Generate passwords with a custom length.
- Include uppercase and lowercase letters.
- Include numbers and special symbols.
- Generate multiple passwords in one session.
- Save generated passwords to a `passwords.txt` file.
- Automatically create the text file when saving the first password.
- Append new passwords on separate lines without overwriting previous entries.

## 🛠️ Technologies Used
- Python
- `secrets` module
- `string` module
- File Handling

## ▶️ How to Run
1. Install Python on your computer.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

   `python password_generator.py`

5. Enter your desired password length.
6. Choose whether to include letters, numbers, and symbols.
7. View the generated password.
8. Choose whether to save it to a text file.

## 📂 Project Structure
```text
4_Password_Generator/
├── password_generator.py
└── passwords.txt  (created when a password is saved)