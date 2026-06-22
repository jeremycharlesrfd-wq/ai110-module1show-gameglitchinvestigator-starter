from logic_utils import check_guess, get_range_for_difficulty, parse_guess


def test_winning_guess():
    # Equal guess and secret is a win.
    assert check_guess(50, 50) == ("Win", "🎉 Correct!")


def test_guess_too_high_tells_player_to_go_lower():
    # Regression: a guess above the secret must point the player LOWER.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_too_low_tells_player_to_go_higher():
    # Regression: a guess below the secret must point the player HIGHER.
    # This is the original bug report: secret 93, guess 50 -> "go higher".
    outcome, message = check_guess(50, 93)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_string_secret_is_compared_numerically():
    # Regression: a stringified secret used to trigger a lexicographic
    # comparison ("100" < "93"), flipping the direction. It must now be
    # compared as a number.
    assert check_guess(100, "93") == ("Too High", "📉 Go LOWER!")
    assert check_guess(50, "93") == ("Too Low", "📈 Go HIGHER!")
    assert check_guess(93, "93") == ("Win", "🎉 Correct!")


def test_hard_range_is_not_easier_than_normal():
    # Regression: Hard used to return (1, 50), a narrower range than Normal's
    # (1, 100), which made Hard easier to guess than Normal. Hard's range must
    # be at least as wide as Normal's.
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high >= normal_high


def test_parse_guess_accepts_valid_in_range():
    assert parse_guess("42", 1, 100) == (True, 42, None)
    # Whitespace around a valid guess is tolerated.
    assert parse_guess("  7 ", 1, 100) == (True, 7, None)
    # Range bounds are inclusive.
    assert parse_guess("1", 1, 100)[0] is True
    assert parse_guess("100", 1, 100)[0] is True


def test_parse_guess_rejects_negative():
    # Edge case: negatives can never equal a 1-100 secret; reject as out of range.
    ok, value, err = parse_guess("-5", 1, 100)
    assert ok is False
    assert value is None
    assert "range" in err.lower()


def test_parse_guess_rejects_decimals_outright():
    # Edge case: decimals must be rejected, not silently truncated to an int.
    for raw in ["3.7", "100.999", "-2.9", "1.5e3"]:
        ok, value, err = parse_guess(raw, 1, 100)
        assert ok is False, f"{raw!r} should be rejected"
        assert value is None
        assert "whole number" in err.lower()


def test_parse_guess_rejects_extremely_large_values():
    # Edge case: huge values parse without overflow but are out of range.
    ok, value, err = parse_guess("999999999999999999999999", 1, 100)
    assert ok is False
    assert "range" in err.lower()


def test_parse_guess_rejects_non_numbers_and_empty():
    assert parse_guess("abc", 1, 100)[0] is False
    assert parse_guess("", 1, 100) == (False, None, "Enter a guess.")
    assert parse_guess(None, 1, 100) == (False, None, "Enter a guess.")
