''' Theodor Norsten 2019-01-23: DD100N
Nedanstående programkod gör det möjligt för användaren att omvandla beräkningsmåtten:
Grader till Fahrenheit, meter till amerikanska mil och liter till gallon. Först intitieras konstanterna.
Därefter används en oändlig while slinga där menyn presenteras för användaren mah print funktionen.
Mah input funktionen får användaren välja konvertering som mah if, elif och else
satser omvandlar vald konvertering till rätt beräkningsmått.
Break funktionen används i while slingan och gör det möjligt för användaren att avsluta programet.'''


'''initering av variabler'''
OMVANDLING_FAHRENHEIT=32
GRADER_FAHRENHEIT_ =1.8
LÄNGD_METER=1609.3
LITER_GALLON= 1/3.785

print('Välkommen till konverteraren!')

      

while True:
    print('välj någon utav nedanstående konverteringar')
    print('1: Grader Celcius till grader Fahrenheit')
    print('2: Meter till amerikanska mil')
    print('3: Liter till galLon')
    print('4: Avsluta')

    Konvertering= int(input('Vilken konvertering väljer du? Ange siffra: 1, 2 ,3 eller 4'))

    if Konvertering == 1:
        grader= float(input('Ange grader i celcius'))                            
        Fahrenheit= grader*GRADER_FAHRENHEIT_ + OMVANDLING_FAHRENHEIT
        print(grader,'grader Celius motsvarar',str(Fahrenheit),'grader Fahrenheit','.')
    elif Konvertering == 2:
        längd= float(input('Ange längd i meter'))
        amerikanska_mil= längd * LÄNGD_METER
        print(längd,'meter motsvarar',str(amerikanska_mil),'amerikanska mil.')
    elif Konvertering == 3:
        liter= float(input('ange volym i liter'))
        gallon= liter* LITER_GALLON
        print(liter,'liter motsvarar',str(gallon),'gallon.')
    elif Konvertering == 4:
        break
    else:
        print('felaktigt menyval!,försök igen')
        

print('välkommen åter!')

        
        






    
    
    



