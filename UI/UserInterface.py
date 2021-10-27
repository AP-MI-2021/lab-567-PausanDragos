from Functions.functions import add, remove, modify, getID, getNume, getPret, getClasa, getCheckin, printList


def print_op1():
    print("1. Adaugare")
    print("2. Stergere")
    print("3. Modificare")


def printMenu():
    print("1. Adaugare/ Stergere/ Modificare.")
    print("2. Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară.")
    print("3. Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit.")
    print("4. Determinarea prețului maxim pentru fiecare clasă.")
    print("5. Ordonarea rezervărilor descrescător după preț.")
    print("6. Afișarea sumelor prețurilor pentru fiecare nume.")
    print("7. Undo.")
    print("P. Afisarea listei curente de rezervari")
    print("X. Exit")


def predifinedList():
        return [[1, "Vasilescu Andrei", "Economy", 5000, "DA"]]


def start():
    currentlist = predifinedList()
    while True:
        printMenu()
        n = input("Alegeti optiunea: ")
        if n == "1":
            print_op1()
            n = input("Alegeti optiunea: ")
            if n == "1":
                add(currentlist)
            elif n == "2":
                currentlist = remove(currentlist)
            elif n == "3":
                modify(currentlist)
        if n.lower() == "p":
            printList(currentlist)
        if n.lower() == "x":
            return