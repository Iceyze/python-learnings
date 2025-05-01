import math
import random
import create



def start():
   p1 = 100
   p2 = 100
   while p1 != 0 and p2 != 0:
    p1Wager = int(input("wager:"))
    p2Wager = int(input("wager:"))

    a = 1 #int(input())
    b = 6 #int(input())
    p1Score = create.create(a, b)
    p2Score = create.create(a, b)

    if p1Score > p2Score:
        p1 += p2Wager
        p2 -= p2Wager
    else:
        p2 += p1Wager
        p1 -= p1Wager
    print(p1)
    print(p2)
    if p1 == 0:
       print("p2 WINS!!!!")
    elif p2 == 0:
       print("p1 WINS!!!!")
start()