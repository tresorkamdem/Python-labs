# Week 4 - Exercise 3
# Password Policy Validator

passwords = [
    "Pass123",
    "SecurePassword1",
    "weak",
    "MyP@ssw0rd",
    "NOLOWER123"
]

print("Validating passwords...")

compliant = 0
non_compliant = 0

for password in passwords:

    issues = []

    # Check length
    if len(password) < 8:
        issues.append("Too short")

    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if "A" <= char <= "Z":
            has_upper = True
        if "a" <= char <= "z":
            has_lower = True
        if "0" <= char <= "9":
            has_digit = True

    if not has_upper:
        issues.append("No uppercase letters")
    if not has_lower:
        issues.append("No lowercase letters")
    if not has_digit:
        issues.append("No digits")

    if len(issues) == 0:
        print("PASS:", password, "- Meets all requirements")
        compliant += 1
    else:
        print("FAIL:", password, "-", ", ".join(issues))
        non_compliant += 1

print("Summary:", compliant, "compliant,", non_compliant, "non-compliant")