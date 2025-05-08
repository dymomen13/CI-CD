"""Implementacja funkcji"""


def add(a: int, b: int) -> int:
    """
    Funkcja dodająca dwie liczby.

    Args:
        a (int): Pierwsza liczba.
        b (int): Druga liczba.

    Returns:
        int: Suma dwóch liczb.
    """
    return a + b


def subtract(a: int, b: int) -> int:
    """
    Funkcja odejmująca dwie liczby.

    Args:
        a (int): Pierwsza liczba.
        b (int): Druga liczba.

    Returns:
        int: Różnica dwóch liczb.
    """
    return a - b


def multiply(a: int, b: int) -> int:
    """
    Funkcja mnożąca dwie liczby.

    Args:
        a (int): Pierwsza liczba.
        b (int): Druga liczba.

    Returns:
        int: Iloczyn dwóch liczb.
    """
    return a * b


def divide(a: int, b: int) -> float:
    """
    Funkcja dzieląca dwie liczby.

    Args:
        a (int): Pierwsza liczba.
        b (int): Druga liczba.

    Returns:
        float: Wynik dzielenia.
    """
    if b == 0:
        raise ValueError("Nie można dzielić przez zero.")
    return a / b
