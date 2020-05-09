# http://codeforces.com/contest/231/problem/A

noOfProblems = int(input())

noOfProblemsToImplement = 0

for i in range(noOfProblems):
    friendsViewList = input().split(" ")
    noOfFriendsReadyToSolveProblem = 0
    if friendsViewList.count('1') >= 2:
        noOfProblemsToImplement += 1

print(noOfProblemsToImplement)
