# https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=288

imageNoCount = 0

while True:
    try:
        imageNoCount += 1
        warEagles = 0
        matrix = []
        squareMatrixSize = int(input())
        for i in range(squareMatrixSize):
            matrix.append([int(x) for x in list(input())])
        print(matrix)





        print('Image Number', imageNoCount, 'contains', warEagles, 'war eagles.')
    except:
        break
