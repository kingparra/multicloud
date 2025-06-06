import time

import pytest

from import_users.password import generate_password


def test_generate_password_invalid_length():
    """Test that ValueError is raised when length is too short"""
    with pytest.raises(ValueError) as exc_info:
        generate_password(length=5)
    assert str(exc_info.value) == "length must be greater than or equal to lower + upper + digit + punct"


def test_generate_password_performance():
    """Test that password generation completes within reasonable time"""
    start_time = time.perf_counter()

    # Generate 100 passwords with default settings
    for _ in range(100):
        generate_password()

    duration = time.perf_counter() - start_time

    # Should generate 100 passwords in under 1 second
    # This is a generous threshold - adjust based on requirements
    assert duration < 1.0, f"Password generation too slow: {duration:.2f} seconds"


def test_randomness_distribution():
    # Generate a bunch of passwords and analyze character distribution
    from collections import Counter

    num_samples = 1000
    pw_length = 30
    chars_seen = Counter()

    for _ in range(num_samples):
        pw = generate_password(length=pw_length)
        chars_seen.update(pw)

    # assert no one character dominates
    top_char, top_count = chars_seen.most_common(1)[0]
    assert top_count < num_samples * pw_length * 0.2, f"Character '{top_char}' appears disproportionately"


def test_negative_min_lower_raises():
    with pytest.raises(ValueError):
        generate_password(length=10, min_lower=-1)
    with pytest.raises(ValueError):
        generate_password(length=10, min_upper=-1)
    with pytest.raises(ValueError):
        generate_password(length=10, min_digit=-1)
    with pytest.raises(ValueError):
        generate_password(length=10, min_punct=-1)
