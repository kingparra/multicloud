from moto import mock_aws

from import_users.validate import email_to_user_name, team_to_group_name


def test_email_to_user_name_valid():
    """Test conversion of valid emails to IAM usernames"""
    result = email_to_user_name("john.doe@example.com")
    assert result.value == "john.doe"
    assert not result.errors

    result = email_to_user_name("first.last@company.com")
    assert result.value == "first.last"
    assert not result.errors


def test_email_to_user_name_invalid():
    """Test handling of invalid email addresses"""
    result = email_to_user_name("not-an-email")
    assert result.value is None
    assert len(result.errors) == 1
    assert isinstance(result.errors[0], Exception)

    result = email_to_user_name("")
    assert result.value is None
    assert len(result.errors) == 1


def test_email_to_user_name_non_ascii():
    """Test handling of non-ASCII characters in email"""
    result = email_to_user_name("josé.garcía@example.com")
    assert result.value is None
    assert result.errors


def test_team_to_group_name_basic():
    """Test basic team name conversions"""
    result = team_to_group_name("Database Admin")
    assert result.value == "DatabaseAdmin"
    assert not result.errors

    result = team_to_group_name("Network Admin")
    assert result.value == "NetworkAdmin"
    assert not result.errors

    result = team_to_group_name("Cloud Architect")
    assert result.value == "CloudArchitect"
    assert not result.errors


def test_team_to_group_name_uppercase():
    """Test preservation of uppercase words"""
    result = team_to_group_name("IT Support")
    assert result.value == "ITSupport"
    assert not result.errors

    result = team_to_group_name("DBA Team")
    assert result.value == "DBATeam"
    assert not result.errors

    result = team_to_group_name("AWS SRE Team")
    assert result.value == "AWSSRETeam"
    assert not result.errors

    result = team_to_group_name("CORE Infrastructure")
    assert result.value == "COREInfrastructure"
    assert not result.errors

    result = team_to_group_name("QA Testing")
    assert result.value == "QATesting"
    assert not result.errors


def test_team_to_group_name_mixed_case():
    """Test handling of mixed case team names"""
    result = team_to_group_name("DevOps Team")
    assert result.value == "DevopsTeam"
    assert not result.errors

    result = team_to_group_name("iOS Team")
    assert result.value == "IosTeam"
    assert not result.errors


def test_team_to_group_name_special_chars():
    """Test handling of special characters and spaces"""
    result = team_to_group_name("Front-end Developers")
    assert result.value == "FrontendDevelopers"
    assert not result.errors

    result = team_to_group_name("Security & Compliance")
    assert result.value == "SecurityCompliance"
    assert not result.errors


def test_team_to_group_name_multiple_spaces():
    """Test handling of multiple spaces and unusual formatting"""
    result = team_to_group_name("Data   Science")
    assert result.value == "DataScience"
    assert not result.errors

    result = team_to_group_name(" Machine Learning ")
    assert result.value == "MachineLearning"
    assert not result.errors


@mock_aws
def test_team_to_group_name_invalid():
    """Test handling of invalid team names"""
    result = team_to_group_name("")
    assert result.value is None
    assert len(result.errors) == 1
    assert "all special characters or all spaces" in str(result.errors[0])

    result = team_to_group_name("   ")
    assert result.value is None
    assert len(result.errors) == 1

    result = team_to_group_name("123 456")
    assert result.value is None
    assert len(result.errors) == 1

    result = team_to_group_name("!@#$%")
    assert result.value is None
    assert len(result.errors) == 1
