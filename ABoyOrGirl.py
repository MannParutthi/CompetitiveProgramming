# http://codeforces.com/contest/236/problem/A

username = input()

uniqueCharacters = ''.join(set(username))

if len(uniqueCharacters) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
