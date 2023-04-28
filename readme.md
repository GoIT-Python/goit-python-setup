# collections:

# list mut ord nu []

# tuple immut ord nu (,)

# set mut no un {}

# frozenset immut no un frozenset ()

# dict mut no nu-un {'key': 'value'}

# str immut ord nu '', "", """""", ''''''

# virtual environment

python -m venv .venv
source .venv/bin/activate
(.venv) deactivate
pip install -r requirements.txt
список установленных пакетов: pip list
список установленных пакетов с версиями: pip freeze
pip uninstall some_package
pip freeze > requirements.txt

build:
https://packaging.python.org/en/latest/tutorials/packaging-projects/
python3 -m pip install --upgrade build
python3 -m build

Uploading the distribution archives:
python3 -m pip install --upgrade twine
python3 -m twine upload --repository testpypi dist/\*

Setuptools Entry Points:
https://setuptools.pypa.io/en/latest/userguide/entry_point.html
