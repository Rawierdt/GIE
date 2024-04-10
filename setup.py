import os
import platform
import sys

try:
    if platform.system() == "Windows":
        os.system("python -m pip install colorama")
        os.system("python -m pip install hashlib")
        os.system("python -m pip install cryptography")
        os.system("cls")
    else:  # Linux, macOS, etc.
        os.system("python3 -m pip install colorama")
        os.system("python -m pip install hashlib")
        os.system("python -m pip install cryptography")
        os.system("clear")

    print("Installed Successfully !!!")
    python_command = "python3" if sys.platform != "win32" else "python"
    os.system(f"{python_command} gie.py -h")
except Exception as error:
    print(f"\n{error}\nError Encountered...")
