import re


def passwordStrength(password):
    # Strength Checks
    charRegex = re.compile(r"(\w{8,})")  # Check if password has atleast 8 characters
    lowerRegex = re.compile(r"[a-z]+")  # Check if at least one lowercase letter
    upperRegex = re.compile(r"[A-Z]+")  # Check if atleast one upper case letter
    digitRegex = re.compile(r"[0-9]+")  # Check if at least one digit.

    if (
        not charRegex.findall(password)
        or not lowerRegex.findall(password)
        or not upperRegex.findall(password)
        or not digitRegex.findall(password)
    ):
        return False
    else:
        return True
