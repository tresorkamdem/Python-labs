import string
import random


# ===============================
# PART A – Individual Functions
# ===============================

def check_min_length(password, min_len=8):
    return len(password) >= min_len


def has_uppercase(password):
    return any(char in string.ascii_uppercase for char in password)


def has_lowercase(password):
    return any(char in string.ascii_lowercase for char in password)


def has_digit(password):
    return any(char in string.digits for char in password)


def has_special_char(password):
    return any(char in string.punctuation for char in password)


# ===============================
# PART B – Master Validation
# ===============================

def validate_password(password):
    results = {
        "min_length": check_min_length(password),
        "has_uppercase": has_uppercase(password),
        "has_lowercase": has_lowercase(password),
        "has_digit": has_digit(password),
        "has_special_char": has_special_char(password)
    }

    results["is_valid"] = all(results.values())

    return results


# ===============================
# PART C – User Interface
# ===============================

def main():
    print("=" * 50)
    print("PASSWORD STRENGTH VALIDATOR")
    print("=" * 50)

    print("\nRequirements:")
    print("- Minimum 8 characters")
    print("- At least one uppercase letter")
    print("- At least one lowercase letter")
    print("- At least one digit")
    print("- At least one special character")

    password = input("\nEnter password to validate: ")

    results = validate_password(password)

    print("\nVALIDATION RESULTS")
    print("=" * 50)

    print("Minimum length:", results["min_length"])
    print("Has uppercase:", results["has_uppercase"])
    print("Has lowercase:", results["has_lowercase"])
    print("Has digit:", results["has_digit"])
    print("Has special char:", results["has_special_char"])

    print("=" * 50)

    if results["is_valid"]:
        print("PASSWORD IS STRONG ✅")
    else:
        print("PASSWORD IS WEAK ❌")

        # Extra: random hint
        hint = random.choice([
            "Try adding a special character!",
            "Include at least one uppercase letter.",
            "Make it longer!",
            "Add at least one number."
        ])
        print("Hint:", hint)

    print("=" * 50)


if __name__ == "__main__":
    main()