from random import randint
from time import perf_counter
from matplotlib import pyplot as plt
import Different_Tri


def moyenne(Tableau):
    """ List -> int
    Fait la moyenne d'une list fourni en argument
    """
    somme = 0
    for Valeur in Tableau:
        somme += Valeur
    return somme / len(Tableau)


def calcule_perf(taille, nombre_essai, cas):
    """int,int,str -> Dico{nom_tri:list}
        Calcule la moyenne des performances temporelles de plusieurs fonctions de n nombre d'essais
        Par taille de list de 10 en 10 jusqu'à taille *10
        """
    dico_des_fonctions = {
        "tri_selection": Different_Tri.tri_selection, "tri_insertion": Different_Tri.tri_insertion,
        "tri_a_bulles": Different_Tri.tri_a_bulles, "tri_cocktail": Different_Tri.tri_cocktail,
        "tri_peigne": Different_Tri.tri_peigne, "tri_fusion": Different_Tri.tri_fusion,
        "tri_rapide": Different_Tri.tri_rapide}
    perf_cas = [0 for _ in range(nombre_essai)]  # tableau qui aura temps de chaque essai sur 200
    Temps_de_toute_perf_par_tri = {"tri_selection": [], "tri_insertion": [], "tri_a_bulles": [], "tri_cocktail": [],
                                   "tri_peigne": [], "tri_fusion": [], "tri_rapide": []}
    if taille <= 0 or nombre_essai <= 0:
        return
    for j in range(10, (taille + 1) * 10, 10):  # Boucle pour chaque taille de 10 en 10 jusqu'à taille*10
        print("Taille de tableau :", j)
        Tableaualeatoire = [randint(1, 100) for _ in range(j)]  # Création Tableau aléatoire
        for values, func in dico_des_fonctions.items():  # Boucle pour chaque fonction
            for i in range(nombre_essai):  # #Boucle pour le nombre d'essais défini
                if cas == 'aléatoire':
                    Tableau = Tableaualeatoire[::]  # Création Tableau aléatoire
                elif cas == 'meilleure':
                    Tableau = [num for num in range(j)]  # Création Tableau trié dans l'ordre croissant
                elif cas == 'pire':
                    Tableau = [num for num in range(j - 1, -1, -1)]  # Création Tableau trié dans l'ordre décroissant
                else:
                    return None
                # Calcul des performances temporelles
                debut = perf_counter()
                func(Tableau)
                fin = perf_counter()
                perf_cas[i] = fin - debut
            Temps_de_toute_perf_par_tri[values].append(moyenne(perf_cas))
    return Temps_de_toute_perf_par_tri


def Afficher_graphique(taille, nombre_essai, cas):
    """int,int,str -> None
    Crée, affiche et sauvegarde le graphique de matplotlib
    Par rapport à la moyenne des performances """
    total_performance = calcule_perf(taille, nombre_essai, cas)  # prend la valeur, de la fonction calcule_perf
    if total_performance is not None:
        for keys, values in total_performance.items():  # Boucle pour chaque clé et valeurs du dico
            plt.plot([i for i in range(10, (taille + 1) * 10, 10)], values, label=keys)  # création des courbes
        plt.legend()
        plt.title("Graphique linéaire de la mesure en temps de chaque tri (" + cas + " cas )")
        plt.xlabel("Nombre d'élément dans le tableau")
        plt.ylabel('Temps')
        plt.savefig("fig" + cas + ".png")
        plt.show()
        print("figure sauvegardée")
