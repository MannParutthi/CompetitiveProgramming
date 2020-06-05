# https://codeforces.com/contest/339/problem/A

sumWrittenOnBoard = [int(x) for x in input().split('+')]

print('+'.join([str(x) for x in sorted(sumWrittenOnBoard)]))
