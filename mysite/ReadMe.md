# Requirements
1. Git
2. python


# Instalation
1. Install GIT
2. Install Python
3. Clone django project into server  ``git clone https://github.com/BoksanD/django-test`` or follow django-admin documentation for installation
4. Instal Django with comand ``python -m pip install Django``
5. install requests `` python -m pip install requests ``


# Configuration
settings.py
``
    DATABRICKS_CONNECTIONS = {
    'default': {
        'HOST': "host name",
        'TOKEN': "personel token",
        'WAREHOUSE_ID': "warehouseid",
    },
}
``
warehouse id and host can can be taken from databrics connection, sql connection of SQL Warehouse.
Host taken from connection must finish with .net/api/2.0/sql/statements/?
