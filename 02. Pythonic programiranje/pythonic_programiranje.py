# Pythonic programiranje



def main():
    # OTPAKIVANJE TUPLI
    list_of_coords = [
        (10, 20, "Novi Sad"),
        (30, 40, "Belgrade"),
        (50, 60, "Subotica")
    ]

    # Los nacin
    for g in list_of_coords:
        Lat = g[0]
        Long = g[1]
        Name = g[2]
        print(f"Grad: {Name}, G.Duz: {Lat}, G.Sir: {Long}.")

    # Ispravan nacin
    for gg in list_of_coords:
        gLat, gLong, gName = gg
        print(f"Grad: {gName}, G.Duz: {gLat}, G.Sir: {gLong}.")

    # LINE BREAKS
    veoma_velika_primanja_odnosno_plata = 100000
    veoma_veliki_rashodi_odnosno_racuni = 50000
    kretenski_porez_drzave_srbije = 20000

    # Pogresno
    neto_novci = veoma_velika_primanja_odnosno_plata - veoma_veliki_rashodi_odnosno_racuni - kretenski_porez_drzave_srbije
    neto_novci_dva = (veoma_velika_primanja_odnosno_plata-
                      veoma_veliki_rashodi_odnosno_racuni-
                      kretenski_porez_drzave_srbije)

    # Ispravno
    neto_novci_plus = (veoma_velika_primanja_odnosno_plata
                       - veoma_veliki_rashodi_odnosno_racuni
                       - kretenski_porez_drzave_srbije)

    # IMPORTOVANJE MODULA
    # Pogresno
    import time, datetime, os, sys

    # Ispravno
    import time
    import datetime
    import os
    import sys
    #from flask import Flask, jsonify, request

    # LIST COMPREHENSION
    # Kreiranje liste bez List Comprehension-a
    lista_gradova = []
    for grad in list_of_coords:
        lista_gradova.append(grad[2])

    # Kreiranje liste sa List Comprehension-om
    lista_gradova_dva = [g[2] for g in list_of_coords]
    lista_gradova_tri = [name for lat,long,name in list_of_coords]
    lista_gradova_cetiri = [name for lat,long,name in list_of_coords if name != "Beograd"]

    # FIRST CLASS FUNCTIONS
    def shout(txt):
        return txt.upper()

    def whisper(txt):
        return txt.lower()

    def a(q):
        if q == "Da":
            return shout
        if q == "Ne":
            return whisper

    def question():
        q = input("Da ili Ne: ")
        print(a(q))

    question()

    #IIFE - Immediately Invoked Function Expression
    # LAMBDA FUNKCIJE - Anonimne funkcije

    print((lambda x,y:x+y)(2,5))
    naziv_l = lambda x,y,z: (x*z)+y
    print(naziv_l(1,2,3))


if __name__ == "__main__":
    main()
