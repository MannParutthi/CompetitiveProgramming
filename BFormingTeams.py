# http://codeforces.com/contest/216/problem/B

noOfStudents, noOfPairOfArchenemies = [int(x) for x in input().split(' ')]

dictOfTeams = {1: [], 2: []}
noOfStudentsToBeSentOnBench = 0
listOfArchenemies = []

for i in range(noOfPairOfArchenemies):
    pairOfArchenemies = [int(x) for x in input().split(' ')]
    listOfArchenemies.append(pairOfArchenemies[0])
    listOfArchenemies.append(pairOfArchenemies[1])
    archenemies1IncludedInATeam = False
    archenemies2IncludedInATeam = False

    for teamX in dictOfTeams.values():
        if pairOfArchenemies[0] in teamX: # and pairOfArchenemies[1] not in teamX:
            archenemies1IncludedInATeam = True
        elif pairOfArchenemies[1] in teamX: # and pairOfArchenemies[0] not in teamX:
            archenemies2IncludedInATeam = True

    # if pairOfArchenemies[0] in dictOfTeams[1] and pairOfArchenemies[0] not in dictOfTeams[2]:
    #
    # elif pairOfArchenemies[1] in dictOfTeams[1] and pairOfArchenemies[1] not in dictOfTeams[2]:
    #
    # elif


    for teamX in dictOfTeams.values():
        print(archenemies1IncludedInATeam, archenemies2IncludedInATeam)
        if archenemies1IncludedInATeam and archenemies2IncludedInATeam:
            break
        else: # len(teamX) != noOfStudents // 2:
            if not archenemies1IncludedInATeam and archenemies2IncludedInATeam:
                if pairOfArchenemies[0] not in teamX and pairOfArchenemies[1] not in teamX:
                    teamX.append(pairOfArchenemies[0])
                    archenemies1IncludedInATeam = True
                    print('1', teamX)
            elif archenemies1IncludedInATeam and not archenemies2IncludedInATeam:
                if pairOfArchenemies[0] not in teamX and pairOfArchenemies[1] not in teamX:
                    teamX.append(pairOfArchenemies[1])
                    archenemies2IncludedInATeam = True
                    print('2', teamX)
            elif not archenemies1IncludedInATeam and not archenemies2IncludedInATeam:
                if pairOfArchenemies[0] not in teamX and pairOfArchenemies[1] not in teamX:
                    teamX.append(pairOfArchenemies[0])
                    archenemies1IncludedInATeam = True
                    print('3', teamX)
    print('final chk', pairOfArchenemies, archenemies1IncludedInATeam, archenemies2IncludedInATeam, dictOfTeams)
    if not archenemies1IncludedInATeam and not archenemies2IncludedInATeam:
        noOfStudentsToBeSentOnBench += 2
    elif archenemies1IncludedInATeam and not archenemies2IncludedInATeam:
        noOfStudentsToBeSentOnBench += 1
    elif not archenemies1IncludedInATeam and archenemies2IncludedInATeam:
        noOfStudentsToBeSentOnBench += 1

# for student in set(listOfArchenemies):
#     if not(student in dictOfTeams[1] or student in dictOfTeams[2]):
#         noOfStudentsToBeSentOnBench += 1

print(dictOfTeams, set(listOfArchenemies), noOfStudentsToBeSentOnBench)
