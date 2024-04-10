![imageTitle](/title.jpg)

[![Static Badge](https://img.shields.io/badge/%20build-MIT-brightgreen?logo=github&label=LICENSE)](https://github.com/Rawierdt/GIE/LICENSE)
![Static Badge](https://img.shields.io/badge/APRIL%202024-red?label=RELEASE%20DATE)
![Static Badge](https://img.shields.io/badge/LANGUAGE-Python-yellow?logo=python)
# GIE

## Encryptor and Decryptor
An Encryptor and Decryptor for files and folders for Windows, written in Python.


> [!CAUTION]
> Disclaimer: This tool was created for educational purposes only. I do not take any responsibility for the misuse of this tool.


![aCreator](https://i.ibb.co/q92xdX2/gie-terminal.gif)


## Version
**GIE V3.0**

### Features
Create and Crack through brute force using a dictionary or wordlist.

## 📦 Requirements
**[Python3](https://www.python.org/downloads/)**

**[Colorama](https://pypi.org/project/colorama/)**

**Subprocess**

**Hashlib**

**Cryptography**

## 💻 Installation
Execute the commands according to your case (Win or Linux)

`pyhon` for windows

Clone or Download this Repository
```
git clone git@github.com:Rawierdt/GIE.git
```

Change Directory
```
cd GIE
```
Run the setup.py file
```
python setup.py
```
OR install the dependencies manually

Run the project
```
python gie.py -h
```

## For Encrypt
Run `-h` for print the help/usage

```
python gie.py -h
```

To **Encrypt** a folder or file 
* ! The path must be enclosed in quotes " " 

For folders
```
python gie.py "C:\ProgramData\Riot Games"
```

For only files
```
python gie.py "C:\ProgramData\Riot Games\lol.exe"
```

* ! A message will appear that says: "Enter a password:"

! NOTE: **The password cannot contain the characters $ and "**

*Once the password is written, the files with the* **".gie"** *extension will begin to be encrypted and a **".GKY"** *file will be generated, which is very important to decrypt your original file*

## For Decrypt

---
### TODO List

- [ ] Password check
- [x] AES
- [ ] UI Menu

### 🤝 Contributing
Contributions, issues and feature requests are welcome! Feel free to check issues page.

### ❤️ Show your support
Give a ⭐️ if this project helped you! 

### 📝 License

Copyright © 2024 [Rawier](https://rawier.vercel.app). This project is [MIT](/LICENSE) licensed.

---
