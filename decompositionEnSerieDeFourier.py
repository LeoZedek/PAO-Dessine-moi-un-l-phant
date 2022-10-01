#!/usr/bin/env python3

def calcul_Cn(z,nb_cercle):
    nb_point = len(z)
    pas = 2*np.pi/nb_point
    t=np.arange(-np.pi,np.pi,pas)
    somme = np.trapz(z*np.exp(-1j*nb_cercle*t),dx=pas)
    return somme/(2*np.pi), t

def decompositions_en_serie_de_fourier(z,nb_cercle):
    Cn = []
    for nb in range(nb_cercle): 
        C_nb , t = calcul_Cn(z,nb)
        Cn.append(C_nb)
    return Cn,t
