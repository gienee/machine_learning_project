FROM python:3.7
COPY. /app     ### this app folder in which all the files/folder are copied present in the python 3.7
WORKDIR /app   ### this app folder working in the same directory
Run pip install -r requirements.txt
EXPOSE $PORT   $### $PORT, it is the variable name which is fixed or given by the heroku..
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app   ###there is 4 workers means 4 systems run paralley and run it very efficiently, it may be change based on the system.
#3# first "app" is the module name and second "app" is the flask name