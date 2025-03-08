# 🔐 Password Generator Project

A Python-based password generator that creates and stores strong random passwords with customizable complexity.

## 🛠️ Features

- Generate passwords with customizable complexity
- Mix of uppercase and lowercase letters
- Include special symbols and numbers
- Shuffled characters for enhanced security
- Save passwords with labels and timestamps
- Store all passwords in a local file

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/tamerakdeniz/Password-Generator-Project.git
```

2. Navigate to the project directory:
```bash 
cd Password-Generator-Project
```

3. Run the script:
```bash
python main.py
```

## 📝 How to Use

1. Run the script and you'll be prompted to:
   - Enter what the password is for (e.g., Gmail, Netflix)
   - Choose number of letters (a-z, A-Z)
   - Choose number of symbols (!#$%&()*+)
   - Choose number of numbers (0-9)

2. The program will:
   - Generate a secure random password
   - Display it on screen
   - Save it to password.txt with timestamp

Example output:
```
Welcome to the PyPassword Generator!
What is this password for? (e.g., Gmail, Netflix, etc.): Gmail
How many letters would you like in your password? 4
How many symbols would you like? 2 
How many numbers would you like? 2

Your password for Gmail is: Kj#9nP&2
Password has been saved to password.txt
```

Password storage format in password.txt:
```
[2025-03-08 14:30:45] Gmail: Kj#9nP&2
```

## 📋 Requirements
- Python 3.x
- No additional packages needed - uses only built-in Python libraries

The program creates and maintains a single password.txt file in the project directory to store all generated passwords.
