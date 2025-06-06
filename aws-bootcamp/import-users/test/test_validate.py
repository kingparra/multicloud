import pytest

from import_users.validate import team_to_group_name


def test_team_name_to_group_name():
    """Test conversion of team names to IAM group names"""
    # Basic conversion
    assert team_to_group_name("Database Admin") == "DatabaseAdmin"
    assert team_to_group_name("Network Admin") == "NetworkAdmin"
    assert team_to_group_name("Cloud Architect") == "CloudArchitect"

    # Preserve uppercase words
    assert team_to_group_name("IT Support") == "ITSupport"
    assert team_to_group_name("DBA Team") == "DBATeam"
    assert team_to_group_name("AWS SRE Team") == "AWSSRETeam"
    assert team_to_group_name("CORE Infrastructure") == "COREInfrastructure"
    assert team_to_group_name("QA Testing") == "QATesting"

    # Don't preserve mixed case
    assert team_to_group_name("DevOps Team") == "DevopsTeam"
    assert team_to_group_name("iOS Team") == "IosTeam"

    # Special characters and spaces
    assert team_to_group_name("Front-end Developers") == "FrontendDevelopers"
    assert team_to_group_name("Security & Compliance") == "SecurityCompliance"

    # Multiple spaces and unusual formatting
    assert team_to_group_name("Data   Science") == "DataScience"
    assert team_to_group_name(" Machine Learning ") == "MachineLearning"

    # Edge cases
    with pytest.raises(ValueError):
        team_to_group_name("")
    with pytest.raises(ValueError):
        team_to_group_name("   ")
    with pytest.raises(ValueError):
        team_to_group_name("123 456")
    with pytest.raises(ValueError):
        team_to_group_name("!@#$%")
