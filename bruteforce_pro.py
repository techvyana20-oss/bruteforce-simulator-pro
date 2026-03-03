import time
import string
import itertools
from colorama import Fore, init

init(autoreset=True)

print(Fore.GREEN + """
=========================================
     BRUTE FORCE SIMULATOR PRO v2.1
        Educational Cyber Lab
=========================================
""")

# User sets password
target_password = input(Fore.CYAN + "Set a password (demo purpose): ")

charset = string.ascii_lowercase + string.digits
length = len(target_password)

print(Fore.YELLOW + f"\n[+] Password length: {length}")
print("[+] Charset used: lowercase letters + numbers")
print("[+] Starting REAL brute force demo...\n")

start = time.time()
attempts = 0

# Generate combinations
for guess_tuple in itertools.product(charset, repeat=length):

    guess = ''.join(guess_tuple)
    attempts += 1

    elapsed = time.time() - start
    speed = attempts / elapsed if elapsed > 0 else 0

    print(
        Fore.GREEN +
        f"Trying: {guess} | Attempts: {attempts} | Speed: {int(speed)} guesses/sec",
        end="\r"
    )

    if guess == target_password:
        break

end = time.time()

print("\n\n" + Fore.GREEN + "[✓] Password Found!")
print(f"Password: {guess}")
print(f"Attempts: {attempts}")
print(f"Time Taken: {round(end-start,2)} seconds")

print(Fore.RED + "\n⚠️ Educational Note:")
print("Short passwords are vulnerable to brute force attacks.")
