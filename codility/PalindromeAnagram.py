#!/usr/bin/python
# encoding: utf-8

# http://computersandbuildings.com/how-not-to-get-hired-by-neurobat/
# Task:
# Write a function solution(S) that, given a non-empty string S consisting
# of N characters, returns 1 if S is an anagram of some palindrome and
# returns 0 otherwise.
#
# Runtime / space expectation: O(n) / O(1)

def solution(S):
    """
    A string is an anagram of a palindrome if a maximum of one character
    occurs an odd number of times.
    """
    # It's ok to use a dict here, since the number of distinct ASCII/
    # Unicode characters is limited by a constant, so still O(1) space
    chars = {}
    for char in S:
        chars[char] = chars.get(char, 0) + 1

    nr_odd_chars = sum([occurs % 2 for occurs in chars.values()])

    return int(nr_odd_chars <= 1)



def main():
    assert(solution("dooernedeevrvn") == 1)
    assert(solution("a") == 1)
    assert(solution("aa") == 1)
    assert(solution("aba") == 1)
    assert(solution("abbbc") == 0)

    print "Passed all tests!"

if __name__ == '__main__':
    main()

# Time used: 16min incl. documentation and testing

