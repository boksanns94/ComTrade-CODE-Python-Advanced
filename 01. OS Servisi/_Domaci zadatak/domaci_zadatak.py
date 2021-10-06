import os


# Zadatak 1:
# Kreirati funkciju koja će na zadatoj putanji roditeljskog direktorijuma
# kreirati foldere definisane putem standardnog ulaza.
# Obezbediti da funkcija proverava validnost putanje

def zadatak_1(parent):
    if os.path.exists(parent):
        child = input("Unesite ime novog foldera: ")
        os.mkdir(os.path.join(parent, child))


# Zadatak 2:
# Kreirati funkciju koja u direktorijume na zadatim
# putanjama kreira 5 praznih datoteka proizvoljnog tipa.

def zadatak_2(parents):
    for p in parents:
        if os.path.exists(p):
            for i in range(5):
                os.mkdir(os.path.join(p, f"test{i}"))


# Zadatak 3:
# Kreirati funkciju koja briše direktorijum. U slučaju
# da direktorijum nije prazan potrebno je da obriše ceo njegov sadržaj.

def zadatak_3(dir):
    if os.path.exists(dir):  # Ako putanja postoji
        dir_list = os.listdir(dir)  # Izlistaj njen sadrzaj
        for el in dir_list:  # Za svaki element koji je sadrzan u direktorijumu
            el_p = os.path.join(dir, el)
            if os.path.isdir(el_p):  # Ako je element direktorijum
                zadatak_3(el_p)  # Ponovi korake od gore
            else:  # Ako nije direktorijum
                os.remove(el_p)  # Obrisi fajl


def main():
    # Zadatak 1
    p = os.getcwd()
    zadatak_1(p)
    # Zadatak 2
    parents = [os.getcwd() for i in range(3)]
    zadatak_2(parents)
    # Zadatak 3
    d = os.getcwd()
    zadatak_3(d)

if __name__ == "__main__":
    main()