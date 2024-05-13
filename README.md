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

## La traduction :
Cette application prend en charge la traduction. Pour le moment les 2 langue prise en charge sont l'anglais - par défaut - et le francais.

Cette internationalisation (i18n) utilise le module gettext.

Il faut préalablement installer le module gettext sur votre machine en executant la commande suivante :
```bash
sudo apt install gettext
```

Pour lancer l'application veuillez utiliser le make run qui va automatique compiler les fichier de compilation.

### Ajout texte dans l'application
si vous souhaitez ajouter du texte traduisible :
1. Si le module ne l'a pas déjà : ajouter l'import de la fonction ```_``` avec la ligne suivante :
```python
from dessiner_des_elephants.traduction import _
```
2. Encadrer le texte à traduire de la manière suivante :  ```_("texte à traduire")```
3. Utiliser la commande 
```bash
make pre_traduction
```
Pour générer le fichier base.pot (il sera générer dans le dossier locales de l'applciation)

4. À partir du fichier base.pot créer un fichier base.po par langue à traduire.
Dans les fichiers base.po ```msgid``` représente la chaine de caractère original et ```msgstr``` la chaine de caractère traduite.
Il faut mettre les fichiers base.po dans un dossier portant le code de la langue (fr pour francais par exemple), dans ce dossier il faut mettre un dossier LC_MESSAGES puis le fichier base.po

5. Pour compiler les fichiers base.po en base.mo utilisable par l'application il faut faire la commande :
```bash
make traduction
```
OU lancer le directement l'application avec la commande ce qui compilera juste avant les fichiers base.po
```bash
make run
```


## Roadmap
Pour la suite du projet nous avons pensez à :
 - réaliser une séparation MVC (modèle view controleur : séparation de la vu et des données)
 - transformer la galerie (composé de .dump) en .jpg
 - pour la ressemblance dtw, prendre le même point de départ
 - dessiner des droites entre chaque point
 - mettre le même nombre de point que la visualisation du dessin original dans le dessin reconstitué
