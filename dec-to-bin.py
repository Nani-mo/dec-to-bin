import colorama
from colorama import Fore, Back, Style
colorama.init()

print('Its a trap')
print("umrechnen von dem Dezimalsystem zu einenm belibigen anderen System")
print("")

def operation():
    basis, decZahl = eingabe()  # Aufrufen von "eingabe" und Erhalt von Rückgabewerten
    ueberrpruefen(basis, decZahl)  # Daten ueberpruefen
    liste = []
    index = 0

    while decZahl >= 1:  # solange ausfuehren bis nix mehr da ist
        i = decZahl / basis  # decZahl durch die "basis" dividiert und wird zu "i"
        rest = decZahl % basis  # der "rest" von (decZahl durch die "basis") kommt in die Variable "rest"
        decZahl = int(i)  # decZahl wird mit dem Wert von "i" ueberschrieben und zu einer Ganzzahl
        index = index + 1  # der "index" wird um 1 erhöht
        liste.insert(-index, str(rest))  # der "rest" wird in die "liste" vorne angefuegt
    return liste  # "liste" als Rückgabewert


def eingabe():
    basis = int(input('Basis -> Zahlensystem (nur Ganzzahlen): '))  # input der Basis
    decZahl = int(input('Dezimalzahl (nur Ganzzahlen): '))  # input der dezimal Zahl
    return (basis, decZahl)


def ueberrpruefen(basis, decZahl):  # wenn basis 1 oder 0 dann Programm beenden
    if basis <= 1 or decZahl < 0:
        print(Fore.RED + "¯\_(ツ)_/¯" + "\033[39m")
        run()


def run():
    while True:
        print(Fore.GREEN + str(" ".join(operation())) + "\033[39m")  # Ausgabe der "liste" wird durch join() der Klammern beraubt (" ". beschreibt das Trennungszeichen)


try:
    run()
except KeyboardInterrupt:
    exit()