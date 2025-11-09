import re
import ast

#Globale samlinger
karakterer = {"INFO100":"A","INFO200":"B", "ECON110":"B", "ECON220":"A",
              "GEO200":"C", "GEO300":"E"}

emner = ["INFO100","ECON110", "GEO200","INFO200","ECON220","GEO300"]
       
class emne:
    def leggtilemne(nyttemne):
        #update dictionary
        karakterer.update({nyttemne:""})
        for x in karakterer:
            print(x, karakterer[x])

    def emneliste():
        print("Velg fag og/eller emnenivå (<enter> for alle")
        global emner
        global karakterer
        
        fag = input('Fag: ')
        nivå = input('Nivå: ')
        if fag == '' and nivå == '':
          for x in karakterer:
              if x in karakterer:
                  print(x + ' ' + karakterer[x])
                
        #search using nivå
        if fag =='' and nivå != '':
            for x in karakterer: 
                rangenivå = (int(re.search(r'\d+',x).group()))
                nivå = int(nivå)
                if nivå == 100:
                    if rangenivå in range(100,200):
                        if x in karakterer:
                            print(x+' '+karakterer[x])
                elif nivå == 200:
                    if rangenivå in range(200,300):
                        if x in karakterer:
                            print(x+' '+karakterer[x])
                elif nivå == 300:
                    if rangenivå in range(300,400):
                        if x in karakterer:
                            print(x+' '+karakterer[x])

        #search using fag (search INFO, ECON, or GEO)
        if fag !='' and nivå =='':
            for x in emner:
                if fag in x:
                    if x in karakterer:
                        print(x + ' ' + karakterer[x])
                        
        if fag != '' and nivå !='':
            for x in emner:
                rangenivå = (int(re.search(r'\d+',x).group()))
                nivå = int(nivå)
                if fag in x and nivå == 100 and rangenivå in range(100,200):
                    if x in karakterer:
                        print (x + ' ' + karakterer[x])
                elif fag in x and nivå == 200 and rangenivå in range(200,300):
                    if x in karakterer:
                        print (x + ' ' + karakterer[x])
                elif fag in x and nivå == 300 and rangenivå in range(300,400):
                    if x in karakterer:
                        print (x + ' ' + karakterer[x])

class karakterfunc:
    def settkarakterer():     
        emne = (input("Emne: "))
        karakter = (input("Karakter (<enter> for å slette): "))
        karakterer[emne] = karakter      

    def karaktersnitt(karakterer):
        fag=input("Fag:")
        nivå=input("Nivå:")
        antallFag=0
        total=0
       
        if fag=="" and nivå=="":
            for bokstav in karakterer.values():
                if bokstav=="A":
                    antallFag=antallFag+6
                    total=total+1
                elif bokstav=="B":
                    antallFag=antallFag+5
                    total=total+1
                elif bokstav=="C":
                    antallFag=antallFag+4
                    total=total+1
                elif bokstav=="D":
                    antallFag=antallFag+3
                    total=total+1
                elif bokstav=="E":
                    antallFag=antallFag+2
                    total=total+1
                elif bokstav=="F":
                    antallFag=antallFag+1
                    total=total+1
             
                snitt = round(antallFag/total)


            if snitt==6:
                print("Snitt: A")
            elif snitt==5:
                print("Snitt: B")
            elif snitt==4:
                print("Snitt: C")
            elif snitt==3:
                print("Snitt: D")
            elif snitt==2:
                print("Snitt: E")
            elif snitt==1:
                print("Snitt: F")
   
#Menu
def start():
    print("""
    1: Emneliste
    2: Legg til emne
    3: Sett karakter
    4: Karaktersnitt
    5: Avslutt
    6: Lagre
    """) 
    
    velg = int(input('Velg handling (0 for meny)> '))
    if velg == 0:
        return start()
    
    if velg == 1:
        emne.emneliste()

        start() #returns meny
 
    elif velg == 2:
        emne.leggtilemne(input("Nytt emne: "))

        start() 
    
    elif velg == 3:
        karakterfunc.settkarakterer()

        start()
        
    elif velg == 4:
        karakterfunc.karaktersnitt(karakterer)
        
        start()
    
    elif velg == 5:
        from sys import exit

    elif velg == 6:
        lagreprint = input("Vil du lagre endringene? (j/n)")
  
        if lagreprint == 'j':
            lagre = open('lagre.txt', 'w')
            lagre.write('emner=' + str(emner) + '\n')
            lagre.write('karakter=' + str(karakterer) + '\n')
            print('Alt er lagret.')
        else:
            print('Takk for nå')
                   
start()
