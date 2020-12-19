##Virtual Environment

### Creating virtual environment

* virtualenv -p python3 .
* source bin/activate (or .\Scripts\activate)
* pip3 install django==2.0.7

### Activating virtual environment

* cd django-project-folder
* source bin/activate  (or .\Scripts\activate)
* deactivate

### Looking at the requirements

* pip3 freeze

It's important to use virtual environment for your projects for several reasons.
I. it keeps all the requirements seperate.

### 3 ways to create a virtual environment

* virtualenv venv
* virtualenv venv2 -p python3
(To find the location where python3 is intalled: which python3)
(Add the path to the command)
* virtualenv venv3 -p python3_path
### The 4th method to create virtual environment

* mkdir venv4
* cd venv4
* virtualenv . -p python3


