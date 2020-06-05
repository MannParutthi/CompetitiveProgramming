# https://codeforces.com/contest/490/problem/A

noOfChildrens = int(input())
childrensSpecialization = [int(x) for x in input().split(' ')]

noOfTeams = 0
listOfTeams = []
dictOfSpecialization = {1: [], 2: [], 3: []}

for index, val in enumerate(childrensSpecialization):
    dictOfSpecialization[val].append(index+1)

noOfTeams = min([len(x) for x in dictOfSpecialization.values()])

for i in range(noOfTeams):
    listOfTeams.append(' '.join([str(x) for x in [dictOfSpecialization[1][i], dictOfSpecialization[2][i], dictOfSpecialization[3][i]]]))

print(noOfTeams)
print('\n'.join(listOfTeams))
