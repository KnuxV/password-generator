from zxcvbn import zxcvbn


# A five-word passphrase should get the top score from zxcvbn.
def test_zxcvbn_score(memorable_password):
    assert zxcvbn(memorable_password)["score"] == 4


def test_zxcvbn_time(memorable_password):
    crack_time = zxcvbn(memorable_password)["crack_times_display"]["offline_slow_hashing_1e4_per_second"]
    assert crack_time == "centuries"
