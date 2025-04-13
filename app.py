# User se password ka input lena
password = input("Apna password likho: ")

# Score variable jo password ki strength count karega
score = 0

# 1. Password ki length check karna
if len(password) >= 8:
    print("Password ki length theek hai!")
    score += 1
else:
    print("Aapka password bohot chhota hai! Kam az kam 8 characters ka rakhein.")

# 2. Uppercase letter check karna
if any(char.isupper() for char in password):
    print("Uppercase letter mojood hai!")
    score += 1
else:
    print("Kam az kam ek uppercase letter zaroori hai!")

# 3. Lowercase letter check karna
if any(char.islower() for char in password):
    print("Lowercase letter mojood hai!")
    score += 1
else:
    print("Kam az kam ek lowercase letter zaroori hai!")

# 4. Special character check karna
special_characters = "!@#$%^&*"
if any(char in special_characters for char in password):
    print("Special character mojood hai!")
    score += 1
else:
    print("Kam az kam ek special character (!@#$%^&*) zaroori hai!")

# 5. Number (0-9) check karna
if any(char.isdigit() for char in password):
    print("Number (0-9) mojood hai!")
    score += 1
else:
    print("Kam az kam ek number (0-9) zaroori hai!")

# Final Score aur Strength Check Karna
print("\n Aapka Password Score:", score, "/ 5")

if score == 5:
    print("Password bohot strong hai! 🚀")
elif score >= 3:
    print("Password theek hai, lekin behtar banaya ja sakta hai.")
else:
    print("Password bohot weak hai! Mazeed behtar karein.")