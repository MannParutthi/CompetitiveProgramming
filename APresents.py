# http://codeforces.com/contest/136/problem/A

noOfFriends = int(input())
giftGivenToFriendIByFriendNo = [int(x) for x in input().split(' ')]

dictOfGiftsToByFrom = {}

for index, val in enumerate(giftGivenToFriendIByFriendNo):
    dictOfGiftsToByFrom[val] = index + 1

print(' '.join([str(val) for key, val in sorted(dictOfGiftsToByFrom.items())]))
