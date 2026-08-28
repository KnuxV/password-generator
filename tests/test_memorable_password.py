from strong_password import StrongPassword, TypePassword


# Five words of at least three letters plus four spaces: longer than 20 characters.
def test_length_memorable(memorable_password):
    assert len(memorable_password) > 20


def test_lowercase(memorable_password):
    assert any(char.islower() for char in memorable_password)


def test_uppercase(memorable_password):
    assert any(char.isupper() for char in memorable_password)


# Five words → four spaces.
def test_has_spaces(memorable_password):
    assert memorable_password.count(" ") == 4


# Same checks without the fixture: generate on demand.
def test_length_memorable_direct():
    password = StrongPassword(length=5, type_p=TypePassword.MEMORABLE).generate()
    assert len(password) > 20


def test_word_count_direct():
    password = StrongPassword(length=3, type_p=TypePassword.MEMORABLE).generate()
    assert len(password.split(" ")) == 3
