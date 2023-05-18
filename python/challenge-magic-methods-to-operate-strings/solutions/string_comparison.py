class MyString:
    def __init__(self, string: str):
        self.string = string

    def __eq__(self, other: "MyString") -> bool:
        """Compare two MyString objects for equality.

        Args:
            other (MyString): The other MyString object to compare with.

        Returns:
            bool: True if the two MyString objects are equal, False otherwise.
        """
        return self.string == other.string

    def __ne__(self, other: "MyString") -> bool:
        """Compare two MyString objects for inequality.

        Args:
            other (MyString): The other MyString object to compare with.

        Returns:
            bool: True if the two MyString objects are not equal, False otherwise.
        """
        return self.string != other.string

    def __lt__(self, other: "MyString") -> bool:
        """Compare two MyString objects for less than.

        Args:
            other (MyString): The other MyString object to compare with.

        Returns:
            bool: True if the current MyString object is less than the other MyString object, False otherwise.
        """
        return self.string < other.string

    def __le__(self, other: "MyString") -> bool:
        """Compare two MyString objects for less than or equal to.

        Args:
            other (MyString): The other MyString object to compare with.

        Returns:
            bool: True if the current MyString object is less than or equal to the other MyString object, False otherwise.
        """
        return self.string <= other.string

    def __gt__(self, other: "MyString") -> bool:
        """Compare two MyString objects for greater than.

        Args:
            other (MyString): The other MyString object to compare with.

        Returns:
            bool: True if the current MyString object is greater than the other MyString object, False otherwise.
        """
        return self.string > other.string

    def __ge__(self, other: "MyString") -> bool:
        """Compare two MyString objects for greater than or equal to.

        Args:
            other (MyString): The other MyString object to compare with.

        Returns:
            bool: True if the current MyString object is greater than or equal to the other MyString object, False otherwise.
        """
        return self.string >= other.string
