#Python osnove

#Tipovi osnovnih promenljivih
ime = "milos"  # String
godine = 27  # Integer
tezina = 98,5  # Float
Musko = True  # Bool
Ima_dece = None  # NoneType

#Tipovi slozenih promenljivih
Lista = [1, 2, 3]
Torka = (1, 2)
Skup = {1, 2, 3, 4}
Recnik = {  # U formatu - kljuc:vrednost
    1: "Prvi"
    2: "Drugi"
    3: "Treci"
}

#Funkcija range
range(3)  # od 0 do 2
range(3,7)  # od 3 do 6
range(4,16,2)  # od 4 do 15 sa korakom 2

#Funkcije nad skupovima
s1 = {1, 2, 3, 4}  # Skup 1
s2 = {3, 4, 5, 6, 7}  # Skup 2
s1.union(s2)  # Unija
s1.intersection(s2)  # Presek
s1.difference(s2)  # Razlika

#While petlja
brojac = 0
while(True):
    brojac += 1
    print(brojac)
    if(brojac > 10):
        break
else:  # Moze imate else, on se izvrsava na kraju prirodnog zavrsetka while (tj. ako se ne desi break)
    print("Kraj")

#For petlja
for i in range(10):
    print(i)

#Funkcije
def sabirac(a,b):  # Implementacija (pravljenje funkcije)
    zbir = a + b
    return zbir

sabirac(3,7)  # Pozivanje (koriscenje funkcije)

