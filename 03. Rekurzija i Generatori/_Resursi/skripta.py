#rekurzija
import os

def faktorijel(n):
    
    if n==1:
        return 1
    else:
        return (n*faktorijel(n-1))

def rek_brisanje_sve(putanja, roditelj = None):
    if os.path.isfile(putanja):
        os.remove(putanja)
        if roditelj!=None:
            rek_brisanje_sve(roditelj)
        return 
    elif os.path.isdir(putanja):
        deca = os.listdir(putanja)
        if not deca:
            os.rmdir(putanja)
            return 
        else:
            for dat in deca:
                dat_putanja = os.path.join(putanja,dat)
                rek_brisanje_sve(dat_putanja, putanja)

def rek_brisanje(putanja):
    if not os.listdir(putanja):
        os.rmdir(putanja)
        return
    else:
        for dat in os.listdir(putanja):
            fajl_putanja = os.path.join(putanja,dat)
            if os.path.isfile(fajl_putanja):
                os.remove(fajl_putanja)
            else:
                rek_brisanje(fajl_putanja)
    print(putanja)
    rek_brisanje(putanja)


#generators
#gen-funkcije/objekti

def simpleGenFn():
    yield 1
    yield 2
    yield 3

def fibonacci(max_br): #13
    fib_niz =[0,1]
    first_num = 1
    sledeci = 1
    while sledeci<=max_br:
        fib_niz.append(sledeci)
        n1 = sledeci #pom promenljiva da zapamtimo trenutnu vrednost sabiraca
        n2 = sledeci+first_num #pom za rezultat sabiranja
        first_num=n1 #novi pocetni broj
        sledeci = n2 #novi naredni broj

    return fib_niz

def fib_gen(max_br):
    prvi,drugi = 0,1
    while prvi<max_br:
        yield prvi
        prvi,drugi=drugi,prvi+drugi

#csv reader
def csv_reader(naziv_fajl):
    fajl = open(naziv_fajl)
    rezultat = fajl.read().split("\n")
    return rezultat


def csv_reader_gen(naziv_fajl):
    for red in open(naziv_fajl,"r"):
        yield red

#5 tipova parametara funkcije
def saberi(a,b,c=10):
    return a+b*c


def korisnik(ime, prezime, adresa=None):
    if adresa:
        print(f'Korisnik: {ime} {prezime} sa adresom {adresa}')
    else:
        print(f'Korisnik: {ime} {prezime} nema adresu')

#*args
def sabiranje(*brojevi):
    rez = 0
    for br in brojevi:
        rez+=br
    return rez

#**kwargs

def funkcija(**kwargs):
    for i in kwargs.items():
        print(i)

def komb_kwargs_args(*args, **kwargs):
    print(f"Argumenti funkcije su: {args}")
    for i in kwargs.items():
        print(i)

#globalne promenljive

ime = "tamara"

def main():

    #funkcije
    rez = saberi(1,2,3)
    print(rez)
    
    #default parametri
    rez = saberi(1,2)
    print(rez)

    #positional/keyword  parametri
    rez = saberi(13,c=5,b=3)
    print(rez)

    korisnik("Tamara","Naumovic","Savska 36")
    korisnik( "Tamara","Naumovic",adresa ="Savska 36")
    korisnik("Petar", "Peric")

    #arbitraty positional arg  (*args)
    zbir = sabiranje(2,3,1,4,5,6,7,8,10,12)
    print(zbir)

    #arbitraty keyword arg  (**kwargs)
    funkcija(broj=5,ime="Tamara", prezime = "Naumovic")

    #kombinacija *args i **kwargs
    komb_kwargs_args("Sarajevska",150,4,21,ime="Tamara", prezime = "Naumovic")
    #---------------------------------

    #scope promenljivih doseg

    #lokalne za sve prog jezike > for, if, while, {}, funkcije
    #lokalno za Python je funkcija
    #enclosed je funkcija unutar funkcije
    #built-in
    from math import pi
    print(pi)


    #---------------------------------
    # print(faktorijel(4))
    # rek_brisanje(os.path.join(os.getcwd(),"test"))
    # rek_brisanje_sve(os.path.join(os.getcwd(),"textfajl.txt"))
    
    #izvrsavanje gen funkcije
    # for val in simpleGenFn():
    #     print(val)

    #kreiranje gen objekta
    # x = simpleGenFn()
    # print(x.__next__())
    # print(x.__next__())
    # print(next(x))

    #fib-klasican
    # fnk = fibonacci(33)
    # print("Fib klasican > ",fnk)

    # fng = fib_gen(33)
    # for i in range(9):
    #     print("Fib generator > ",next(fng))

    #generator citanje fajlova
    # csv_gen = csv_reader("mdata.txt")
    # br_redova = 0

    # for red in csv_gen:
    #     br_redova+=1
    
    # csv_gen = csv_reader_gen("mdata.txt")

    # gen_exp = (red for red in open("mdata.txt"))

    # print(f"BrGen izraz {next(gen_exp)}")


    #paketima, modulima
    




if __name__=="__main__":
    main()

