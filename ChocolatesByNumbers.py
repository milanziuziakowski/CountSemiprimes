"""ChocolatesByNumbers.py

Module-level notes: Classic problem — number of chocolates eaten equals N / gcd(N, M).
See math/ChocolatesByNumbers.md for the formal proof and explanation.

Usage:
    from ChocolatesByNumbers import solution
    print(solution(10, 4))  # example
"""

def solution(N, M):
    List_of_N=[]
    if N>0:
        for i in range(0,N):
            List_of_N.append(i)
    #print(List_of_N)
    List_of_Ate=[]
    var=0
    while(1):
        List_of_Ate.append(var)
        var=(var+M)%N
        #print(var)
        if var in List_of_Ate:
            break
    #print(List_of_Ate)
    return len(List_of_Ate)
