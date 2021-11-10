from Domain.domain import getID, getNume, getClasa, getPret
from Functions.functions import addDO, removeDO, modifyDO, get_higher_class, apply_discount, determine_max, \
    order_by_price, get_sums_for_names, undo, redo


def test_add():
    test_list = []
    addDO(test_list, 1, "Popescu Ioan", "Economy", 500.3, "NU", [], [])
    assert len(test_list) == 1
    assert getID(test_list[0]) == 1
    assert getNume(test_list[0]) == "Popescu Ioan"
    assert getClasa(test_list[0]) == "Economy"


def test_remove():
    test_list = []
    addDO(test_list, 1, "Popesecu Ioan", "Economy", 500.3, "NU", [], [])
    addDO(test_list, 2, "Ionescu Adi", "Economy plus", 550.3, "DA", [], [])
    test_list = removeDO(test_list, 1, [], [])
    assert len(test_list) == 1
    assert getID(test_list[0]) == 2
    assert getNume(test_list[0]) == "Ionescu Adi"


def test_modify():
    test_list = []
    addDO(test_list, 1, "Popesecu Ioan", "Economy", 500.3, "NU", [], [])
    addDO(test_list, 2, "Ionescu Adi", "EconomyPlus", 550.3, "DA", [], [])
    modifyDO(test_list, 2, "Ionescu Adrian", "Business", 550.3, "DA", [], [])
    assert len(test_list) == 2
    assert getNume(test_list[1]) == "Ionescu Adrian"
    assert getClasa(test_list[1]) == "Business"


def test_upgrade():
    test_list = []
    addDO(test_list, 1, "Popesecu Ioan", "Economy", 500.3, "NU", [], [])
    addDO(test_list, 2, "Ionescu Adi", "EconomyPlus", 550.3, "DA", [], [])
    addDO(test_list, 3, "Ionescu Adi", "Business", 6000, "DA", [], [])
    get_higher_class(test_list, "Ionescu Adi", [], [])
    assert getClasa(test_list[0]) == "Economy"
    assert getClasa(test_list[1]) == "Business"
    assert getClasa(test_list[2]) == "Business"
    get_higher_class(test_list, "Popesecu Ioan", [], [])
    assert getClasa(test_list[0]) == "EconomyPlus"


def test_discount():
    test_list = []
    addDO(test_list, 1, "Popesecu Ioan", "Economy", 500.3, "NU", [], [])
    addDO(test_list, 2, "Ionescu Adi", "EconomyPlus", 550.3, "DA", [], [])
    addDO(test_list, 3, "Ionescu Adi", "Business", 6000, "DA", [], [])
    apply_discount(test_list, 25, [], [])
    assert getPret(test_list[1]) == 412.72
    assert getPret(test_list[2]) == 4500.0
    assert getPret(test_list[0]) == 500.3


def test_get_max():
    test_list = []
    addDO(test_list, 1, "Popesecu Ioan", "Economy", 500.3, "NU", [], [])
    addDO(test_list, 2, "Ionescu Adi", "EconomyPlus", 550.3, "DA", [], [])
    addDO(test_list, 3, "Ionescu Adi", "Business", 6000, "DA", [], [])
    addDO(test_list, 4, "Popesecu Ioan", "Economy", 40.3, "NU", [], [])
    addDO(test_list, 5, "Ionescu Adi", "EconomyPlus", 1550.3, "DA", [], [])
    addDO(test_list, 6, "Ionescu Adi", "Business", 5990, "DA", [], [])
    assert determine_max(test_list) == [500.3, 1550.3, 6000]


def test_order():
    test_list = []
    addDO(test_list, 1, "Popesecu Ioan", "Economy", 500.3, "NU", [], [])
    addDO(test_list, 2, "Ionescu Adi", "EconomyPlus", 550.3, "DA", [], [])
    addDO(test_list, 3, "Ionescu Adi", "Business", 6000, "DA", [], [])
    addDO(test_list, 4, "Popesecu Ioan", "Economy", 40.3, "NU", [], [])
    addDO(test_list, 5, "Ionescu Adi", "EconomyPlus", 1550.3, "DA", [], [])
    addDO(test_list, 6, "Ionescu Adi", "Business", 5990, "DA", [], [])
    test_list = order_by_price(test_list, [], [])
    assert getID(test_list[0]) == 4
    assert getID(test_list[1]) == 1
    assert getID(test_list[2]) == 2
    assert getID(test_list[3]) == 5
    assert getID(test_list[4]) == 6
    assert getID(test_list[5]) == 3

def test_sums_for_names():
    test_list = []
    addDO(test_list, 1, "Popesecu Ioan", "Economy", 500.3, "NU", [], [])
    addDO(test_list, 2, "Ionescu Adi", "EconomyPlus", 550.3, "DA", [], [])
    addDO(test_list, 3, "Ionescu Adi", "Business", 6000, "DA", [], [])
    addDO(test_list, 4, "Popesecu Ioan", "Economy", 40.3, "NU", [], [])
    addDO(test_list, 5, "Ionescu Adi", "EconomyPlus", 1550.3, "DA", [], [])
    addDO(test_list, 6, "Ionescu Adi", "Business", 5990, "DA", [], [])
    lst1 = get_sums_for_names(test_list)[0]
    lst2 = get_sums_for_names(test_list)[1]
    assert lst1 == ["Popesecu Ioan", "Ionescu Adi"]
    assert lst2 == [540.6, 14090.6]


def test_undo():
    test_list = []
    undo_list = []
    addDO(test_list, 1, "Popesecu Ioan", "Economy", 500.3, "NU", undo_list, [])
    test_list = undo(test_list, undo_list, [])
    assert test_list == []
    addDO(test_list, 1, "Popesecu Ioan", "Economy", 500.3, "NU", undo_list, [])
    addDO(test_list, 2, "Popesecu Ion", "Economy", 500.3, "NU", undo_list, [])
    test_list = undo(test_list, undo_list, [])
    assert getNume(test_list[0]) == "Popesecu Ioan"
    assert getPret(test_list[0]) == 500.3


def test_redo():
    test_list = []
    undo_list = []
    redo_list = []
    addDO(test_list, 1, "Popesecu Ioan", "Economy", 500.3, "NU", undo_list, redo_list)
    test_list = undo(test_list, undo_list, redo_list)
    test_list = redo(test_list, undo_list, redo_list)
    assert getNume(test_list[0]) == "Popesecu Ioan"
    assert getPret(test_list[0]) == 500.3
    addDO(test_list, 2, "Popesecu Ion", "Economy", 500.3, "NU", undo_list, redo_list)
    test_list = undo(test_list, undo_list, redo_list)
    test_list = redo(test_list, undo_list, redo_list)
    assert getNume(test_list[0]) == "Popesecu Ioan"
    assert getPret(test_list[0]) == 500.3
    assert getNume(test_list[1]) == "Popesecu Ion"
    assert getID(test_list[1]) == 2


def test_functions():
    test_remove()
    test_add()
    test_modify()
    test_upgrade()
    test_discount()
    test_order()
    test_sums_for_names()
    test_undo()
    test_redo()
