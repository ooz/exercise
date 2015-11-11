# https://codility.com/demo/take-sample-test/frog_jmp/
# https://codility.com/demo/results/trainingEHXVQK-X5Z/

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(X, Y, D):
    # write your code in Python 2.7
    jumps = (Y - X) / D
    if (Y - X) % D != 0:
        jumps += 1
    return jumps
