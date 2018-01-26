# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import deque


def solution(A):
    # write your code in Python 3.6
    equileaders = 0
    leaders_left = get_leaders(A)
    leaders_right = get_leaders(A[::-1])[::-1]
    for i in range(len(A)-1):
        left = leaders_left[i]
        right = leaders_right[i+1]

        if left == right and left is not None:
            equileaders += 1

    return equileaders


def get_leaders(A):
    result = []
    stack = deque()
    leader_counts = dict()
    for i in range(len(A)):
        x = A[i]
        if len(stack) == 0:
            stack.append(x)

        else:
            if x == stack[-1]:
                stack.append(x)
            else:
                stack.pop()

        if x in leader_counts:
            leader_counts[x] += 1
        else:
            leader_counts[x] = 1

        if len(stack) != 0:
            l = stack[-1]  # candidate
            if leader_counts[l] > (i + 1) / 2:
                result.append(l)
            else:
                result.append(None)
        else:
            result.append(None)
    return result
