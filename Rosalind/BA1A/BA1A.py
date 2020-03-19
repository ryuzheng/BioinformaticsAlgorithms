# -*- coding: utf-8 -*-
import sys


def PatternCount(text, pattern):
    count = 0
    for i in range(0, len(text) - len(pattern) + 1):
        # print(text[i:i + len(pattern)])
        if text[i:i + len(pattern)] == pattern:
            count += 1
    return count


with open(sys.argv[1], 'r') as fi:
    text = fi.readline().rstrip()
    pattern = fi.readline().rstrip()

    print(PatternCount(text, pattern))

# print(PatternCount('GCGCG', 'GCG'))
