"""
Fichier regroupant les taux de compressions calculé
@author:Alexis IMBERT
"""

def taux_de_compression(nb_points_total : int, nb_points: int) -> float:
    """
    Calcul le taux de compression en pourcentage
    # Parameter
     - nb_points_total : le nombre de points de l'image de base
     - nb_points : le nombre de points choisi par l'utilisateur

     # Return :
     float : le taux de compression en pourcentage 
    """
    #return round(((nb_points-nb_cercle) / (nb_points)), 3)*100
    return ((nb_points_total - nb_points)/nb_points_total)*100