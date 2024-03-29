def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    counter = {}
    for ltr in phrase:
        if counter.get(ltr) is None:
            counter[ltr] = 1
        else:
            counter[ltr] = counter[ltr] + 1
    return counter

    #look at soln
       counter = {}
    for ltr in phrase:
        if counter.get(ltr, 0) is None:
            counter[ltr] = 1
        else:
            counter[ltr] = counter[ltr] + 1
    return counter