Using Python==3.9, DJano==4.0, HTMX, Bootstrap, HTML, CSS, Javascript


Requirements: Need Python on testing system to run this project

How To Run:

1) Create virtual envioronment using "python -m venv <venv_name>"
2) actiavte venv using "venv_name/scripts/activate" (on windows)/ "source venv_name/bin/activate" (on ubuntu)
3) Install django using "pip3 install django" (this is only requiemet for project)
3) Go inside "Animal" directory and run "python3 manage.py migrate" (using sqlite3 as database)
4) Run "python3 manage.py runserver"
5) Enter http://127.0.0.1:8000/ in browser.

Note:
1) Superuser credentils. username - skeshari, password - ListAnimal@123. Create new superuser using "python3 manage.py createsuperuser"
2) DB table has been created for Animal and Breed. Can be added dynamically.