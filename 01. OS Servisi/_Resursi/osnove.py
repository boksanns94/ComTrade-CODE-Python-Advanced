#pajton osnove

#nista nije tipski definisano

#prosti tipovi promenljive
naziv = "Advanced Python" #string promenljiva
br_polaznika = 6 # brojevi
kurs_poceo = True #boolean promenljiva True/False

#strukture - slozeni tipovi promenljivih
kursevi = ["Advanced Python","Basic Python","Data Science"] #lista 
koordinate = (40.000, 41.000) #torke/ tuple
namirnice = {"jabuke","banane","paradajz"} #skup

akademija={
    "kursevi":kursevi,
    "max_br_polaznika":20,
    "min_trajanje": 48,
    "max_trajanje": 200,
}  #recnik, kljuc-vrednost

#immutable objects/types> int, float, bool, string, unicode, tuple
#mutable objects/types> list, dict, set


skup1 = set() #definisanje praznog seta/skupa
skup2 = set()

#for-petlja
for i in range(5): #i ide od 0-4
    skup1.add(i)

for i in range(3,9): #i ide od 3-8
    skup2.add(i)

#funkcije nad skupovima
#presek
skup3 = skup1.intersection(skup2)
skup3_1 = skup1 & skup2


#razlika
skup4 = skup1.difference(skup2)
skup4_1 = skup2 - skup1

print(skup4_1)
print(skup4)

#while petlja
brojac = 0
while(True): #beskonacna petlja
    print(brojac)
    brojac+=1 #operator inkrementa
    if brojac>10: #provera uslova
        break #prekidanje petlje
print("Nastavak brojaca, ",brojac)
while(brojac):
    print(brojac)
    if brojac>10: #provera uslova
        brojac=0
else:
    print("Kraj petlje 2") #deo koda koji se izvrsava nakon prirodnog zavrsetka petlje (bez break)


#funkcije
def sabirac(a,b):
    zbir = a+b
    return zbir

rez = sabirac(3,4)
print("Rezultat sabiranja je ", rez)