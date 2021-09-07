def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    lst_phrase = []
    for ltr in phrase:
        if ltr != " ": #.replace()
            lst_phrase.append(ltr.lower())
    rev_phrase = lst_phrase.copy()
    rev_phrase.reverse()
    if rev_phrase == lst_phrase: 
        return True
    return False

    #slice(::-1).
    #