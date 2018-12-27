cd /d %~dp0/web

python manage.py migrate

pause

python manage.py makemigrations

python manage.py migrate blog 0001

