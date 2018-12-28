cd /d %~dp0/web

python manage.py makemigrations

python manage.py migrate webapp 0002

pause
