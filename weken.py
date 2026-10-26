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
    if day2 > day1:
        dag1 = day2
    else:
        dag1 = day1
    
    dagen_verstreken = day2 - dag1
    
    weken = dagen_verstreken // 7
    return print(f"Er zijn {weken} weken weken verstreken")
    
weeks_elapsed(3, 20)