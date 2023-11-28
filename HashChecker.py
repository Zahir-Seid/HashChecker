import hashlib
from colorama import init, Fore

init(autoreset=True)

def hash_file(hf_path):
    #Read and return the content of the hash file.
    with open(hf_path, 'r') as file:
        file_content = file.read().strip()
    return file_content

def calculate_hash(file_path, hash_type):
    #Calculate and return the hash of the file.
    print("Checking the hash...")
    hasher = hashlib.new(hash_type)
    with open(file_path, 'rb') as file:
        for data in iter(lambda: file.read(8192), b''):
            hasher.update(data)
    return hasher.hexdigest()

if __name__ == "__main__":
    print("File Hash Checker")
    file_path = input("\nEnter the path of the file to be checked: ")
    print("\nChoose from the options below. \n1) Input hash value from a file \n2) Input hash value from keyboard")
    option = int(input("#: "))
    hash_type = input("Enter the hash type of the file to be checked: ")

    if option == 1:
        hf_path = input("Enter the path of the hash file: ")
        actual_hash = calculate_hash(file_path, hash_type)
        expected_hash = hash_file(hf_path)
        if actual_hash == expected_hash:
            print(Fore.GREEN + "It matches")
        else:
            print(Fore.RED + "The hashes don't match")
    elif option == 2:
        hash_value = input("Enter the hash value: ")
        actual_hash = calculate_hash(file_path, hash_type)
        if actual_hash == hash_value:
            print(Fore.GREEN + "It matches")
        else:
            print(Fore.RED + "The hashes don't match")
    else:
        print("Invalid input")
