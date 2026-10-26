import math

def weeks_elapsed (day1: int, day2: int) -> str:
    """
    Berekent het aantal volle weken dat verstreken is tussen twee dagen
    in hetzelfde jaar. De dagen zijn gegeven als dagnummer (day1 en day2).

    >>> weeks_elapsed(3, 20)
    2
    >>> weeks_elapsed(20, 3)
    2
    >>> weeks_elapsed(8, 5)
    0

    >>> weeks_elapsed(40, 61)
    3

    """
    weken = abs(day2 - day1) // 7)
    
    return print(f"Weken voorbij: {weken}")
    
weeks_elapsed(3, 20)
weeks_elapsed(20, 3)
weeks_elapsed(8, 5)
weeks_elapsed(40, 61)