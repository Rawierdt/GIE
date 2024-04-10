import os
from argparse import ArgumentParser
from getpass import getpass
from crypt_utl import encrypt_file, decrypt_file, encrypt_directory, decrypt_directory
from colorama import Fore, Style


def main():
    parser = ArgumentParser(prog=Fore.LIGHTMAGENTA_EX + 'GIE' + Style.RESET_ALL,
                            description=Fore.LIGHTBLUE_EX + "Encripta y Desencripta by Rawier" + Style.RESET_ALL,
                            epilog=r'Examp: gie.py "C:\Sys32" to encrypt or gie.py -p "PASS" -d "C:\Sys32" to decrypt')
    parser.add_argument("path", help="Ruta del archivo o carpeta a encriptar/desencriptar")
    parser.add_argument("-p", "--password", help="Contraseña para generar la clave")
    parser.add_argument("-d", "--decrypt", action="store_true", help="Desencriptar la carpeta o archivo")
    args = parser.parse_args()

    input_path = args.path

    if not os.path.exists(input_path):
        print("No se ha proporcionado una ruta válida.")
        return

    if args.password is not None:
        password = args.password.encode()  # Convertir la contraseña a bytes
    else:
        password = getpass("Ingrese la contraseña: ")
        print(Fore.LIGHTGREEN_EX + f"Your Password Is: {password}" + Style.RESET_ALL)
    if args.decrypt:
        if os.path.isdir(input_path):
            decrypt_directory(input_path, password)
        elif os.path.isfile(input_path):
            decrypt_file(input_path, password)  # No need to remove the .gie extension
        print(f"Archivo o carpeta desencriptado en: {input_path}")
    else:
        if os.path.isdir(input_path):
            encrypt_directory(input_path, password)
            print(f"Directorio encriptado en: {input_path}")
        elif os.path.isfile(input_path):
            encrypt_file(input_path, password)
            print(f"Archivo encriptado en: {input_path}")
        else:
            print(Fore.LIGHTRED_EX + f"No se pudo encontrar el archivo o carpeta: {input_path}" + Style.RESET_ALL)


if __name__ == "__main__":
    main()
