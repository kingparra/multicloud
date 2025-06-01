from import_users.validate import team_to_group_name
import pytest
from icecream import ic


def test_team_to_group_name():
# Test cases based on the Team column from sample-input.csv
    assert team_to_group_name("Database Admin") == "DatabaseAdmin"
    assert team_to_group_name("Network Admin") == "NetworkAdmin"
    assert team_to_group_name("Cloud Architect") == "CloudArchitect"
    assert team_to_group_name("Linux Admin") == "LinuxAdmin"
    assert team_to_group_name("Trainee") == "Trainee"
   asse ass
    ert team_to_group_name("Gn/\\arly Words of wordyness") == "GnarlyWordsOfWordyness"
