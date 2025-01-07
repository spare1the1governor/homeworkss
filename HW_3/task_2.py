import random
friends = ["Анна", "Борис", "Виктор", "Галина", "Дмитрий"]
gifts = ["игрушку", "книгу", "шарф", "носки", "конфеты", "часы", "фотоальбом"]

def choose_gifts():
    global friends
    global gifts
    gif=[]
    for i in range(0,len(friends)):
        e=(random.choice(gifts))
        gif.append(e)
        gifts.remove(e)
        print(f'{friends[i]} получит {gif[-1]}')


choose_gifts()

