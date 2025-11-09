from math import pi

saldo = 500
rentesats = 0.01
endringer = []


def valg():
    print("""
    1: Vis saldo
    2: Innskudd
    3: Uttak
    4: renteoppjor
    5: siste endringer
    """)

    velg = int(input('Velg handling: '))
    if velg == 1:
        return saldo
    elif velg == 2:
        return innskudd()
    elif velg == 3:
        return uttak()
    elif velg == 4:
        return renteoppgjor()
    elif velg == 5:
        print(endringer[-3:-2])
        print(endringer[-2:-1])
        print(endringer[-1:])


def renteoppgjor():
    global saldo
    global rentesats
    if saldo >= 1000000:
        rentesats = 0.02
        print('Gratulerer, du får bonusrente!')
    else:
        rentesats = 0.01
        print('Du har nå ordinær rente.')
    saldo = (rentesats +1)*saldo
    return saldo

def innskudd():
    global saldo
    global endringer
    ditt_innskudd = int(input('innskudd:'))
    saldo = saldo + ditt_innskudd
    endringer.append("+" + (str(ditt_innskudd)))
    return saldo

def uttak():
    global saldo
    global endringer
    ditt_uttak = int(input('uttak:'))
    saldo = saldo - ditt_uttak
    endringer.append("-"+(str(ditt_uttak)))
    if saldo < 0:
        print('overtrekk')
    else:
        return saldo

