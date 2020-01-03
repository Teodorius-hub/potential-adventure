''' Theodor Norsten 2019-01-20. kurskod: DD100N
 Nedanstående kod är en kort presentation om mig.
 Först defineras de variabler och konstanter som återfinns i texten.
 Print funktionen används sedan för att skriva ut texten innehållandes definerade variabler och konstanter'''

tid= 25
dubbel_tid= tid*2
storlek= 43.5
PERIOD=365
NAMN= 'Theodor'
EFTERNAMN= 'Norsten'
dagar= tid*PERIOD
dubbel_dagar= dubbel_tid*PERIOD
yta= 21.5
dubbel_yta= yta*2
stad= 'Stockholm'

print(' Hej! jag heter ' + NAMN , EFTERNAMN , ' och jag är',tid,'år gammal.',end='')
print(' Jag bor i',stad, 'i en lägenhet på',yta,'kvadratmeter.')
print(' Om min lägenhet vore dubbelt så stor skulle den vara ' + str(dubbel_yta) + ' kvadratmeter.')
print('Jag har skostorlek',storlek,end='')
print(' Min nuvarande ålder, ' + str(tid) + ' år, motsvarar en ålder i antalet dagar på '+ str(dagar) +'.')
print(' Om',tid,'år, kommer jag vara',dubbel_tid,'år,vilket kommer motsvara en ålder i antal dagar på',dubbel_dagar,'.')




