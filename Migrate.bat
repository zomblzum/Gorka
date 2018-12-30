cd /d %~dp0/web

python manage.py migrate

pause

python manage.py makemigrations

pause

python manage.py migrate webapp 0009

pause