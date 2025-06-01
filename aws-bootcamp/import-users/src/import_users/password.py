import secrets
import string


def generate_password(length: int) -> str:
    """Generate a password for IAM user login profile creation.

    The password will have at least 1 lowercase, 1 uppercase
    and 1 digit.
    """
    # Punctuation characters are limited to make output csv parsing easier.
    # No quotes, commas, backslashes, or brackets.
    goodset = string.ascii_lowercase + string.ascii_uppercase + "!@#$%^&-_+." + string.digits
    while True:
        password = "".join(secrets.choice(goodset) for _ in range(length))
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        if has_lower and has_upper and has_digit:
            break
    return password
