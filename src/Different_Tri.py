def tri_insertion(Tableau):
    """list[int] -> list[int]
    Condition: len(Tableau)>=1
    Role: tri le tableau de façon croissante à partir de la méthode du
    tri insertion. Le principe du tri insertion est de faire des
    comparaison d'élément à la fois en balayant plusieurs fois le tableau.
    """
    for i in range(1, len(Tableau)):
        valeur = Tableau[i]
        j = i
        while (j > 0) and (Tableau[j - 1] > valeur):
            Tableau[j] = Tableau[j - 1]
            j = j - 1
        Tableau[j] = valeur
    return Tableau


def tri_selection(table):
    """  role : Le tri par sélection est un algorithme de tri qui consiste à sélectionner répétitivement l'élément le
    plus petit ou le plus grand d'une liste non triée et à l'ajouter à une nouvelle liste triée. Il parcourt la liste
    à trier pour trouver l'élément le plus petit, échange cet élément avec le premier élément de la liste,
    puis recommence le processus avec la sous-liste restante. Il répète ce processus jusqu'à ce que tous les éléments
    aient été triés. """

    for i in range(len(table)):
        # Trouver le minimum
        min = i
        for j in range(i + 1, len(table)):
            if table[min] > table[j]:
                min = j
        valeur = table[i]
        table[i] = table[min]
        table[min] = valeur
    return table


def tri_a_bulles(Table):
    """
    Rôle : L'algorithme de tri à bulles est un algorithme de tri qui consiste à comparer répétitivement les éléments consécutifs d'un tableau, et à les permuter lorsqu'ils sont mal triés.
    """
    # boucle sur tous les éléments de la liste
    for i in range(len(Table) - 1):
        # boucle sur les éléments non triés
        for j in range(len(Table) - 1 - i):
            # variable pour vérifier si un échange a été fait
            echange = False
            # compare l'élement courant à son voisin
            if Table[j] > Table[j+1]:
                # échange les élements s'ils sont dans le mauvais ordre
                Table[j], Table[j+1] = Table[j+1], Table[j]
                 # indique qu'un échange a été fait
                echange == True
                # si un échange a été fait
                if echange == True :
                    # retourne la liste triée
                    return Table
    # retourne la liste triée
    return Table

def tri_cocktail(liste: list) -> list:
    """
    Fonction permettant d'effectuer un tri croissant à partir de la méthode du
    tri cocktail.
    Le principe du tri cocktail est de faire des vas et viens sur la liste afin
    de mettre en position les valeurs en fonction du rétrécissement de la liste
    et de les mettre dans les positions maximum et minimum du rétrécissement.

    >>> tri_cocktail([4, 2, 5, 7, 3])
    [2, 3, 4, 5, 7]
    """
    # valeur booléenne
    echanger_bool = True
    # tant que echanger_bool est à True
    while echanger_bool:
        echanger_bool = False
        # boucle allant de 0 jusqu'à la longueur de la liste - 1
        for i in range(0, len(liste) - 1):
            # si l'élement est supérieur à l'élement de droite
            if liste[i] > liste[i + 1]:
                # méthode pour alterner les valeurs
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
                echanger_bool = True
        # boucle allant de la longueur de la liste - 2 jusqu'à -1
        for i in range(len(liste) - 2, -1, -1):
            # si l'élement est supérieur à l'élement de droite
            if liste[i] > liste[i + 1]:
                # méthode pour alterner les valeurs
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
                echanger_bool = True
    return liste


def tri_peigne(liste):
    """Cette fonction tri la liste passé en argument à l'aide l'algorithme de tri à peigne.

    Args:
        liste (list[int]): une liste d'entier
    """
    intervalle = len(liste)
    echange = True
    while intervalle > 1 or echange:
        intervalle = int(intervalle / 1.3)
        if intervalle < 1:
            intervalle = 1

        i = 0
        echange = False

        while i < len(liste) - intervalle:
            if liste[i] > liste[i + intervalle]:
                liste[i], liste[i + intervalle] = liste[i + intervalle], liste[i]
                echange = True
            i += 1
    return liste


def fusionne(tab1, tab2):
    """list[int], list[int] -> list[int]
    Préconditions : tab1 et tab2 sont triés dans l'ordre croissant
    Rôle : fusionne les deux tableaux en un seul, trié dans l'ordre croissant"""
    # Initialisation des indices de chaque tableau
    i1 = 0
    i2 = 0
    it = 0

    len2 = len(tab1) + len(tab2)  # Calcul de la longueur du futur tableau à trier
    tab_trie = [0] * len2  # Initialisation du futur tableau a trié

    # Comparaison des valeurs du premier tableau avec les valeurs du second tableau
    while i1 < len(tab1) and i2 < len(tab2):
        v1, v2 = tab1[i1], tab2[i2]
        if v1 <= v2:
            i1 += 1
            tab_trie[it] = v1  # Ajout des valeurs dans le tableau trié
        else:
            i2 += 1
            tab_trie[it] = v2  # Ajout des valeurs dans le tableau trié
        it += 1
    while i1 < len(tab1):  # Traitement des cas apparts : Tableau gauche
        tab_trie[it] = tab1[i1]
        it += 1
        i1 += 1
    while i2 < len(tab2):  # Traitement des cas apparts : Tableau droit
        tab_trie[it] = tab2[i2]
        it += 1
        i2 += 1
    return tab_trie  # On retourne le nouveau tableau fusionné


def tri_fusion(tab):
    """list[int] -> list[int]
    Préconditions :
    Rôle : retourne le tableau trié dans l'ordre croissant"""
    if len(tab) <= 2:  # Cas de base, si la longueur du tableau est inférieure ou égale à 2 valeurs, alors fusionner la première moitié du tableau avec la seconde moitié.
        return fusionne(tab[:1], tab[1:])
    return fusionne(tri_fusion(tab[:len(tab) // 2]), tri_fusion(tab[
                                                                len(tab) // 2:]))  # Sinon, on fusionne les tableaux gauche (première moitié) et droite (seconde moitié) qui seront eux même divisés en 2.


def tri_rapide(tab):
    """
        Function return sorter list with quick sorter
    """
    if len(tab) < 2:
        return tab
    else:
        pivot = tab.pop(len(tab) // 2)
        minpart = [i for i in tab if i < pivot]
        maxpart = [i for i in tab if i >= pivot]
        return tri_rapide(minpart) + [pivot] + tri_rapide(maxpart)
