#!/usr/bin/python3
"""Island perimeter module.
"""


def island_perimeter(grid):
    """Computes the perimeter of an island without any lakes.
    """
    perimeter = 0
    if type(grid) != list:
        return 0
    n = len(grid)
    for k, row in enumerate(grid):
        l = len(row)
        for e, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                k == 0 or (len(grid[k - 1]) > e and grid[k - 1][e] == 0),
                e == l - 1 or (m > e + 1 and row[e + 1] == 0),
                k == n - 1 or (len(grid[k + 1]) > e and grid[k + 1][e] == 0),
                e == 0 or row[e - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter
