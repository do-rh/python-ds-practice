def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    high_count = 0
    

    for num in nums: 
        count = nums.count(num)
        if count > high_count:
            high_count = count
            high_num = num

    return high_num

        