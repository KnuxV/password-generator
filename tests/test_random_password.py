SPECIAL = "!@#$%^&*()-_=+[]{}|;:,.<>?"


def test_length_random(random_password):
    assert len(random_password) == 12


def test_has_special(random_password):
    assert any(char in SPECIAL for char in random_password)


def test_has_digits(random_password):
    assert any(char.isdigit() for char in random_password)


def test_has_lowercase(random_password):
    assert any(char.islower() for char in random_password)


def test_has_uppercase(random_password):
    assert any(char.isupper() for char in random_password)
