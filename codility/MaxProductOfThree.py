# https://codility.com/demo/take-sample-test/max_product_of_three/
# https://codility.com/demo/results/trainingP5DBKD-4ZM/

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    A.sort()
    return max(A[-1] * A[-2] * A[-3], A[-1] * A[0] * A[1])
