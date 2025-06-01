import email_validator
import re


class ValidEmail:
    """Provides components of a validated email address"""
    def __init__(self, email: str) -> None:
        self._errors = []
        try:
            self.email = email_validator.validate_email(email)
            self.username = self.email.ascii_local_part
            self.domain = self.email.ascii_domain
        except email_validator.exceptions_types.EmailSyntaxError as e:
            self._errors.append(str(e))


# The username should be ValidEmail(email).username


# The group name should be taken from the Team field of the CSV.
# It should be in PascalCase format, and only contain ascii english letters.
def team_to_group_name(team_name: str) -> str:
    """Convert a team name (which may be any arbitray string) into PascalCase with non-alphabetic characters stripped."""
    cap_words = (re.sub(r'[^A-Za-z]', '', w).capitalize() for w in team_name.split())
    return ''.join(cap_words)
