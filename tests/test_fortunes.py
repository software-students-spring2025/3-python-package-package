import pytest
from src.magic8ball.fortunes import Magic8Ball

class TestMagic8Ball:
    """Test suite for Magic8Ball's daily_by_birth_month function."""

    @pytest.mark.parametrize("month", ["January", "February", "March"])
    def test_valid_month(self, month):
        """Test that a valid month returns a message from the correct list."""
        assert Magic8Ball.daily_by_birth_month(month) in Magic8Ball.DATA["birthdays"][month]

    @pytest.mark.parametrize("month, expected",
        [
            ("january", "January"),
            ("FEBRUARY", "February"),
            ("MarCh", "March"),
        ]
    )
    def test_case_insensitivity(self, month, expected):
        """Test that the function handles different cases correctly."""
        assert Magic8Ball.daily_by_birth_month(month) in Magic8Ball.DATA["birthdays"][expected]

    @pytest.mark.parametrize("invalid_month", ["NotAMonth", "Octember", "1234", ""])
    def test_invalid_month(self, invalid_month):
        """Test that an invalid month raises a ValueError."""
        with pytest.raises(ValueError, match="Invalid month: Please enter a valid month name"):
            Magic8Ball.daily_by_birth_month(invalid_month)

    @pytest.mark.parametrize("invalid_input", [123, None, ["January"], {"month": "January"}])
    def test_non_string_input(self, invalid_input):
        """Test that non-string inputs raise a TypeError."""
        with pytest.raises(TypeError, match="Invalid input: The month must be provided as a string."):
            Magic8Ball.daily_by_birth_month(invalid_input)

    def test_random_fortune_selection(self):
        """Test that the function always returns a valid fortune from the respective month."""
        month = "January"
        for _ in range(10):  # Run multiple times to verify randomness
            assert Magic8Ball.daily_by_birth_month(month) in Magic8Ball.DATA["birthdays"][month]
