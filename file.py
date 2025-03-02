# Assignment7, 

import colorama
from colorama import Fore, Style
import os

def load_existing_names(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return {line.strip().lower() for line in file}
    else:
        return set()

def main():
    # Define the file paths
    file_path = "names.txt"
    nofound_path = "nofound.txt"

    existing_names = load_existing_names(file_path)
    with open(nofound_path, "a") as nofound_file:
        while True:
            name = input("Enter a name (or type 'exit' to quit): ").strip()

            if name.lower() == "exit":
                print(Fore.GREEN +" Hope u had fun, Goodbyeاتمنئ ان استمتعتو.")
                break

            if name.lower() in existing_names:
                print(f"{name} is in the list.")
            else:
                print(f"{name} was not found. Writing to {nofound_path}.")
                nofound_file.write(name + "\n")

if __name__ == "__main__":
    main()
