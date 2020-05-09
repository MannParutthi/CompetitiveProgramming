# http://codeforces.com/contest/405/problem/A

noOfColumns = input()
noOfCubesInEachColumn = [int(x) for x in input().split(' ')]

print(' '.join([str(x) for x in sorted(noOfCubesInEachColumn)]))
