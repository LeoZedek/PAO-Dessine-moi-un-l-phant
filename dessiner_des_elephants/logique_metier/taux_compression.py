"""
Fichier regroupant les taux de compressions calculé
@author:Alexis IMBERT
"""


def taux_de_compression(nb_points: int, nb_cercle: int) -> float:
    """
    Calcul le taux de compression en pourcentage
    # Parameter
     - nb_points : le nombre de points gardé pour le dessin
     - nb_cercle : le nombre de cercle stocké afin de reproduire le dessin

     # Return :
     float : le taux de compression en pourcentage arrondi 
    """
    return round(((nb_points-nb_cercle) / (nb_points)), 3)*100
