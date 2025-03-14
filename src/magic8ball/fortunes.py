import os
import json

# Determine the path to the data file within the package
DATA_PATH = os.path.join(os.path.dirname(__file__), 'data.json')

with open(DATA_PATH, 'r') as f:
    DATA = json.load(f)


class Magic8Ball:
    @staticmethod
    def tell_fortune() -> str:
        """Return a random general fortune."""
        # TODO
        return

    @staticmethod
    def personalized_fortune(name: str) -> str:
        """Return a personalized fortune including the given name."""
        # TODO
        return

    @staticmethod
    def fortune_by_category(category: str) -> str:
        """Return a fortune from the specified category (e.g., 'love', 'career', 'health')."""
        # TODO
        return

    @staticmethod
    def daily_by_birth_month(month: str) -> str:
        """
        Return a fortune for the given birth month.
        """
        # TODO
        return
