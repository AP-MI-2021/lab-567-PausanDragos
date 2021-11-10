from Functions.functions import add, remove, modify, printList, \
    get_higher_class, apply_discount, determine_max, order_by_price, get_sums_for_names, undo, redo


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
    print("8. Redo.")
    print("P. Afisarea listei curente de rezervari")
    print("X. Exit")


def predefinedList():
        return [[1, "Vasilescu Andrei", "Economy", 5000, "DA"],
                [2, "Georgescu Sebastian", "Business", 10000, "NU"],
                [3, "Vasilescu Andrei", "EconomyPlus", 6000, "DA"]]


def start():
    undolst = []
    redolst = []
    currentlist = predefinedList()
    while True:
        printMenu()
        n = input("Alegeti optiunea: ")
        if n == "1":
            print_op1()
            n = input("Alegeti optiunea: ")
            if n == "1":
                add(currentlist, undolst, redolst)
            elif n == "2":
                currentlist = remove(currentlist, undolst, redolst)
            elif n == "3":
                modify(currentlist, undolst, redolst)
        if n == "2":
            name = input("Dati numele persoanei ale carei rezervari doriti sa le urcati la o clasa superioara:")
            get_higher_class(currentlist, name, undolst, redolst)
        if n == "3":
            procentaj = float(input("Dati procentajul cu care doriti sa se ieftineasca rezervarile cu checkin"))
            apply_discount(currentlist, procentaj, undolst, redolst)
        if n == "4":
            econ = determine_max(currentlist)[0]
            econ_plus = determine_max(currentlist)[1]
            bus = determine_max(currentlist)[2]
            print("Pretul maxim pentru clasa economy este:", econ)
            print("Pretul maxim pentru clasa economy plus este:", econ_plus)
            print("Pretul maxim pentru clasa business este:", bus)
            print("Daca pretul este egal cu -1 inseamna ca pentru clasa respectiva nu exista inregistrari")
        if n == "5":
            currentlist = order_by_price(currentlist, undolst, redolst)
        if n == "6":
            nameLst = get_sums_for_names(currentlist)[0]
            priceLst = get_sums_for_names(currentlist)[1]
            for i in range(len(nameLst)):
                print(nameLst[i], "are suma preturilor", priceLst[i])
        if n == "7":
            currentlist = undo(currentlist, undolst, redolst)
        if n == "8":
            currentlist = redo(currentlist, undolst, redolst)
        if n.lower() == "p":
            printList(currentlist)
        if n.lower() == "x":
            return
