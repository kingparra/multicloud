import re

import email_validator


def email_to_user_name(email: str) -> str:
    """Convert an email in firstname.lastname@companyname.com
    to a valid AWS IAM username.
    """
    valid_email = email_validator.validate_email(email)
    local_part = valid_email.ascii_local_part
    if local_part is None:
        raise ValueError("email user name is not ascii")
    else:
        return local_part


def team_to_group_name(team: str) -> str:
    """Convert a team name (which may be any arbitrary string)
    into PascalCase with non-alphabetic characters stripped.
    Words that are all uppercase remain uppercase.
    """
    cleaned_team = re.sub(r"[^A-Za-z ]", "", team)
    cleaned_words = [word if word.isupper() else word.capitalize() for word in cleaned_team.split()]
    result = "".join(cleaned_words)

    if len(result) == 0:
        raise ValueError("team was either all special characters or all spaces")
    else:
        return result
