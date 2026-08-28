import pytest

from strong_password import StrongPassword, TypePassword


# Fixtures: a password generated once per test that asks for it.
@pytest.fixture
def random_password():
    return StrongPassword(length=12, type_p=TypePassword.RANDOM).generate()


@pytest.fixture
def memorable_password():
    return StrongPassword(length=5, type_p=TypePassword.MEMORABLE).generate()
