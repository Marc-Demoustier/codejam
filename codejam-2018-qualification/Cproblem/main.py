# -*- coding: utf-8 -*-
import fileinput
import math
import codejamhelpers


def solve(n, k):
    return 42


f = fileinput.input()

T = int(f.readline())
for case in range(1, T+1):
    # N = int(f.readline())
    N, K = (int(x) for x in f.readline().split)
    solution = solve(N, K)
    print("Case #{case}: {solution}")
