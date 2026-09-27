def is_palindrome(s):
    """Check whether a string is a palindrome."""
    return s == s[::-1]


def count_vowels(s):
    """Count the number of vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)


def fahrenheit_to_celsius(f):
    """Convert temperature from Fahrenheit to Celsius."""
    return (f - 32) * 5 / 9


# Example usage
print(is_palindrome("madam"))
print(count_vowels("Artificial Intelligence"))
print(fahrenheit_to_celsius(98.6))