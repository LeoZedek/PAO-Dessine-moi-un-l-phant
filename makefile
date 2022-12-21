# génération du fichier .pot
POT_FILE := base.pot
PYTHON_FILES := $(shell find . -name "*.py")

# préparation à la traduction
LOCALES_DIR := locales
PO_FILES := $(wildcard $(LOCALES_DIR)/*/*/*.po)#recherche de fichier .po
MO_FILES := $(patsubst %.po,%.mo,$(PO_FILES))#liste des fichier .mo à compiler

%.mo: %.po
	msgfmt $< -o $@

.PHONY: clean

all : run

preinstall :
	pyenv install 3.10.2
	pyenv local 3.10.2
	pipenv --python=3.10.2
	pyenv shell 3.10.2

install :
	pipenv shell
	pipenv install

pre_traduction : $(POT_FILE)

$(POT_FILE): $(PYTHON_FILES)
	xgettext -o $(LOCALES_DIR)/$@ $(PYTHON_FILES)

traduction : $(MO_FILES)

run : traduction
	python main.py

clean:
	rm -f $(MO_FILES)
