#pythonic programiranje

import os
from time import process_time

#-----------------------------------
    #First Class functions, Higher-Order functions
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def text_line(func):
    line = func("Da li me cujes?")
    print(line)

def upitno_vikanje(odgovor):
    if odgovor=="Da":
        return shout
    else:
        return whisper

def zbir(a):
    return a+a

def samoglasnici(promenljiva):
    slova = ['a','e','i','o','u']
    if promenljiva in slova:
        return True
    else:
        return False


def main():
    brojevi = (1,2,3,4)
    # rezultat = []
    # for broj in brojevi:
    #     rezultat.append(zbir(broj))

    rezultat = map(zbir,brojevi)
    print(*rezultat) # print(*iterable) stampanje vrednosti iterabilne strukture u jednoj liniji sa razmakon izmedju svakog elementa
    
    niz_slova = ['a','b','c','f','i','i','p']

    filtrirano =filter(samoglasnici,niz_slova)
    print("Samoglasnici u nizu slova ")
    print(*filtrirano)

    #IIFE - Immediately Invoked Function Expression 
    (lambda x,y:x+y)(2,3) #anonimna funkcija

    naziv_l = lambda x,y:x+y
    def naziv(x,y): return x+y 
    print(naziv(2,3))
    print(naziv_l(5,6))

def main1():
    #test za funkcije First Class i Higher-Order

    # text_line(shout)
    # text_line(whisper)
    # odgovor = input("Da li da vicem ili ne? ")
    # linija = upitno_vikanje(odgovor)
    # print(linija("Tekst"))
    # print(type(linija))

    #tuple/torke
    lista_gradova = [(44.8125, 20.4612, "Beograd"),
    (45.2889, 19.7245, "Novi sad"),
    (43.7238, 20.6873, "Kraljevo")]

    #pogresno
    brojac = 0
    for grad in lista_gradova:
        brojac+=1
        g_duz = grad[0]
        g_sir= grad[1]
        g_ime = grad[2]

        print("Geografska duzina grada "+g_ime+" je "+str(g_duz)+", a sirina je "+str(g_sir))
    #pogresno 2
    for i in range(len(lista_gradova)):
        g_duz = lista_gradova[i][0]
        g_sir= lista_gradova[i][1]
        g_ime = lista_gradova[i][2]

    #ispravno
    for grad in lista_gradova:
        g_duz,g_sir,g_ime = grad
        print(f"Geografska duzina grada {g_ime} je {g_duz}, a sirina je {g_sir}")

    #---------------------------------
    #line breaks
    ukupno_dnevnice = 100
    porez = 50
    takse = 20
    studentski_kredit = 10
    privatni_casovi = 20

    #ispravno
    primanja = (ukupno_dnevnice
    -porez
    -takse
    -studentski_kredit
    +privatni_casovi)

    #pogresno
    primanja = (ukupno_dnevnice-
    porez-
    takse-
    studentski_kredit+
    privatni_casovi)
    #---------------------------------

    #importovanje modula
    
    #pogresno
    import time, datetime, os, sys

    #ispravno
    import time
    from datetime import datetime
    import os
    import sys

    # from flask import Flask, jsonify, request

    #---------------------------------
    prom_a = 10
    prom_b = 15
    prom_c = 5
    prom_d = 6
    zbir = prom_a + prom_b
    rezultat = prom_a*prom_c + prom_b*prom_d


    #-----------------------------------
    #list comprehension
    
    lista_naziva_gradova = []
    for g_duz,g_sir,g_ime in lista_gradova:
        lista_naziva_gradova.append(g_ime)
    print("Lista gradova")
    print(lista_naziva_gradova)

    lista_naziva_gradova_2 = [g_ime for g_duz,g_sir,g_ime in lista_gradova if g_ime.startswith("K")]
    print(lista_naziva_gradova_2)

    parni = [i for i in range(0,101,2)]
    print(parni)


if __name__=="__main__":
    main()