"""CountSemi.py

Module-level notes: This script contains a simple example for generating and counting semiprimes.
See math/CountSemi.md for detailed mathematical background, asymptotics and algorithms.

Usage:
    python CountSemi.py

This file was augmented to include documentation and a pointer to the math notes.
"""

def CountSemiprimes():
    P=[1,4,16]
    Q=[26,10,20]
    
    Numbers=range(2,30)
    
    def IsPrime(number):
        if number==2:
            return 1
        for i in range(2,number):
           
            if (number % i ==0):
                return 0
        return 1
    Prime_List=[Prime for Prime in Numbers if IsPrime(Prime)]
    print(Prime_List)
    def MakeSemiPrime(Prime_List):
        SemiPrime_List=[]
        for a in Prime_List:
            for i in Prime_List:
                b=a*i
                SemiPrime_List.append(b)
        SemiPrime_List=sorted(set(SemiPrime_List)) 
        return SemiPrime_List
    SemiPrime_List=MakeSemiPrime(Prime_List)
    print(SemiPrime_List)
    
    def GettingScore(Q, P):
        Score=[]
        for i in range(len(Q)):
            start=P[i]
            licznik=0
            finish=Q[i]
            print(i)
            print(start)
            print(finish)
            for o in SemiPrime_List:
                print(o)
                if (o>=start and o<=finish):
                    licznik+=1
                if (o>finish):
                    Score.append(licznik)
                    break
        return Score        
    Score=GettingScore(Q, P)
    print('Score =',Score)
        # write your code in Python 3.6
CountSemiprimes()   
