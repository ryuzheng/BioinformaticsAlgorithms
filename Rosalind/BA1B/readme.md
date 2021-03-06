# Find the Most Frequent Words in a String

We say that Pattern is a most frequent k-mer in Text if it maximizes Count(Text, Pattern) among all k-mers. For example, "ACTAT" is a most frequent 5-mer in "ACAACTATGCATCACTATCGGGAACTATCCT", and "ATA" is a most frequent 3-mer of "CGATATATCCATAG".

## Frequent Words Problem
Find the most frequent k-mers in a string.

Given: A DNA string Text and an integer k.

Return: All most frequent k-mers in Text (in any order).

## Sample Dataset
```
ACGTTGCATGTCGCATGATGCATGAGAGCT
4
```
## Sample Output
```
CATG GCAT
```