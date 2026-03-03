import time
import string
import itertools
from datetime import datetime
from colorama import Fore, init

init(autoreset=True)

print(Fore.GREEN + """
=========================================
     BRUTE FORCE SIMULATOR PRO v3.0
        Educational Cyber Lab
=========================================
""")

# ===============================
# Password Input
# ===============================
target_password = input(Fore.CYAN + "Set a password (demo purpose): ")
length = len(target_password)

# ===============================
# AUTO CHARSET DETECTION
# ===============================
charset = ""

if any(c.islower() for c in target_password):
    charset += string.ascii_lowercase

if any(c.isupper() for c in target_password):
    charset += string.ascii_uppercase

if any(c.isdigit() for c in target_password):
    charset += string.digits

if charset == "":
    charset = string.ascii_lowercase

charset_size = len(charset)

print(Fore.YELLOW + f"\n[+] Password length: {length}")
print(f"[+] Charset size detected: {charset_size}")

# ===============================
# TOTAL COMBINATIONS
# ===============================
total_combinations = charset_size ** length
print(f"[+] Total combinations: {total_combinations}")

# ===============================
# CREATE TIMESTAMP LOG FILE
# ===============================
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_filename = f"attempt_log_{timestamp}.txt"

log_file = open(log_filename, "w")
log_file.write("=== BRUTE FORCE ATTEMPT LOG ===\n\n")

print(f"[+] Logging attempts to: {log_filename}")
print("[+] Starting REAL brute force demo...\n")

# ===============================
# BRUTE FORCE LOOP
# ===============================
start = time.time()
attempts = 0
last_update = 0

for guess_tuple in itertools.product(charset, repeat=length):

    guess = ''.join(guess_tuple)
    attempts += 1

    # Write log (buffered every 100 attempts)
    log_file.write(f"Attempt {attempts}: {guess}\n")

    elapsed = time.time() - start
    speed = attempts / elapsed if elapsed > 0 else 0

    progress = (attempts / total_combinations) * 100

    # ETA calculation
    remaining = (total_combinations - attempts) / speed if speed > 0 else 0

    # Update terminal less frequently (faster)
    if attempts - last_update >= 50:
        print(
            Fore.GREEN +
            f"Trying: {guess} | "
            f"{progress:.5f}% | "
            f"Speed: {int(speed)} guesses/sec | "
            f"ETA: {int(remaining)} sec",
            end="\r"
        )
        last_update = attempts

    if guess == target_password:
        break

end = time.time()

# ===============================
# FINAL LOG
# ===============================
log_file.write("\n=== PASSWORD FOUND ===\n")
log_file.write(f"Password: {guess}\n")
log_file.write(f"Attempts: {attempts}\n")
log_file.write(f"Time Taken: {round(end-start,2)} seconds\n")

log_file.close()

# ===============================
# RESULT OUTPUT
# ===============================
print("\n\n" + Fore.GREEN + "[✓] Password Found!")
print(f"Password: {guess}")
print(f"Attempts: {attempts}")
print(f"Time Taken: {round(end-start,2)} seconds")

print(Fore.CYAN + f"\nLog saved as: {log_filename}")

print(Fore.RED + "\n⚠️ Educational Note:")
print("Password complexity increases brute force difficulty exponentially.")
