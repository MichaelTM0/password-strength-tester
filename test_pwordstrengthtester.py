from pwordstrengthtester import analyze_password

LENGTH = "at least 8 characters"
UPPER = "at least 1 uppercase letter"
LOWER = "at least 1 lowercase letter"
NUMBER = "at least 1 number"
SPECIAL = "at least 2 special characters"


def test_strong_password_passes_every_rule():
    results = analyze_password("Str0ng!!")
    assert all(results.values())


def test_too_short_fails_length_rule():
    results = analyze_password("Ab1!!")
    assert results[LENGTH] is False


def test_no_uppercase_fails_uppercase_rule():
    results = analyze_password("str0ng!!")
    assert results[UPPER] is False


def test_no_lowercase_fails_lowercase_rule():
    results = analyze_password("STR0NG!!")
    assert results[LOWER] is False


def test_no_number_fails_number_rule():
    results = analyze_password("Strong!!")
    assert results[NUMBER] is False


def test_one_special_character_fails_special_rule():
    results = analyze_password("Abcdef1!")
    assert results[SPECIAL] is False


def test_two_special_characters_passes_special_rule():
    results = analyze_password("Abcde1!!")
    assert results[SPECIAL] is True


def test_empty_password_fails_every_rule():
    results = analyze_password("")
    assert not any(results.values())
