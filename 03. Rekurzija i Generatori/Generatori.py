# Generatori

# gen-funkcije
def simple_generator_function():
    yield 1
    yield 2
    yield 3

def fib(max):
    fib = [0, 1]
    f = n = 1
    while n <= max:
        fib.append(n)
        n = n + f
        f = n - f
    print(fib)

def fib_gen(max):
    f, n = 0, 1
    while f < max:
        yield f
        f, n = n, n+f

# generator citanje fajlova
def csv_reader(ime_fajla):
    fajl = open(ime_fajla, "r")
    rez = fajl.read().split("\n")
    return rez

def csv_reader_gen(ime_fajla):
    for red in open(ime_fajla,"r"):
        yield red

def main():
    """
    for val in simple_generator_function():
        print(val)
    x = simple_generator_function()
    print(x.__next__())
    print(x.__next__())
    print(next(x))

    el = 34
    fib(el) # Obicna FIB funkcija
    fib_g = fib_gen(el) # Kreiranje fib generator objekta
    for i in range(el): # Iteriranje kroz generator objekat da bi dobili vrednost fibonacija
        print("Fib-gen: ", next(fib_g))
    """

    # generator citanje fajlova
    csv = csv_reader("MOCK_DATA.csv")
    br_red = 0
    for red in csv:
        br_red += 1
    print(f"Broj redova je {br_red}.")

    csv_gen = csv_reader_gen("MOCK_DATA.csv")
    br_red_gen = 0
    for red in csv_gen:
        br_red_gen += 1
    print(f"Broj redova sa generatorom je {br_red_gen}.")

    # Moduli, paketi
    # 1. default parametri (a, b, c=10) -> (3,4)
    # 2. pozicioni parametri (a, b, c) -> (c=1,a=2,b=3)
    # 3. Arbitrary positional parametri *args (*a) -> (5,2,7,3,6,4)
    # 4. Arbitrary keyword parametri **kwargs (**a) -> (ime="asd", prezime="asdf")
    # 5. Kombinacija 3 i 4:
    # def func(*args, **kwargs) -> ("Ulica", 12, 220, ime = "asd", prezime = "asdfg")


if __name__ == "__main__":
    main()
