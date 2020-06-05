# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1051
# Perfect squares have odd number of factors

import math

while True:
    noOfTimesSwitchClicked = 0
    bulbNo = int(input())
    if bulbNo == 0:
        break
    else:
        # for i in range(bulbNo):
        #     if bulbNo % (i+1) == 0:
        #         noOfTimesSwitchClicked += 1
        # if noOfTimesSwitchClicked % 2 == 0:
        #     print('no')
        # else:
        #     print('yes')
        if int(math.sqrt(bulbNo)) ** 2 == bulbNo:
            print('yes')
        else:
            print('no')
