import os
import json
import random

# Determine the path to the data file within the package
DATA_PATH = os.path.join(os.path.dirname(__file__), 'data.json')

with open(DATA_PATH, 'r') as f:
    DATA = json.load(f)


class Magic8Ball:

    DATA = DATA
    
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
        Returns a personalized fortune message based on the given birth month.
        
        Parameters:
            month (str): The name of the birth month.
        
        Returns:
            str: A randomly selected fortune message for the given month.
        
        Raises:
            TypeError: If the input is not a string.
            ValueError: If the input is not a valid month name.
        """
        if not isinstance(month, str):
            raise TypeError("Invalid input: The month must be provided as a string.")

        birthdays = DATA["birthdays"]
        month = month.capitalize()  

        if month in birthdays:
            return random.choice(birthdays[month]) 
        else:
            raise ValueError("Invalid month: Please enter a valid month name (e.g., 'January', 'February').")


