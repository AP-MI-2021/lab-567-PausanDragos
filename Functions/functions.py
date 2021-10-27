from Domain.domain import getID, getNume, getPret, getClasa,getCheckin, setNume, setClasa, setPret, setCheckin


def printList(lst):
    """
    Printam lista
    :param lst: list
    """
    if (len(lst) == 0):
        print("Lista este goala.")
        return
    for i in range(len(lst)):
        print(f"{getID(lst[i])}. Numele este: {getNume(lst[i])}. Clasa este: {getClasa(lst[i])}. Pretul este: {getPret(lst[i])}. Checkin: {getCheckin(lst[i])}.")



def add(lst):
    """
    Citim un dictionar
    :param lst: list
    """
    ID = int(input("Dati ID-ul utlizatorului: "))
    nume = input("Dati numele: ")
    while True:
        printMenuClasa()
        clasa = input()
        if clasa == "1" or clasa == "2" or clasa == "3":
            if clasa == "1":
                clasa = "Economy"
            elif clasa == "2":
                clasa = "Economy plus"
            elif clasa == "3":
                clasa = "Bussines"
            break
    pret = float(input("Pretul biletului este: "))
    while True:
        printMenuCheckin()
        checkin = input()
        if checkin == "1" or checkin == "2":
            if checkin == "1":
                checkin = "DA"
            elif checkin == "2":
                checkin = "NU"
            break
    addDO(lst, ID, nume, clasa, pret, checkin)


def addDO(lst, ID, nume, clasa, pret, checkin):
    """
    Adaugam un dictionar in lista
    :param lst: list
    :param ID: int
    :param nume: str
    :param clasa: str
    :param pret: float
    :param checkin: str
    """
    rezervare = [ID, nume, clasa, pret, checkin]
    lst.append(rezervare)


def remove(lst):
    """
    Citim ID-ul inregistrarii pe care dorim sa o eliminam
    :param lst: list
    :return:
    """
    n = int(input("Alegeti ID-ul inregistrarii pe care doriti sa fie stearsa: "))
    return removeDO(lst, n)


def removeDO(lst, n):
    """
    Eliminam un dictionar din lista
    :param lst: list
    :param n: int
    :return: Lista rezultata in urma eliminarii
    """
    newLst = [rezervare for rezervare in lst if rezervare[0] != n]
    return newLst


def modify(lst):
    """
    Citim modificarile dorite unui dictionar din lista
    :param lst: list
    :return: Lst, daca nu se efectueaza modificari asupra ei
    """

    printList(lst)
    try:
        ID = int(input("Alegeti ID-ul inregistrarii pe care doriti sa o modificati(lasati liber daca nu vreti actualizare): "))
    except:
        ID = ""
    if ID != "":
        try:
            nume = input("Dati noul nume(lasati liber daca nu vreti actualizare): ")
        except:
            nume = ""
        try:
            clasa = input("Dati noua clasa(lasati liber daca nu vreti actualizare): ")
        except:
            clasa = ""
        try:
            pret = float(input("Dati pretul nou(lasati liber daca nu vreti actualizare): "))
        except:
            pret = ""
        try:
            checkin = input("Dati noua situatie a checkin-ului(lasati liber daca nu vreti actualizare): ")
        except:
            checkin = ""
    else:
        return lst
    modifyDO(lst, ID, nume, clasa, pret, checkin)


def modifyDO(lst, ID, nume, clasa, pret, checkin):
    """
    Modificam un dictionar din lista
    :param lst: list
    :param ID: int
    :param nume: str
    :param clasa: str
    :param pret: float
    :param checkin: str
    """
    for i in range(len(lst)):
        if lst[i][0] == ID:
            poz = i
    if nume != "":
        setNume(lst[int(poz)], nume)
    if clasa != "":
        setClasa(lst[int(poz)], clasa)
    if pret != "":
        setPret(lst[int(poz)], pret)
    if checkin != "":
        setCheckin(lst[int(poz)], checkin)

def printMenuClasa():
    print("Selectati optiunea pentru clasa")
    print("1. Economy")
    print("2. Economy plus")
    print("3. Bussines")


def printMenuCheckin():
    print("Selectati optiunea dorita pentru checkin")
    print("1. Doresc Checkin")
    print("2. Nu doresc Checkin")


def test_add():
    test_list = []
    addDO(test_list, 1, "Popescu Ioan", "Economy", 500.3, "NU")
    assert len(test_list) == 1
    assert getID(test_list[0]) == 1
    assert getNume(test_list[0]) == "Popescu Ioan"
    assert getClasa(test_list[0]) == "Economy"


def test_remove():
    test_list = []
    addDO(test_list, 1, "Popesecu Ioan", "Economy", 500.3, "NU")
    addDO(test_list, 2, "Ionescu Adi", "Economy plus", 550.3, "DA")
    test_list = removeDO(test_list, 1)
    assert len(test_list) == 1
    assert getID(test_list[0]) == 2
    assert getNume(test_list[0]) == "Ionescu Adi"


def test_modify():
    test_list = []
    addDO(test_list, 1, "Popesecu Ioan", "Economy", 500.3, "NU")
    addDO(test_list, 2, "Ionescu Adi", "Economy plus", 550.3, "DA")
    modifyDO(test_list, 2, "Ionescu Adrian", "Bussines", 550.3, "DA")
    assert len(test_list) == 2
    assert getNume(test_list[1]) == "Ionescu Adrian"
    assert getClasa(test_list[1]) == "Bussines"

def test_functions():
    test_remove()
    test_add()
    test_modify()
