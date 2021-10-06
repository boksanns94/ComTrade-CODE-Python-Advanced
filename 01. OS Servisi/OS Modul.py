#OS modul

# Importuje se klasicno
import os

# Trenutni radni direktorijum - current working directory - CWD
cwd = os.getcwd()
print(cwd)

def trenutni_folder():
    print("Prethodni radni folder")
    print(os.getcwd())
    print()

trenutni_folder()
os.chdir("./test_folder")  # Menjanje u child folder (ako postoji)
trenutni_folder()
os.chdir("../")  # Menjanje u roditeljski folder
trenutni_folder()
# . - tacka predstavlja trenutni folder
# .. - dve tacke predstavljaju roditeljski folder

parent_dir = os.getcwd()
child_dir = os.path.join(parent_dir, "test_folder")
for i in range(2, 10):
    os.mkdir(os.path.join(child_dir, f"folder {i}"))
# Python po defaultu direktorijumima dodeljuje 777 level pristupa

# Ako imamo folder "./Comtrade/Predavanja", i zelimo da kreiramo sledecu strukturu:
# "./Comtrade/Predavanja/APD/Cas 1......12
# Fali nam folder APD i python ce se buniti, nece hteti da kreira "Cas 1" jer "APD" ne postoji
# Komanda os.makedirs kreira sve neophodne nadfoldere kako bi napravio trazeni folder.
for i in range(2, 10):
    os.makedirs(os.path.join(os.path.join(child_dir, "APD"), f"Cas {i}"))

# Izlistavanje foldera
lista_dir = os.listdir(os.getcwd())
print(lista_dir)

# Brisanje krajnjeg direktorijuma
try:
    os.rmdir(os.path.join(os.getcwd(), "test_folder"))
except:
    print("Folder nije prazan.")

# kreiranje, otvaranje, zatvaranje i brisanje fajla
try:
    er = 0
    fajl = "testfajl.txt"
    er = 1
    f = open(fajl, "w")
    er = 2
    f.close()
    er = 3
    os.remove(os.path.join(os.getcwd(), fajl))
except:
    print(f"Problem pri citanju fajla {fajl}. er={er}")