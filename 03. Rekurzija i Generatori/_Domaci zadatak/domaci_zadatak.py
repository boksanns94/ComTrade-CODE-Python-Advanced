# Zadatak 1_1
# Napisati program koji rekurzivno cita sumu svih elemenata neke liste. Lista moze
# imati integere ili liste drugih integera.
import os


def zadatak11(lista1):
    if len(lista1) == 1:
        if isinstance(lista1[0], list):
            return zadatak11(lista1[0])
        return lista1[0]
    else:
        if isinstance(lista1[0], list):
            return zadatak11(lista1[0]) + zadatak11(lista1[1:])
        else:
            return lista1[0] + zadatak11(lista1[1:])


# Zadatak 1_2
# Napisati program koji ce rekurzivno proci kroz stablo direktorijuma i datoteka
# i obrisati fajl sa prosledjenim nazivom ako on u stablu postoji.
# ... ne znam kako rekurzivno da idem kroz stablo ako nemam pre toga sve elemente svakog foldera u celom stablu ...
# ... a i dobijem ospice cim vidim nesto u OS modulu haha ...


# Zadatak 1_3
# Napisati program koji ce rekurzivno proci kroz listu i naci najveci broj u listi
def zadatak13(lista3):
    if len(lista3) == 1:
        return lista3[0]
    if lista3[0] > zadatak13(lista3[1:]):
        return lista3[0]
    else:
        return zadatak13(lista3[1:])


# Zadatak 2_1
# Napisati generator funkciju koja prihvata broj i vraca sledeci broj koje je deljiv sa prosledjenim brojem.
def zadatak21(br):
    yield br*2


# Zadatak 2_2
# Napisati funkciju koja proverava da li je prosledjeni broj prost, a zatim
# generator funkciju koja vraca naredni prost broj od zadatog broja.
def prost(br):
    flag = True
    for i in range(2, br//2):
        if br % i == 0:
            flag = False
    return flag

def zadatak22(br):
    for i in range(br+1, br*2):
        if prost(i):
            yield i


# Zadatak 2_3
# Napisati program putem kojeg korisnik moze da se krece kroz stablo direktorijuma i prilikom
# svakog pomeraja dobija listu svih fajlova i direktorijuma unutar ternutnog direktorijuma.
# Unosom naziva fajla na standardnom izlazu mu se prikazuje sadrzaj fajla, gde se svaka naredna
# linija prikazuje pritiskom na odredjeni taster (npr N za next) ili se prekida pregledanje fajla
# pritiskom na odredjeni taster (npr E za exit), nakon cega se ponovo izlistava trenutni sadrzaj
# direktorijuma. Izlistavanje sadrzaja datoteke treba definisati generator funkcijom.
# ... krecu ospice opet cim vidim OS modul ...
# ... skip ...


def main():
    # Pokretanje zadatka 1_1
    test = [1, 2, [3, 4], [5, 6]]
    rez = zadatak11(test)
    print(rez)
    # Pokretanje zadatka 1_2
    # prc, malo sutra
    # Pokretanje zadatka 1_3
    lista3 = [1, 2, 7, 3, 4, 9, 5, 6]
    maks = zadatak13(lista3)
    print(maks)

    # Pokretanje zadataka 2_1
    z21 = zadatak21(int(input("Unesite broj: ")))
    print(z21.__next__())
    # Pokretanje zadataka 2_2
    z22 = zadatak22(int(input("Unesite potencijalno prost broj: ")))
    print(z22.__next__())
    # Pokretanje zadatka 2_3
    # ponovo prc, kek


if __name__ == "__main__":
    main()
