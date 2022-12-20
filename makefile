
all : run

preinstall :
	pyenv install 3.10.2
	pyenv local 3.10.2
	pipenv --python=3.10.2
	pyenv shell 3.10.2

install :
	pipenv shell
	pipenv install

traduction :

run :
	python main.py