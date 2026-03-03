import time
import string
from colorama import Fore, Style, init

init(autoreset=True)

# ===== Hacker Banner =====
print(Fore.GREEN + """
=========================================
     BRUTE FORCE SIMULATOR PRO v2.0
        Educational Cyber Lab
=========================================
""")

password = input(Fore.CYAN + "Enter password to simulate: ")

# ===== Detect Character Set =====
charset = 0

if any(c.isdigit() for c in password):
    charset += 10
if any(c.islower() for c in password):
    charset += 26
if any(c.isupper() for c in password):
    charset += 26
if any(c in string.punctuation for c in password):
    charset += 32

length = len(password)

total_combinations = charset ** length

# ===== Time Estimation =====
guesses_per_sec = 100000

seconds = total_combinations / guesses_per_sec
days = seconds / 86400
years = days / 365

print(Fore.YELLOW + "\n[+] Password Analysis")
print("-----------------------------------")
print("Length:", length)
print("Charset Size:", charset)
print("Total Combinations:", total_combinations)

print(Fore.MAGENTA + "\nEstimated Crack Time:")
print(f"{seconds:.2f} seconds")
print(f"{days:.2f} days")
print(f"{years:.2f} years")

# ===== Strength Rating =====
if years < 0.01:
    strength = Fore.RED + "WEAK"
elif years < 5:
    strength = Fore.YELLOW + "MEDIUM"
else:
    strength = Fore.GREEN + "STRONG"

print("\nPassword Strength:", strength)

input(Fore.CYAN + "\nPress ENTER to start simulation...")

# ===== Simulation =====
print(Fore.GREEN + "\n[+] Launching brute force engine...\n")

start = time.time()
attempts = 0
bar_length = 30

simulation_steps = 500  # animation size

for i in range(simulation_steps):
    attempts += 1
    
    progress = (i + 1) / simulation_steps
    filled = int(bar_length * progress)
    bar = "█" * filled + "-" * (bar_length - filled)

    elapsed = time.time() - start
    speed = attempts / elapsed if elapsed > 0 else 0

    print(
        Fore.GREEN +
        f"[{bar}] {progress*100:5.1f}% | "
        f"Attempts: {attempts} | "
        f"Speed: {int(speed)} guesses/sec",
        end="\r"
    )

    time.sleep(0.01)

end = time.time()

print("\n\n" + Fore.GREEN + "[✓] Simulation Complete!")
print(Fore.WHITE + f"Time elapsed: {round(end-start,2)} seconds")

print(Fore.RED + "\n⚠️ Lesson:")
print("Short passwords fall quickly to brute force attacks.")
print("Use long passwords with mixed characters.")
