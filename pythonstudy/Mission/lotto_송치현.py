import random as r

ltlist = []

for i in range(0, 6):
    while True:
        rand = r.randint(1,45)
        if rand not in ltlist:
            ltlist.append(rand)
            break
            
print(ltlist)