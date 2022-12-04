import random
lose=0
win=0
score=0
played=0
while True:
    choice=input("Do you want to play(Y/N):")
    if choice=='Y':
        played+=1
        n=int(input("Enter a number:"))
        r=random.randint(1,6)
        print("You got:",r)
        if n==r:
            print("YOU WIN")
            score=score+r
            win+=1
        else:
            print("YOU LOSE")
            lose+=1
    else:
        break
print("GAMES PLAYED:",played) 
print("SCORE:",score)
print("LOSE:",lose)
print("WIN:",win)
