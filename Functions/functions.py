from Domain.domain import getID, getNume, getPret, getClasa,getCheckin, setNume, setClasa, setPret, setCheckin


def copyTheList(lst):
    """
    Copiaza lista
    :param lst:lista curenta
    :type lst: lista de liste
    :return: aceeasi lista, dar diferita in memorie
    :rtype: lista de liste
    """
    newLst = []
    for elem in lst:
        if isinstance(elem, list):
          value = copyTheList(elem)
          newLst.append(value)
        else:
            newLst.append(elem)
    return newLst


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



def add(lst, undolst, redolst):
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
                clasa = "EconomyPlus"
            elif clasa == "3":
                clasa = "Business"
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
    addDO(lst, ID, nume, clasa, pret, checkin, undolst, redolst)


def addDO(lst, ID, nume, clasa, pret, checkin, undolst, redolst):
    """
    Adaugam un dictionar in lista
    :param lst: list
    :param ID: int
    :param nume: str
    :param clasa: str
    :param pret: float
    :param checkin: str
    """
    redolst = []
    undolst.append(copyTheList(lst))
    rezervare = [ID, nume, clasa, pret, checkin]
    lst.append(rezervare)


def remove(lst, undolst, redolst):
    """
    Citim ID-ul inregistrarii pe care dorim sa o eliminam
    :param lst: list
    :return:
    """
    n = int(input("Alegeti ID-ul inregistrarii pe care doriti sa fie stearsa: "))
    return removeDO(lst, n, undolst, redolst)


def removeDO(lst, n, undolst, redolst):
    """
    Eliminam un dictionar din lista
    :param lst: list
    :param n: int
    :return: Lista rezultata in urma eliminarii
    """
    redolst = []
    undolst.append(copyTheList(lst))
    newLst = [rezervare for rezervare in lst if rezervare[0] != n]
    return newLst


def modify(lst, undolst, redolst):
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
    modifyDO(lst, ID, nume, clasa, pret, checkin, undolst, redolst)


def modifyDO(lst, ID, nume, clasa, pret, checkin, undolst, redolst):
    """
    Modificam un dictionar din lista
    :param lst: list
    :param ID: int
    :param nume: str
    :param clasa: str
    :param pret: float
    :param checkin: str
    """
    redolst = []
    undolst.append(copyTheList(lst))
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
    print("2. EconomyPlus")
    print("3. Business")


def printMenuCheckin():
    print("Selectati optiunea dorita pentru checkin")
    print("1. Doresc Checkin")
    print("2. Nu doresc Checkin")


def get_higher_class(lst, name, undolst, redolst):
    """
    Se trec toate rezervarile facute pe un nume la o clasa superioara
    :param lst: list
    :param name: str
    :param undolst: list
    :param redolst: list
    """
    redolst = []
    undolst.append(copyTheList(lst))
    for i in range(len(lst)):
        if getNume(lst[i]) == name:
            if getClasa(lst[i]) == "Economy":
                setClasa(lst[i], "EconomyPlus")
            elif getClasa(lst[i]) == "EconomyPlus":
                setClasa(lst[i], "Business")


def apply_discount(lst, procentaj, undolst, redolst):
    """
    Se aplica discount tuturor rezervarilor care au facut checkin-ul
    :param lst: list
    :param procentaj: float
    :param undolst: list
    :param redolst: list
    """
    redolst = []
    undolst.append(copyTheList(lst))
    for i in range(len(lst)):
        if getCheckin(lst[i]) == "DA":
            new_price = (100 - procentaj) / 100 * getPret(lst[i])
            new_price = round(new_price, 2)
            setPret(lst[i], new_price)


def determine_max(lst):
    """
    Se determina pretul maxim al fiecarei clase
    :param lst: list
    :return: Valorile maxime gasite pentru fiecare clasa
    """
    max_econ = -1
    max_econ_plus = -1
    max_bus = -1
    for i in range(len(lst)):
        if getClasa(lst[i]) == "Economy":
            max_econ = max(getPret(lst[i]), max_econ)
        elif getClasa(lst[i]) == "EconomyPlus":
            max_econ_plus = max(getPret(lst[i]), max_econ_plus)
        elif getClasa(lst[i]) == "Business":
            max_bus = max(getPret(lst[i]), max_bus)
    return max_econ, max_econ_plus, max_bus


def order_by_price(lst, undolst, redolst):
    """
    Se ordoneaza lista crescator dupa pretul rezervarilor
    :param lst: list
    :param undolst: list
    :param redolst: list
    :return: Lista formata in urma ordonarii
    """
    redolst = []
    undolst.append(copyTheList(lst))
    lst.sort(key=getPret)
    return lst


def get_sums_for_names(lst):
    """
    Se efectueaza suma preturilor tuturor inregistrarilor facute pentru fiecare nume
    :param lst: list
    :return: O lista cu numele fiecarei persoane care a facut cel putin o rezervare si o lista cu pretul inregistrarilor
            facute de fiecare persoana
    """
    j = 0
    nameLst = []
    priceLst = []
    for i in range(len(lst)):
        if getNume(lst[i]) not in nameLst:
            nameLst.append(getNume(lst[i]))
            priceLst.append(0)
    while j < len(nameLst):
        for i in range(len(lst)):
            if nameLst[j] == getNume(lst[i]):
                priceLst[j] += getPret(lst[i])
        j += 1
    return nameLst, priceLst


def undo(lst, undolst, redolst):
    """
    Undo la lista curenta
    :param lst: list
    :param undolst: list
    :param redolst: list
    :return: Lista rezultata dupa efectuarea undo-ului
    """
    if len(undolst) > 0:
        redolst.append(copyTheList(lst))
        lst = undolst[len(undolst) - 1]
        undolst.pop(len(undolst) - 1)
        print("Undo-ul s-a realizat")
    else:
        print("Nicio modificare facuta")
    return lst


def redo(lst, undolst, redolst):
    """
    Redo la lista curenta
    :param lst: list
    :param undolst: list
    :param redolst: list
    :return: Lista rezultata dupa efectuarea redo-ului
    """
    if len(redolst) > 0:
        undolst.append(copyTheList(lst))
        lst = redolst[len(redolst) - 1]
        redolst.pop(len(redolst) - 1)
        print("Redo-ul s-a realizat")
    else:
        print("Nu se poate efectua redo")
    return lst


