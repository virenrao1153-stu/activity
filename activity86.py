def pallind(r):
    e = len(r)-1
    s = 0
    while(s<e):
        if(r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True

r = (1, 2, 3, 4, 9, 1)
if (pallind(r)):
    print("The Tuple is Flip-Flop")
else:
    print("The Tuple is not Flip-Flop")