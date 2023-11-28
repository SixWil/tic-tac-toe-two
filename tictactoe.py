# bord = tom för tio rutor.
bräde = [' ' for x in range(10)]

# vilken ruta = vilken bokstav
def skriv_bokstav(letter,pos):
    bräde[pos] = letter

# Om ruta = ej tagen ge tom ruta
def fri_platts(pos):
    return bräde[pos] == ' '

# Skapa spelbrädet
def printbräde(bräde):
    print('   |   |   ')
    print(' ' + bräde[1] + ' | ' + bräde[2] + ' | ' + bräde[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + bräde[4] + ' | ' + bräde[5] + ' | ' + bräde[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + bräde[7] + ' | ' + bräde[8] + ' | ' + bräde[9])
    print('   |   |   ')

# är brädet fullt?
def isbrädeFull(bräde):
    if bräde.count(' ') > 1:
        return False
    else:
        return True

# vem vann?
def vinnare(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

# spelar val
def spelare_tur():
    run = True
    while run:
        move = input("välj en position för dit X mellan 1 och 9\n")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if fri_platts(move):
                    run = False
                    skriv_bokstav('X' , move)
                else:
                    print('redan tagen')
            else:
                print('skriv ett nummer mellan 1 och 9')

        except:
            print('skriv ett NUMMER')

# dator val
def dator_tur():
    possibleMoves = [x for x , letter in enumerate(bräde) if letter == ' ' and x != 0  ]
    move = 0

    for let in ['O' , 'X']:
        for i in possibleMoves:
            brädecopy = bräde[:]
            brädecopy[i] = let
            if vinnare(brädecopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1 , 3 , 7 , 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = välj_Random(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = välj_Random(edgesOpen)
        return move

# randomizer
def välj_Random(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

# huvud funktion
def main():
    print("välkommen!")
    printbräde(bräde)

    while not(isbrädeFull(bräde)):
        if not(vinnare(bräde , 'O')):
            spelare_tur()
            printbräde(bräde)
        else:
            print("Du förlorar!")
            break

        if not(vinnare(bräde , 'X')):
            move = dator_tur()
            if move == 0:
                print(" ")
            else:
                skriv_bokstav('O' , move)
                print('datorn placerade sitt o på' , move , ':')
                printbräde(bräde)
        else:
            print("Du vann!")
            break




    if isbrädeFull(bräde):
        print("Oavgjort")

# start och stop
while True:
    x = input("Vill du starta? y för ja, n för nej (y/n)\n")
    if x.lower() == 'y':
        bräde = [' ' for x in range(10)]
        print('--------------------')
        main()
    else:
        break
