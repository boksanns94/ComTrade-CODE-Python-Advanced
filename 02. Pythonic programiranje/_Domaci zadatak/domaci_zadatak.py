import datetime
from itertools import permutations


def main():
    # Zadatak 1_1
    # Kreirati funkciju koja prima jedan argument i vraca funkciju koja mnozi zadati
    # broj sa nepoznatim brojem. Povratna funkcija treba da bude lambda izraz.
    print((lambda a, b: a*b)(int(input("Unesite broj: ")), 4))

    # Zadatak 1_2
    # Sortirati zadatu listu torki koristeci sort funkciju, ciji ce kljuc biti lambda izraz
    lista1 = [('English', 88), ('Matematika', 90), ('Maths', 97), ('Social Matematikas', 82)]
    lista1.sort(reverse=int(input("Unesite 1 za silazno, 0 za uzlazno sortiranje: ")), key=(lambda lista1: lista1[1]))
    print(lista1)

    # Zadatak 1_3
    # Napisati program koji filtrira listu brojeva, koristeci lambda izraz
    # Filtriracu sve deljive sa 3 (za primer)
    lista2 = [3, 11, 14, 27, 9, 35, 1, 19, 12]
    l2 = filter(lambda a: a % 3 == 0, lista2)
    print(*l2)

    # Zadatak 1_4
    # Napisati program koji proverava da li string pocinje zadatim slovom, koristeci lambda izraz
    rec = input("Unesite rec: ")
    slovo = input("Unesite slovo: ")
    odg = ""
    if not (lambda r, s: r[0] == s)(rec.lower(), slovo.lower()):
        odg = "ne "
    print(f"Rec {rec} {odg}pocinje slovom {slovo}.")

    # Zadatak 1_5
    # Napisati program koji iz datuma izvlaci godinu, mesec, dan i vreme, koristeci lambda izraz
    m, h, d, m, g = (lambda x: (x.minute, x.hour, x.day, x.month, x.year))(datetime.datetime.now())
    print(f"Vreme je {h}:{m}, dan je {d}, mesec je {m} a godina je {g}.")

    # Zadatak 1_6
    # Napisati program koji pronalazi presek dve liste, koristeci lambda izraz
    lista3 = [1, 7, 2, 6, 3, 5, 4]
    lista4 = [5, 9, 6, 8, 7]
    res = list(filter(lambda x: x in lista3, lista4))
    print(res)

    # Zadatak 1_7
    # Napisati funkciju koja za zadati broj vraca prvi veci broj premestanjem redosleda cifara.
    # U slucaju da to nije moguce treba da vrati False
    num = input("Unesite broj: ")
    if len(num) == 1:
        print("FALSE")
    else:
        p2 = list(map(lambda x: "".join(x), list(permutations(num))))
        p2.sort()
        if p2[-1] == num:
            print("FALSE")
        else:
            print(p2[p2.index(num)+1])

    # Zadatak 2_1
    # Napisati program koji od zadate liste brojeva kreira listu sa vrednostima pomnozenim sa 3.
    lista5 = [2, 5, 7, 12, 4, 3]
    print(*map(lambda b: b*3, lista5))

    # Zadatak 2_2
    # Kreirati program koji od zadate liste karaktera kreira listu torki, gde svaka torka
    # sadrzi malo i veliko slovo (npr ("U","u")). Novokreirana lista ne treba da sadrzi
    # duplikate u slucaju da oni postoje u originalnoj listi.
    lista6 = ["a", "e", "i", "a", "u", "o", "e"]
    l6 = set(lista6)
    print(*map(lambda c: (c.upper(), c.lower()), l6))

    # Zadatak 2_3
    # Kreirati program koji od zadate liste parova (torki od 2 elementa)
    # kreira listu stringova, gde par sada predstavlja jedan element.
    lista7 = [('Sheridan', 'Gentry'), ('Laila', 'Mckee'), ('Ahsan', 'Rivas'), ('Conna', 'Gonzalez')]
    print(list(map(lambda tup: " ".join(tup), lista7)))

    # Zadatak 2_4
    # Kreirati program koji konvertuje recnik listi u listu recnika.
    dict1 = {'Matematika': [88, 89, 62, 95], 'Engleski': [77, 78, 84, 80]}
    l8 = [dict(zip(dict1, el)) for el in zip(*dict1.values())]
    print(l8)

    # Mrzi me jako da radim OS zadatke xDDD

    # Zadatak 3_1
    # Kreirati program koji za zadatu putanju vraca listu foldera i vraca listu fajlova.
    # Liste kreirati koriscenjem list comprehension funkcionalnost.

    # Zadatak 3_2
    # Napisati program koji dozvoljava korisniku da sa standardnog ulaza kreira tekstualni fajl
    # i putem standardnog ulaza unosi tekst dok ne unese komandu za prekid unosa. Nakon toga
    # korisnik kreira folder putem standardnog ulaza. Prethodno kreirani tekstualni fajl prebaciti u folder.


if __name__ == "__main__":
    main()
