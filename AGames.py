# https://codeforces.com/contest/268/problem/A

noOfTeams = int(input())

teamsUniformsList = []
noOfGamesThatHostTeamWillPlayInGuestUniform = 0

for i in range(noOfTeams):
    teamsUniformsList.append(input())

for index, value in enumerate(teamsUniformsList):
    for i in range(len(teamsUniformsList)):
        if index != i:
            if int(value.split(' ')[0]) == int(teamsUniformsList[i].split(' ')[1]):
                noOfGamesThatHostTeamWillPlayInGuestUniform += 1

print(noOfGamesThatHostTeamWillPlayInGuestUniform)
