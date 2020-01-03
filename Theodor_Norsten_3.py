'''Theodor Norsten kurskod: DD100N 2019-02-03
Först initieras tomma listor,hashtabell samt konstanter överst i programmet.
mha for-slingor och funktionen .append()läggs användarens val av namn och
längd på hopp till i de fördefinierade tomma listorna.En hashtabell skapas sedan mha dessa
listor med namn som nycklar och längder som värden. Mha while,for-slinga samt if satser får användaren ett menyval
med utskrift av information för varje menyval.'''



minhashtabell={}
värden=[]
nycklar=[]
ANTAL_ELEVER=3
ANTAL_HOPP_ELEV=3

print('välkommen till programmet som håller räkningen på längdhoppen per elev')
print('Följande program utgår från 3 elever med 3 hopp vardera')
print('börja med att skriva in namnet på eleverna och längden på deras hopp') 

for i in range(ANTAL_ELEVER):
    namn=input('Namn på elev')
    hopp=[]
    nycklar.append(namn)
    for j in range(ANTAL_HOPP_ELEV):
        längd= float(input('skriv längden på hopp nr ' + str(j+1)))
        hopp.append(längd)
    värden.append(hopp)



for i in range(len(nycklar)):
    minhashtabell[nycklar[i]]=värden[i]


while True:
    print('1.visa alla resultat.')
    print('2.visa längsta hopp för varje elev.')
    print('3.visa hur långt det sista hoppet var för varje elev.')
    print('4. Avsluta programet.')

    val= int(input('välj en siffra mellan 1-4 av ovanstående menyval. '))

    if val==1:
        for i in minhashtabell.keys():
            print(i,'hoppade',minhashtabell[i],'meter.')
            
    elif val==2:
        for i in minhashtabell.keys():
            print(i,'hoppade som längst',max(minhashtabell[i]),'meter.')

    elif val==3:
        for i in minhashtabell.keys():
            print(i,'hoppade',minhashtabell[i] [-1], 'meter på sista hoppet.')
            
    elif val==4:
        break
    
    else:
        print('felaktigt menyval,försök igen!')

print('välkommen åter.')
        
                
            



    





















    
     


