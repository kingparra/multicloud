import secrets
import string


def generate_password(
    length: int = 30, min_lower: int = 2, min_upper: int = 2, min_digit: int = 2, min_punct: int = 2
) -> str:
    """Generate a password for IAM user login profile creation."""
    if length < min_lower + min_upper + min_digit + min_punct:
        raise ValueError("length must be greater than or equal to lower + upper + digit + punct")
    if any(x < 0 for x in [length, min_lower, min_upper, min_digit, min_punct]):
        raise ValueError("All parameters must be greater than or equal to 0.")

    # Limit punctuation so output CSV is easier to parse (no commas or quotes).
    custom_punct = "!@#$%^&-_+.[]()"
    goodset = string.ascii_lowercase + string.ascii_uppercase + string.digits + custom_punct

    while True:
        password = "".join(secrets.choice(goodset) for _ in range(length))
        checks = {
            "has_min_lower": sum(c.islower() for c in password) >= min_lower,
            "has_min_upper": sum(c.isupper() for c in password) >= min_upper,
            "has_min_digit": sum(c.isdigit() for c in password) >= min_digit,
            "has_min_punct": sum(c in custom_punct for c in password) >= min_punct,
        }
        if all(v for v in checks.values()):
            break

    return password
