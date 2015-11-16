#!/usr/bin/python
# encoding: utf-8

# A Codility task (from memory)
#
# S is a set of integers s having the form s = 2**p * 3**q
# (p, q: non-negative integers).
# A is the sorted ascending list of all integers in S.
# For a given integer N (0 <= N <= 200) find A[N].
# Runtime is of no concern.

from math import sqrt

def naive_solution(N):
    """
    O(n ** 2) time complexity
    O(n ** 2) space complexity
    """
    pq_ints = []
    upper = N + 1
    for p in xrange(upper):
        for q in xrange(upper):
            pq_ints.append(2**p * 3**q)
    pq_ints = list(set(pq_ints))
    pq_ints.sort()
    return pq_ints[N]

def better_solution(N):
    """
    O(n * log(n)) time complexity
    O(n) space complexity
    """
    pq_ints = []
    upper = 2 * int(sqrt(N)) + 1
    for p in xrange(upper):
        for q in xrange(upper):
            pq_ints.append(2**p * 3**q)
    pq_ints = list(set(pq_ints))
    pq_ints.sort()
    return pq_ints[N]

def best_solution(N):
    """
    There probably is a solution in O(n) space and time.
    """
    pass

def main():
    for i in xrange(501):
        bs = better_solution(i)
        ns = naive_solution(i)
        assert(ns == bs)
        print "A[%i] = %i" % (i, bs)

if __name__ == '__main__':
    main()
