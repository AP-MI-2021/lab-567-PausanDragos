from Functions.functions import addDO, removeDO, modifyDO, get_higher_class, apply_discount, printList
from UI.UserInterface import printMenu, predefinedList


def printHelp():
    print("Toate comenzile vor fi precedate de ';'")
    print("Pentru adaugari vom folosi urmatorul model: 'add (ID) (nume) (clasa) (pret) (checkin)'")
    print("Pentru stergeri vom folosi urmatorul model: 'remove (ID)'")
    print("Pentru modificari vom folosi urmatorul model: 'modify (ID) (nume) (clasa) (pret) (checkin)'")
    print("Pentru upgrade la clasa vom folosi urmatorul model: 'upgrade (nume)'")
    print("Pentru a aplica reducere celor cu checkin-ul facut vom folosi urmatorul model:'discount (procent reducere)'")
    print("Pentru a afisa lista curenta vom folosi comanda 'print'")
    print("Pentru a iesi din program vom folosi comanda 'exit'")


def start_1():
    currentlist = predefinedList()
    printMenu()
    while True:
        n = input("Dati comanda")
        commandList = n.split(';')
        for i in range(len(commandList)):
            option = commandList[i].split()
            if option[0] == "add":
                option[1] = int(option[1])
                option[4] = float(option[4])
                addDO(currentlist, option[1], option[2], option[3], option[4], option[5])
            elif option[0] == "remove":
                option[1] = int(option[1])
                currentlist = removeDO(currentlist, option[1])
            elif option[0] == "modify":
                option[1] = int(option[1])
                option[4] = float(option[4])
                currentlist = modifyDO(currentlist, option[1], option[2], option[3], option[4], option[5])
            elif option[0] == "upgrade":
                get_higher_class(currentlist, option[1])
            elif option[0] == "discount":
                option[1] = float(option[1])
                apply_discount(currentlist, option[1])
            elif option[0] == "print":
                printList(currentlist)
            elif option[0] == "exit":
                return
            elif option[0] == "help":
                printHelp()
            else:
                print("Nu ati introdus o comanda valabila")
