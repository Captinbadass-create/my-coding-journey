import random
import string

print("=== CAPTAIN'S VAULT PRO MAX ===")

length = int(input("Length? (8-20): "))

use_upper = input("Include CAPS? (y/n): ").lower() == 'y'
use_numbers = input("Include Numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include Symbols like @#$? (y/n): ").lower() == 'y'

chars = string.ascii_lowercase
if use_upper:
    chars += string.ascii_uppercase
if use_numbers:
    chars += string.digits
if use_symbols:
    chars += string.punctuation

if not chars:
    print("Oga you must choose at least one na!")
else:
    password = "".join(random.choice(chars) for _ in range(length))
    print(f"\n🔐 PASSWORD: {password}")
    
    # strength check
    if length >= 12 and use_upper and use_numbers and use_symbols:
        print("Strength: LEGENDARY 🔥🔥🔥 (Shey you be hacker now?)")
    elif length >= 8:
        print("Strength: Strong 💪")
    else:
        print("Strength: Weak o, increase length")
