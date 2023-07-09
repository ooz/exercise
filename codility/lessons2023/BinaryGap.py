#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
# Time needed: ca. 15 minutes

def solution(N):
    binaryString = "{0:b}".format(N)
    counts = [0]
    count = 0
    previousDigit = None
    for digit in binaryString:
        if previousDigit == '1' and digit == '0':
            count = 1
        elif previousDigit == '0' and digit == '0':
            count += 1
        elif previousDigit == '0' and digit == '1':
            counts.append(count)
            count = 0
        previousDigit = digit
    return max(counts)


if __name__ == "__main__":
    assert solution(9) == 2
    assert solution(529) == 4
    assert solution(20) == 1
    assert solution(15) == 0
    assert solution(32) == 0
    assert solution(1041) == 5
    print("Green!")

