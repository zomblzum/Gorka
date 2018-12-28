cd /d %~dp0/web

python manage.py migrate

python manage.py makemigrations

python manage.py migrate webapp 0001

pause
