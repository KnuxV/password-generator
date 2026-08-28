"""Compare the strength of a memorable and a random password.

Uses the `zxcvbn` library (the project's one dependency) to estimate how long
each password would take to crack.

    uv run compute_crack_time.py
"""

from zxcvbn import zxcvbn

from strong_password import StrongPassword, TypePassword


def report(password: str, label: str) -> None:
    """Print the zxcvbn score (0-4) and estimated crack time of a password."""
    results = zxcvbn(password)
    score = results["score"]
    crack_time = results["crack_times_display"]["offline_slow_hashing_1e4_per_second"]
    print(f"\n{label}")
    print(f"  password:   {password}")
    print(f"  score:      {score}/4")
    print(f"  crack time: {crack_time}")


def main() -> None:
    memorable = StrongPassword(length=4, type_p=TypePassword.MEMORABLE).generate()
    report(memorable, "Memorable, 4 words")

    random_p = StrongPassword(length=12, type_p=TypePassword.RANDOM).generate()
    report(random_p, "Random, 12 characters")


if __name__ == "__main__":
    main()
