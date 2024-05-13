"""
Fichier regroupant les taux de compressions calculé
"""

def compression_rate_sampling(nb_points_total : int, nb_points: int) -> float:
    """
    Calcul le taux de compression du sampling en pourcentage
    # Parameter
     - nb_points_total : le nombre de points de l'image de base
     - nb_points : le nombre de points choisi par l'utilisateur

     # Return :
     float : le taux de compression en pourcentage 
    """
    return ((nb_points_total - nb_points)/nb_points_total)*100

def compression_rate_circles(nb_points_total : int, nb_cercles: int) -> float:
    """
    Calcul le taux de compression du dessin reconstruit en pourcentage
    # Parameter
     - nb_points_total : le nombre de points de l'image de base
     - nb_cercles : le nombre de cercles choisi par l'utilisateur

     # Return :
     float : le taux de compression en pourcentage 
    """
    return ((nb_points_total - nb_cercles)/nb_points_total)*100
