import random

ES = ["5E","8E" ]
AS = ["5A","7A"]
DS = ["5D","7D",]
GS = ["5G","7G",]
BS = ["5B","8B" ]
eS = ["5e","8e" ]

string = 1

solo = []

def notes(inputlist,outputlist):
    random.shuffle(inputlist)
    choice = inputlist[0]
    outputlist.append(choice)
    return outputlist

def number():
    numberofnotes = random.randint(2,5)
    return numberofnotes

def get_next_string(string):
    if string == 0:
        return 0
    elif string == 1:
        return random.choice([0,2])
    elif string == 2:
        return random.choice([1,3])
    elif string == 3:
        return random.choice([2,4])
    elif string == 4:
        return random.choice([3,5])
    elif string == 5:
        return random.choice([4,6])
    elif string == 6:
        return random.choice([5,7])
    elif string == 7:
        return 0

def E():
    for _ in range(number()):
        notes(ES,solo)
def A():
    for _ in range(number()):
        notes(AS,solo)
def D():
    for _ in range(number()):
         notes(DS,solo)
def G():
    for _ in range(number()):
        notes(GS,solo)
def B():
    for _ in range(number()):
        notes(BS,solo)
def e():
    for _ in range(number()):
        notes(eS,solo)


while string != 0 or len(solo) == 1:
    if string == 1:
        E()
    elif string == 2:
        A()
    elif string == 3:
        D()
    elif string == 4:
        G()
    elif string == 5:
        B()
    elif string == 6:
        e()
    string = get_next_string(string)


print(solo)
