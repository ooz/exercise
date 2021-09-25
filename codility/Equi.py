# https://codility.com/demo/take-sample-test/
# https://codility.com/demo/results/demo8FQ64J-WQA/

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    sum = 0
    for elem in A:
        sum += elem

    sum_r2l = 0
    for i in xrange(len(A) - 1, -1, -1):
        if sum - A[i] == sum_r2l:
            return i
        sum_r2l += A[i]
        sum -= A[i]

    return -1

