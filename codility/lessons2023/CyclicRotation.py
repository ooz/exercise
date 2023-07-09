#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
# Time needed: ca. 8 min

from collections import deque

def solution(A, K):
    d = deque(A)
    d.rotate(K)
    return list(d)

if __name__ == "__main__":
    assert solution([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]
    assert solution([0, 0, 0], 1) == [0, 0, 0]
    assert solution([1, 2, 3, 4], 4) == [1, 2, 3, 4]
    print("Green!")