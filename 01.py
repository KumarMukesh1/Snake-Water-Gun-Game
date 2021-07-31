import random

def gamewin(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'g':
            return True
        elif you == 'w':
            return False
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True
print("comp turn:  snake(s) water(w) gun(g)")
randno = random.randint(1,3)
if randno == 1:
    comp = 's'
elif randno == 2:
    comp = 'w'
elif randno == 3:
    comp = 'g'
you = input("your turn: snake(s) water(w) gun(g)\nEnter your choice")
a = gamewin(comp,you)
print(f"computer choose {comp}")
print(f"you choose {you}")
if a == None:
    print("tie")
elif a==True:
    print("you win")
else:
    print("you loose")
    


    