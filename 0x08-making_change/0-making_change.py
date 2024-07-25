#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    Return the minimum number of coins needed for the given total to  be met
    Args:
        coins (list of ints): a list of coins of different values
        total (int): total value to be met
    Return:
        Number of coins or -1 if meeting the total is not possible
    """
    if total <= 0:
        return 0
    if coins == [] or coins is None:
        return -1
    try:
        n = coins.index(total)
        return 1
    except ValueError:
        pass

    coins.sort(reverse=True)
    coin_count = 0
    for k in coins:
        if total % k == 0:
            coin_count += int(total / k)
            return coin_count
        if total - k >= 0:
            if int(total / k) > 1:
                coin_count += int(total / k)
                total = total % k
            else:
                coin_count += 1
                total -= k
                if total == 0:
                    break
    if total > 0:
        return -1
    return coin_count
