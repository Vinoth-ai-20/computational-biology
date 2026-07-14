def gc_content(sequence: str) -> float:
    """
    Calculate GC content of a DNA sequence.

    Parameters
    ----------
    sequence : str
        DNA sequence string (A, T, G, C, N allowed; case-insensitive)

    Returns
    -------
    float
        Fraction of bases that are G or C (0.0-1.0). N bases are excluded
        from the denominator (unknown bases don't count).

    Raises
    ------
    ValueError
        If sequence is empty.

    Examples
    --------
    >>> gc_content("ATGC")
    0.5
    >>> gc_content("AAAA")
    0.0
    """
    raise NotImplementedError("Module 16 exercise — implement per the docstring above.")
