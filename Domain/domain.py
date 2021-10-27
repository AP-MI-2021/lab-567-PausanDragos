def getID(rezervare):
    """
    Gasim ID-ul unei rezervari
    :param rezervare: dictionar
    :return: int
    """
    return rezervare[0]


def getNume(rezervare):
    """
    Gasim numele unei rezervari
    :param rezervare: dictionar
    :return: str
    """
    return rezervare[1]


def getClasa(rezervare):
    """
    Gasim clasa unei rezervari
    :param rezervare: dictionar
    :return: str
    """
    return rezervare[2]


def getPret(rezervare):
    """
    Gasim pretul unei rezervari
    :param rezervare: dictionar
    :return: float
    """
    return rezervare[3]


def getCheckin(rezervare):
    """
    Gasim situatia checkin-ului unei rezervari
    :param rezervare: dictionar
    :return: str
    """
    return rezervare[4]


def setNume(rezervare, newNume):
    """
    Modificam numele unei rezervari
    :param rezervare: dictionar
    :param newNume: str
    :return: str
    """
    rezervare[1] = newNume


def setClasa(rezervare, newClasa):
    """
    Modificam clasa unei rezervari
    :param rezervare: dictionar
    :param newClasa: str
    :return: str
    """
    rezervare[2] = newClasa


def setPret(rezervare, newPret):
    """
    Modificam pretul unei rezervari
    :param rezervare: dictionar
    :param newPret: float
    :return: float
    """
    rezervare[3] = newPret


def setCheckin(rezervare, newCheckin):
    """
    Modificam situatia checkin-ului unei rezervari
    :param rezervare: dictionar
    :param newCheckin: str
    :return: str
    """
    rezervare[4] = newCheckin