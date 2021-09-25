# https://codility.com/demo/take-sample-test/distinct/
# https://codility.com/demo/results/trainingXNTBKD-FN5/

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    values = {}
    for elem in A:
        values[elem] = 1
    return len(values.keys())

def better_solution(A):
    return len(set(A))
