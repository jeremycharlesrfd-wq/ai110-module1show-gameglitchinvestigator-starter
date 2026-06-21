from logic_utils import check_guess


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
