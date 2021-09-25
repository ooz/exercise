# https://codility.com/demo/take-sample-test/nesting/
# https://codility.com/demo/results/trainingYVY6XZ-ZZX/

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(S):
    # write your code in Python 2.7
    stack_size = 0
    for i in xrange(len(S)):
        c = S[i]
        if c == "(":
            stack_size += 1
        elif c == ")":
            stack_size -= 1
        if stack_size < 0:
            return 0
    if stack_size == 0:
        return 1
    return 0

def better_solution(S):
    stack_size = 0
    for c in S:
        if c == "(":
            stack_size += 1
        elif c == ")":
            stack_size -= 1
        if stack_size < 0:
            return 0
    if stack_size == 0:
        return 1
    return 0
