# PAO dessiner un Elephant
Ce dépot du projet assisté par ordinateur (PAO) dessiner des éléphants  

## Le sujet 
L'objectif de ce PAO est de réalisé une "application" en python afin de reproduire l'hypothèse de Van Neummann : 
" Avec 4 paramètre, je peux une bonne approximation d'un éléphant"  
Le projet sera présenté durant les Journée Portes Ouvertes de l'INSA 2023 afin de présenté le département ITI.  

L'application pourra à therme : 
 - redessiner un dessin selectionné à la souris (dans le cas des JPO sur un écran tacil)
 - n'être utilisable qu'à la souris (ou au doigt sur un écran tactile)
 - pouvoir changer le nombre de point échantilloné 
 - pouvoir changer le nombre de cercle pour changer qui approcime le dessin initial
 - choisir une image pré-dessiné
 - choisir n'importe quelle image

Le projet a été fortement inspiré de la vidéo de El Jj [Deux (deux ?) minutes pour l'éléphant de Fermi & Neumann](https://www.youtube.com/watch?v=uazPP0ny3XQ)


## Membres :
Réalisé sous la supervision de : M. DELESTRE et M. CHATELAIN
Réalisé par : Alexis IMBERT, Solène PERRET et Léo ZEDEK

## Pyenv 
### Installation 
[Voir le GitHub de pyenv ici](https://github.com/pyenv/pyenv)

### Installer la bonne version de python
Le projet utilise la version 3.10.2  
Pour installer cette version merci d'utiliser la commande : 

```bash
pyenv install 3.10.2
```

### définir la version local du projet
Pour utiliser la bonne version de python dans le projet, utiliser :
```bash
pyenv local 3.10.2
```
## Pipenv

(partie extraite d'un projet de M. DELESTRE)

To create the pipenv environnement, you need to execute the following command:
```bash
pipenv --python=3.10.2
```

In order to activate your virtual environment, you need to execute the following command:
```bash
pipenv shell
```
In order to execute the other commands, you will need your virtual environment activated

To exit from the virtual environment:
```bash
exit
```

If you want to install requirements, execute the following command:
```bash
pipenv install
```


## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.
