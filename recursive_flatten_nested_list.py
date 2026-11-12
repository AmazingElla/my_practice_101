def flatten(nested: list, index: int = 0) -> list:
    if type(nested) != list:
        raise TypeError("Input must be a list")
    if nested == []:
        return []
    first = nested[0]
    if type(first) == list:
        first = flatten(first)
    else:
        first = [first]
    rest = flatten(nested[1:])

    return first + rest


"""
    Recursively flattens an arbitrarily nested list of items.

    Args:
        nested (list): The nested list.
        index (int): Pointer index in the current list level.

    Returns:
        list: A 1D flattened list.

    Raises:
        TypeError: If nested is not a list.
    """