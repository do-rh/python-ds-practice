def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    lst_phrase = list(phrase)
    lst_phrase.reverse()
    reversed_string = ""
    return reversed_string.join(lst_phrase)

    #look at soln