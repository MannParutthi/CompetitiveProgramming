# http://codeforces.com/contest/734/problem/A

noOfGames = input()
gameWinnersList = input()

antonWins = 0
danikWins = 0

for ele in gameWinnersList:
    if ele == 'A':
        antonWins += 1
    elif ele == 'D':
        danikWins += 1

if antonWins > danikWins:
    print("Anton")
elif danikWins > antonWins:
    print("Danik")
else:
    print("Friendship")
