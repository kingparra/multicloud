import re
from enum import Enum

import email_validator

from import_users.iam_utils import check_group_exists, check_user_exists


def email_to_user_name(email: str) -> str:
    """Convert an email in firstname.lastname@companyname.com
    to a valid AWS IAM username and verify it doesn't exist.

    :raises ValueError: If email is invalid, contains non-ASCII chars,
                      or username already exists in IAM
    """
    valid_email = email_validator.validate_email(email)
    local_part = valid_email.ascii_local_part

    if local_part is None:
        raise ValueError("email user name is not ascii")

    if check_user_exists(local_part):
        raise ValueError(f"IAM user '{local_part}' already exists")

    return local_part


def team_to_group_name(team: str) -> str:
    """Convert a team name (which may be any arbitrary string)
    into PascalCase with non-alphabetic characters stripped.
    Words that are all uppercase remain uppercase.

    :raises ValueError: If result would be empty or group already exists
    """
    cleaned_team = re.sub(r"[^A-Za-z ]", "", team)
    cleaned_words = [word if word.isupper() else word.capitalize() for word in cleaned_team.split()]
    result = "".join(cleaned_words)

    if len(result) == 0:
        raise ValueError("team was either all special characters or all spaces")

    if check_group_exists(result):
        raise ValueError(f"IAM group '{result}' already exists")

    return result
