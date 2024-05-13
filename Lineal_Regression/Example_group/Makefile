

all: 

# Creamos un entorno virtual
create_venv:
	python3 -m venv venv

# Nos permite activar el entorno virtual
activate_venv:
	. venv/bin/activate

init_project: create_venv install_requirements
	. venv/bin/activate && python3 Linear_Regression.py

# Intalamos los requerimientos del proyecto
install_requirements: activate_venv
	. venv/bin/activate && venv/bin/pip install -r requirements.txt

create_requirements: activate_venv
	venv/bin/pip freeze >> requirements.txt
