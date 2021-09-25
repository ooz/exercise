# https://codility.com/demo/take-sample-test/tie_ropes/
# https://codility.com/demo/results/training4WY49X-XTM/

# score is only 75% (50% correctness)

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(K, A):
    # write your code in Python 2.7
    tied_rope = 0
    nr_ropes = 0
    for rope in A:
        if rope >= K:
            nr_ropes += 1
        else:
            tied_rope += rope
            if tied_rope >= K:
                nr_ropes += 1
                tied_rope = 0
    return nr_ropes

