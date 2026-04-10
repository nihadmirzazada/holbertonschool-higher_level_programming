#!/usr/bin/python3
"""Module for MyList class."""


class MyList(list):
    """Inherits from list with print_sorted method."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
