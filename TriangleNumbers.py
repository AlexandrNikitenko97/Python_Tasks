"""
We need to saw the stick.
The length of the stick is N inches. We should help our robots saw the stick.
All of the parts should have integer lengths (1, 2, 3 .. inches, but not 1.2).
As we love the numerical series and especially the Triangular numbers,
you should saw the stick so that the lengths form the consecutive fragment of the Triangular numbers series with
the maximum quantity (fragment's length). The parts should have different lengths (no repeating).
For example: 64 should divided at 15, 21, 28, because 28, 36 is shorter and 1, 3, 15, 45 is not a consecutive fragment.

You are given a length of the stick (N).
You should return the list of lengths (integers) for the parts in ascending order.
 If it's not possible and the problem does not have a solution, then you should return an empty list.

Input: A length of the stick as an integer.

Output: A fragment of the Triangular numbers as a list of integers (sorted in ascending order) or an empty list.

Example:

stick(64) == [15, 21, 28]
stick(371) == [36, 45, 55, 66, 78, 91]
stick(225) == [105, 120]
stick(882) == []

"""


def stick(n):
    chain = []
    num = 0
    iteration = 1
    while num <= n:
        chain.append(num)
        num += iteration
        iteration += 1
    count = 0
    chain.remove(0)
    for i in chain:
        result = []
        count += 1
        for j in range(count, len(chain)):
            result.append(chain[j-1])
            result.append(chain[j])
            i += chain[j]
            if i == n:
                return sorted(list(set(result)))
    return []
