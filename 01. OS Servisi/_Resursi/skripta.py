#os modul
import os

#current working directory cwd
cwd = os.getcwd()
print("Trenutni direktorijum ", cwd)

def trenutni_folder():
    print("Prethodni radni folder")
    print(os.getcwd())
    print()

#
# os.chdir('../') #menjanje direktorijuma u roditeljski folder
# os.chdir('./test_folder') #menjanje direktorijuma u child folder ako on postoji

# roditelj_dir = os.getcwd()
# print(roditelj_dir)

# dete_dir=""
# for i in range(2,13):
#     # dete_dir = os.path.join(roditelj_dir,"cas "+str(i))
#     dete_dir = os.path.join(roditelj_dir,f"cas {i}") #path je string   
#     os.mkdir(dete_dir) #kreiranje direktorijuma

# print(dete_dir)
# dete = roditelj_dir+f"\cas {i}"
# print(dete)
# APD/Cas 1 .... 12
# roditelj_dir = os.path.join(os.getcwd(),"APD")

# print(roditelj_dir)
# for i in range(1,13):
#     # dete_dir = os.path.join(roditelj_dir,"cas "+str(i))
#     dete_dir = os.path.join(roditelj_dir,f"cas {i}") #path je string   
#     os.makedirs(dete_dir) #kreira zadati direktorijum i sve prethodne nedostajuce dir u putanji


#izlistavanje foldera/direktorijuma
lista_dir = os.listdir(os.getcwd()) #proslediti putanju za koju zelimo da proverimo listu dir i datoteka
print(lista_dir)

#brisanje direktorijuma
# os.remove(os.path.join(os.getcwd(),"testfajl.py")) #brisanje fajlova
# os.rmdir(os.path.join(os.getcwd(),"test_folder")) #brisanje dir


# try:
#     fajl = "testfajl.txt"
#     f = open(fajl, 'w')
#     f.close()
#     # os.close(f) zatvaranje fajla preko os modula
# except:
#     print("Problem pri citanju fajla "+fajl)


# os.rename("testfajl.txt","new.txt") #preimenovanje fajlova

os.chdir("./APD")
print(os.getcwd())
os.rmdir(os.path.join(os.getcwd(),"cas 1"))
