""" Module permettant la gestion i18n (internationnalisation)
pour l'importation de la fonciton gettext et son alias _"""
import gettext
# Initialisation de la traduction
# Définition du chemin vers le dossier de traductions
TRANSLATIONS_PATH = './locales'

# définition du chemin vers le dossier de traduction
gettext.bindtextdomain("base", TRANSLATIONS_PATH)
gettext.textdomain("base")

# création d'une fonction _ qui utilise la fonction gettext.gettext
_ = gettext.gettext
