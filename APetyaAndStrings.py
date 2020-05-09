# http://codeforces.com/contest/112/problem/A

firstString = input()
secondString = input()

if firstString.lower() < secondString.lower():
    print(-1)
elif secondString.lower() < firstString.lower():
    print(1)
else:
    print(0)
