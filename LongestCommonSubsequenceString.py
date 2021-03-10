# https://www.youtube.com/watch?v=sSno9rV8Rhg

def LCS(X, Y):
    m = len(X) 
    n = len(Y)
    L = [[None]*(n + 1) for i in range(m + 1)]
    
    for i in range(m + 1): 
        for j in range(n + 1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    print('Length of LCS:',L[m][n])
    
    i = m
    j = n
    lcsStr = ''
    while i > 0 and j > 0:
      if X[i-1] == Y[j-1]:
        lcsStr += X[i-1]
        i-=1
        j-=1
      elif L[i-1][j] > L[i][j-1]:
        i-=1
      else:
        j-=1
    print('LCS String:', lcsStr[::-1])
        
LCS('SHINCHAN', 'NOHARAAA')
