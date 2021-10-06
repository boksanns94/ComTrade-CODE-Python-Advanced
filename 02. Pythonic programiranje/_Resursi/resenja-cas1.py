import os, shutil

def kreirajFoldere(roditeljski_dir, lista_dir):
    if not os.path.exists(roditeljski_dir):
        print( "Putanja ne postoji")
        return
    
    for dir in lista_dir:
        os.mkdir(os.path.join(roditeljski_dir,dir))
    print( "Uspesno kreirani direktorijumi")

def kreirajDatoteke(roditelj,lista_putanja):
    if len(lista_putanja)==0:
        print("Nisu prosledjeni direktorijumi")
        return
    
    for dir in lista_putanja:
        os.chdir(os.path.join(roditelj,dir)) #bitno je promeniti direktorijum u prvom for-u
        for i in range(5):
            f = open(f"{i+1}.txt", mode="w") #postaviti mode na pisanje - w
            f.close()
        # os.chdir("../") ovo je solucija II ako ne prosledjujemo roditelja u funkciji
    print("Uspesno kreirane datoteke")


def obrisiDirektorijum(dir):
    if not os.path.exists(dir):
        print("Direktorijum ne postoji")
        return
    if not os.path.isdir(dir):
        print("Putanja nije direktorijum")
        return
    
    for el in os.listdir(dir):
        if os.path.isfile(el):
            os.remove(el)
        elif os.path.isdir(el):
            for el_d in os.listdir(el):
                os.remove(el_d)
            os.rmdir(el)
        else:
            print("Doslo je greske nije fajl ni direktorijum")


def main():
    #test 1 - kreiranje sa invalidnom putanjom
    # kreirajFoldere("cas 2", ["1","2"])

    #test 2 - kreiranje sa validnom putanjom
    # os.mkdir("roditelj")
    # kreirajFoldere("roditelj", ["1","2"])

    #test 3 - kreiranje direktorijuma zadatih preko std-ulaza
    # direktorijumi = []
    # dir = input("Unesite naziv direktorijuma. Za prekid unesite X. ")
    # while dir!="X":
    #     direktorijumi.append(dir)
    #     dir = input("Unesite naziv direktorijuma. Za prekid unesite X. ")
    # print("Lista unetih dir",direktorijumi)
    
    #test 4 - kreiranje fajlova unutar liste direktorijuma
    # kreirajFoldere("roditelj", direktorijumi)
    # os.chdir(os.path.join(os.getcwd(),"roditelj"))
    # kreirajDatoteke(os.getcwd(),["1","2","prvi"])
    # kreirajDatoteke(os.path.join(os.getcwd(),"roditelj"),["1","2","prvi"]) # druga opcija za slanje roditeljskog direktorijuma

    #test 5 - provera sadrzavaja direktorijuma
    # os.chdir(os.path.join(os.getcwd(),"roditelj"))
    # print(os.listdir(os.getcwd()))

    #test 6 - brisanje dir pomocu kreirane funkcije
    # obrisiDirektorijum(os.getcwd())

    #test 7 - brisanje direktorijuma pomocu shutil modula
    # shutil.rmtree(os.path.join(os.getcwd(),"roditelj"))

    #sudo i python
    os.system("python komande.py")



    
if __name__=="__main__":
    main()