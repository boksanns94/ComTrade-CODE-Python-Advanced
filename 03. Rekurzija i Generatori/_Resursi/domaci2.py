import os
#lambda1
def mnozenje_sa_zadatim_br(n):
    return lambda x : x * n

#lambda2

def sotiraj_listu_torki(lista,kljuc_index=1):
    #lista_predmeta = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
    return lista.sort(key = lambda x: x[kljuc_index]) #sortiraj po broju, ne po predmetu

#lambda4
def pocinje_sa(slovo):
    return lambda x:True if x.startswith(slovo) else False

#lambda5
import datetime
def datum_u_delove(datum):

    year = lambda x: x.year
    month = lambda x: x.month
    day = lambda x: x.day
    t = lambda x: x.time()
    print(year(datum))
    print(month(datum))
    print(day(datum))
    print(t(datum))

#lambda6
def presek(lista1, lista2):
    return list(filter(lambda x: x in lista1, lista2)) 

#lambda7
def sledeci_veci(n):
    nums = list(str(n))
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False

#map1
def triple(lista_br):
    return map(lambda x: 3*x, lista_br)

#map2
def char_to_tuple(lista_karaktera):
    
    def mala_velika_slova(slovo):
        return str(slovo).upper(), str(slovo).lower()
    
    lista = map(mala_velika_slova, lista_karaktera)
    return set(lista) #vrati samo unikatne vrednosti ako se karakteri ponavljaju

#map3
def torke_u_listu(lista):
    return list(map(' '.join, lista))

#map4

def dict_to_list(recnik):
    result = map(dict, zip(*[[(k,v) for v in value] for k,value in recnik.items()]))
    return list(result)

#os1
def folder_info(putanja_foldera):
    fajlovi = [naziv for naziv in os.listdir(putanja_foldera) if os.path.isfile(os.path.join(putanja_foldera,naziv))]
    folderi = [naziv for naziv in os.listdir(putanja_foldera) if os.path.isdir(os.path.join(putanja_foldera,naziv))]
    return fajlovi,folderi

def folder_info_for(putanja):
    fajlovi = []
    folderi = []
    for el in os.listdir(putanja):
        if os.path.isfile(os.path.join(putanja,el)):
            fajlovi.append(el)
        else:
            folderi.append(el)
#os2
def unos_teksta():
    naziv_fajla = input("Unesite naziv fajla: ")
    fajl_putanja = f'{naziv_fajla}.txt'
    print("Unesite zeljeni tekst.")
    print("Za prekid unosa unesite !quit  .")
    with open(fajl_putanja,mode="a") as fajl:
        unos = input()
        while unos!="!quit":
            fajl.write(unos+"\n")
            unos = input()
    return fajl_putanja

def main():
    # recnik = {'Matematika': [88, 89, 62, 95], 'Engleski': [77, 78, 84, 80]}
    # dict_to_list(recnik)

    # files, folders = folder_info(os.path.join(os.getcwd(),"test"))
    # print("Fajlovi> ",files)
    # print("Folderi> ",folders)

    fajl = unos_teksta()
    folder = input("Kreirajte folder unosenjem njegov naziva: ")
    os.mkdir(folder)
    folder_putanja = os.path.join(os.getcwd(), folder)
    os.rename(fajl, os.path.join(folder_putanja, fajl))


    #lambda 3
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Originalna lista brojeva:")
    print(nums)
    print("\nParni brojevi:")
    even_nums = list(filter(lambda x: x%2 == 0, nums))
    print(even_nums)
    print("\nNeparni brojevi:")
    odd_nums = list(filter(lambda x: x%2 != 0, nums))
    print(odd_nums)


    

if __name__=="__main__":
    main()