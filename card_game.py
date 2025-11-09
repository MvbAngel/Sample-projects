import random
import codecs

#Cards/decks
deck = {'A':[],
        'B':[],
        'C':[],
        'D':[],
        'E':[],
        'F':[],
        'G':[],
        'H':[]}

def everything():
    global deck
    cards = ['\u2660''A', '\u2660''7', '\u2660''8', '\u2660''9',
             '\u2660''10', '\u2660''J', '\u2660''Q','\u2660''K',
             '\u2666''A', '\u2666''7', '\u2666''8', '\u2666''9',
             '\u2666''10', '\u2666''J', '\u2666''Q', '\u2666''K',
             '\u2663''A', '\u2663''7', '\u2663''8', '\u2663''9',
             '\u2663''10', '\u2663''J', '\u2663''Q', '\u2663''K',
             '\u2665''A', '\u2665''7', '\u2665''8', '\u2665''9',
             '\u2665''10', '\u2665''J', '\u2665''Q', '\u2665''K']
    random.shuffle(cards)

    deck1 = cards[0:4]
    deck2 = cards[4:8]
    deck3 = cards[8:12]
    deck4 = cards[12:16]
    deck5 = cards[16:20]
    deck6 = cards[20:24]
    deck7 = cards[24:28]
    deck8 = cards[28:32]

    deck = {'A':deck1,
            'B':deck2,
            'C':deck3,
            'D':deck4,
            'E':deck5,
            'F':deck6,
            'G':deck7,
            'H':deck8}
    
#The gard game        
def carddeck():
    global deck 
    for keys in deck.keys():
        print(keys[0], end='  ',)
    print("\n")
    for value in deck.values():
        if len(value) != 0:
            print(value[0], end=' ')
        else:
            print('!', end='  ')
    print("\n")
    for number in deck.values():
        print(len(number),end='  ')
    print("\n")
    #Prints out the decks and corresponding cards.

def Choose(bokstav1, bokstav2):
    global deck
    x = 'x'
    
    if bokstav1 == bokstav2:
        print("Ugylding trekk: Velg to kort med samme verdi")
        return True     
     
    if bokstav1 == '' and bokstav1 == '':
        print('Velg to kort!')
        #If enter, will continue game.

    if bokstav1 == x:
        key = input("spillet er avbrut, (Enter) tilbake til meny")
        return start()
        #Stops game temp. and allows you to save. 

    card1 = deck[bokstav1][0]
    number1 = card1[1:]
    card2 = deck[bokstav2][0]
    number2 = card2[1:]
    
    if number1 == number2:
        for x in deck.keys():
            if bokstav1 == x:
                del deck[x][0]
            else:
                continue
            
        for x in deck.keys():
            if bokstav2 ==x:
                del deck[x][0]
            else:
                continue
    else:
        print('velg to kort med samme verdi')

    return True

def winorlose():
    global deck
    x = []

    for value in deck.values():
        if len(value) != 0:
            y = value[0][1:]
            x.append(y)
            
    if len(x) == 0:
        print('Gratulerer du vant!')
        key = input("Enter")
        start()

    if len(x) != 0:
        if len(x) == len(set(x)):
            print('Beklager du tapte :(')
            key = input("Enter")
            start()  

def Game():
    winorlose()
    carddeck()
    print('Trekk to kort (x: avbryt)')
    bokstav1 = input('Velg bunke: ')
    bokstav2 = input('Velg bunke: ')
    if not Choose(bokstav1, bokstav2):
        return
    Game()

def save():
    global deck
    
    lagrespill = input("Vil du lagre spillet? (j/n)")
    if lagrespill == 'j':
        file = open('wishsolitaire.txt', 'w', encoding = "utf-8")
        for bunke in deck.values():
            for card in bunke:
                file.write(card + ' ')
            file.write('\n')
        print('Alt er lagret.')
    else:
        print('Takk for nå')

def returngame():
    global deck
    y = 0
    bokstaver = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    file = open ('wishsolitaire.txt', 'r', encoding = "utf-8")
    linjer = file.read().split('\n')
    for linje in linjer:
        x = linje.split(' ')
        for kort in x:
            if len(kort) > 1:
                deck[bokstaver[y]].append(kort)
        y += 1
               
def start():
    print("""
    \u2660\u2666Wish Solitaire\u2663\u2665
    1: Start nytt spill
    2: Lagre spillet
    3: Hent lagret spill
    4: Avslutt
    """)
    
    velg = int(input('Velg handling(0 for meny):'))
    if velg == 0:
        return start()
    
    if velg == 1:
        everything()
        Game()
    
    if velg == 2:
        save()
        
    if velg == 3:
        returngame()
        Game()
            
    if velg == 4:
        print("Takk for nå")
        from sys import exit
start()
