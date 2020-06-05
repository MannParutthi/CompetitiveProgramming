# https://codeforces.com/contest/443/problem/A

listOfLetters = (input().replace('{', '').replace('}', '')).split(', ')

if listOfLetters == ['']:
    print(0)
else:
    print(len(set(listOfLetters)))
