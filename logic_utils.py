def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 100  # FIX: was 1, 50 (narrower than Normal); widened so Hard isn't easier than Normal
    return 1, 100


def parse_guess(raw: str, low: int = 1, high: int = 100):
    """
    Parse user input into an int guess and validate it against [low, high].

    Decimals (e.g. "3.7") are rejected outright rather than truncated, so the
    player always knows exactly which number was scored.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    raw = raw.strip()
    if raw == "":
        return False, None, "Enter a guess."

    try:
        # int() rejects decimals and scientific notation, so "3.7" / "1e9"
        # fall through to the error message below instead of being truncated.
        value = int(raw)
    except Exception:
        return False, None, "Enter a whole number."

    if not (low <= value <= high):
        return False, None, f"Out of range. Pick a number from {low} to {high}."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # Compare numerically so a stringified secret can't trigger a
    # lexicographic comparison (e.g. "100" < "93").
    guess = int(guess)
    secret = int(secret)

    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        # Guess is above the secret -> the player should aim lower.
        return "Too High", "📉 Go LOWER!"

    # Guess is below the secret -> the player should aim higher.
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        # FIX: attempt_number is already 1-based; dropped the extra +1 that double-counted it.
        points = 100 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
