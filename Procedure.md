# Django-MVT-CRUD-operations-Employee-Details

Django

# Create a seprate folder and inside that create virtaul environment
pip3 install virtualenv // Create Virtual Environment 
virtualenv --version  //check versionn	
virtualenv env_name   //set name for environment(takes copy of py packages inside env)
source env_name/scripts/activate  //after actavating, env name will be shown in bracket
Set-ExecutionPolicy -ExecutionPolicy Remotesigned (if error exist in above)//open shell in admin mode and type


python3 -m pip install Django // Install Django
python3 -m django --version
django-admin startproject Project_Name // Create a project Application (seperate folder will be created)

// Navigate to Project Folder
cd Project_Name/

python manage.py makemigrations //after adding extra functionality
python manage.py migrate  //after adding extra functionality
python manage.py runserver //it will host

//
python manage.py startapp app_name
python manage.py runserver
