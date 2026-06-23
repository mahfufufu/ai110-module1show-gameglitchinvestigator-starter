from logic_utils import check_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_string_secret_numeric():
    # Numeric secret represented as a string should compare numerically
    assert check_guess(50, "50") == "Win"
    assert check_guess(60, "50") == "Too High"
    assert check_guess(40, "50") == "Too Low"


def test_string_guess_numeric_secret():
    # Numeric guess represented as a string should compare numerically
    assert check_guess("60", 50) == "Too High"
    assert check_guess("40", 50) == "Too Low"


def test_app_hint_mapping_and_initial_state_is_correct():
    # Importing the Streamlit app module should initialize the expected
    # hint mapping and default session state. We clear session state
    # first to keep imports idempotent across test runs.
    import importlib
    import sys
    import streamlit as st

    # Ensure a fresh import of the app module
    if "app" in sys.modules:
        del sys.modules["app"]

    st.session_state.clear()
    app = importlib.import_module("app")

    # Hint mapping should match the fixed mappings in the app
    expected = {
        "Win": "🎉 Correct!",
        "Too High": "📉 Go LOWER!",
        "Too Low": "📈 Go HIGHER!",
    }
    assert getattr(app, "HINT_MESSAGES") == expected

    # After import the app should set attempts to 0 and status to "playing"
    assert st.session_state.attempts == 0
    assert st.session_state.status == "playing"
