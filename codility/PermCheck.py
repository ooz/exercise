# https://codility.com/demo/take-sample-test/perm_check/
# https://codility.com/demo/results/trainingGX6G5T-B9H/

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    bs = range(len(A))
    if len(bs) > 0:
        bs[0] = 1
    for a in A:
        if a > 0 and a - 1 < len(A):
            if bs[a - 1] != 0:
                bs[a - 1] = 0
            else:
                bs[a - 1] = 1
    s = sum(bs)
    if s > 0:
        return 0
    return 1

