# create virtual environment
venv:
	virtualenv venv

# install all needed for development
develop: venv
	venv/bin/python3 -m pip install -e . -r requirements_pytest.txt
	venv/bin/python3 -m pip install -e . -r requirements.txt

# clean the development environment
clean:
	-rm -rf venv
