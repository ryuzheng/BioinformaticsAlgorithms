# -*- coding: utf-8 -*-
import sys
# from collections import Counter


def frequent_kmer(text, length):
    kmers = {}
    for i in range(0, len(text) - length + 1):
        kmer = text[i:i + length]
        kmers.setdefault(kmer, 0)
        kmers[kmer] += 1

    # kmers = Counter(kmers)
    return ' '.join([k for k, v in kmers.items() if v == max(kmers.values())])


with open(sys.argv[1], 'r') as fi:
    text = fi.readline().strip()
    length = int(fi.readline().strip())

    print(frequent_kmer(text, length))

# print(frequent_kmer('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4))
