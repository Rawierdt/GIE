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
Encrypt and decrypt your files and folders with AES, for any file, jpg, png, mp4, mp3, docx, pdf, etc... 

**IMPORTANT TO READ ALL**

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
---

## For Encrypt
Run `-h` for print the help/usage

```
python gie.py -h
```

To **Encrypt** a folder or file 
* ! The path must be enclosed in quotes " " 

For folders
```
python gie.py "C:\YOUR\FOLDER"
```

For only files
```
python gie.py "C:\YOUR\FILES.extension"
```

extension = jpg, png, mp3, mp4, docx, etc, etc...

* ! A message will appear that says: "Enter a password:"

! NOTE: **The password cannot contain the characters $ and "**

Example Output:
`python gie.py "D:\Sam\Plugins\IP.exe"`
`Enter a password:      `

Note: The password will not be visible while you type it

Once the password is entered, it will start encrypting the files with the extension **".gie"** and will generate a **".GKY"** file, which is very important to decrypt your original file.

*"GKY" is the extension of the file containing the key for decryption, along with the password provided.*

! *If you want to share the file with your colleague, you will need to provide him/her with three files, the .gie, the .GKY and the password.*


## For Decrypt

To **Decrypt** a folder or file 
* ! The path and password must be enclosed in quotes " " 

Run `-d` for decrypt
Run `-p` for set the password used previously

For folders
```
python gie.py -p "PASSWORD" -d "C:\YOUR\FOLDER"
```

For only files
```
python gie.py -p "PASSWORD" -d "C:\YOUR\FILES.extension.gie"
```
---

Example Output:
`python gie.py -p "L1ñy*8Cv" -d "D:\Sam\Plugins\IP.exe"`

The program will search if the .GKY file exists in the path provided and will try to decrypt the file with the password, if the password does not match the file will not decrypt or will decrypt corruptly, if the GKY does not exist, the program will throw an error message and will not be able to decrypt.

It is very important to save the .GKY and the PASSWORD very well.

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
