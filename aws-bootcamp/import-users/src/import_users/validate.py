# Keep this

import re
from dataclasses import dataclass

import email_validator

from import_users.iam_utils import check_group_exists, check_user_exists


@dataclass
class ValidationResult:
    errors: list[Exception]
    value: str | None = None


def email_to_user_name(email: str) -> ValidationResult:
    """Convert an email in firstname.lastname@companyname.com
    to a valid AWS IAM username and verify it doesn't already exist.
    """
    errors: list[Exception] = []
    local_part = None
    try:
        valid_email = email_validator.validate_email(email, check_deliverability=False)
        local_part = valid_email.ascii_local_part

        if local_part is None:
            errors.append(ValueError("email user name is not ascii"))
        else:
            try:
                check_user_exists(local_part)
            except Exception as e:
                errors.append(e)

    except Exception as e:
        errors.append(e)

    return ValidationResult(value=local_part, errors=errors)


def team_to_group_name(team: str) -> ValidationResult:
    """Convert a team name (which may be any arbitrary string)
    into PascalCase with non-alphabetic characters stripped.
    Words that are all uppercase remain uppercase.
    """
    cleaned_team = re.sub(r"[^A-Za-z ]", "", team)
    cleaned_words = [word if word.isupper() else word.capitalize() for word in cleaned_team.split()]
    result = "".join(cleaned_words)

    errors: list[Exception] = []

    if len(result) == 0:
        errors.append(ValueError("team was either all special characters or all spaces"))
        result = None

    if result is not None:
        try:
            check_group_exists(result)
        except Exception as e:
            errors.append(e)

    return ValidationResult(value=result, errors=errors)
