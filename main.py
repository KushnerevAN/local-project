def recursive_flatten_generator(array: Iterable) -> List:
    """
    Recursive algorithm
    Looks like recursive_flatten_iterator, but with extend/append

    """
    lst = []
    for i in array:
        if isinstance(i, list):
            lst.extend(recursive_flatten_generator(i))
        else:
            lst.append(i)
    return lst






