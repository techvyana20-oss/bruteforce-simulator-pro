import time
import string
import itertools
from colorama import Fore, init

init(autoreset=True)

print(Fore.GREEN + """
=========================================
     BRUTE FORCE SIMULATOR PRO v2.2
        Educational Cyber Lab
=========================================
""")

# Password input
target_password = input(Fore.CYAN + "Set a password (demo purpose): ")

charset = string.ascii_lowercase + string.digits
length = len(target_password)

print(Fore.YELLOW + f"\n[+] Password length: {length}")
print("[+] Charset used: lowercase letters + numbers")
print("[+] Logging attempts to: attempt_log.txt")
print("[+] Starting REAL brute force demo...\n")

# Create log file
log_file = open("attempt_log.txt", "w")
log_file.write("=== BRUTE FORCE ATTEMPT LOG ===\n\n")

start = time.time()
attempts = 0

for guess_tuple in itertools.product(charset, repeat=length):

    guess = ''.join(guess_tuple)
    attempts += 1

    # Save attempt to file
    log_file.write(f"Attempt {attempts}: {guess}\n")

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

# Final log info
log_file.write("\n=== PASSWORD FOUND ===\n")
log_file.write(f"Password: {guess}\n")
log_file.write(f"Total Attempts: {attempts}\n")
log_file.write(f"Time Taken: {round(end-start,2)} seconds\n")

log_file.close()

print("\n\n" + Fore.GREEN + "[✓] Password Found!")
print(f"Password: {guess}")
print(f"Attempts: {attempts}")
print(f"Time Taken: {round(end-start,2)} seconds")

print(Fore.CYAN + "\nLog saved as: attempt_log.txt")

print(Fore.RED + "\n⚠️ Educational Note:")
print("Short passwords are vulnerable to brute force attacks.")
