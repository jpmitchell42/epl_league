```bash

#create a new virtual environment using python3 
# you might have your own way of doing this like pipenv or virtualenv and thats fine
python3 -m venv venv

# activate the virtual environment
. venv/bin/activate

# install all the requirements from requirements.txt
pip3 install -r requirements.txt

# make your migrations. If you did the django tutorial, notice we're skipping makemigrations because
# the migartion files already exist in epl_league_api/migrations We just need to apply them
# this creates the tables our models define in a local sqlite database
python manage.py migrate

# Create a super user for yourself. 
python manage.py createsuperuser
# choose something simple. You can skip the email field just by pressing enter.
# This will only work locally. Put your username and password somewhere so you dont forget

# first lets look at the contents of our dbs. 
python manage.py runserver
# See your console print out a url. Should be http://127.0.0.1:8000/
# This is your localhost, the current "computer" you're running it from on port djangos default port
# go to this url in a browswer and login with your admin credentials


# Click on the "http://127.0.0.1:8000/users/" and you will see a representation of whats in the users table
# go back and click on soccer_teams, it will be empty
# We need to populate these on your local database which exists entirely as the db.sqlite3 file you see in your current directory

# we are using a tool called django_extions (see we've installed it from requirements.txt)
# The main versions of this that are useful are the shell_plus which allows you to fuck around
# and the script running ability
# we use the scripts to populate the databse

# ctrl c to kill your server

# create the soccer teams by running create_soccer_teams.py which reads from teams.csv
# running from with shell_plus allows it to access the models we've created
python manage.py runscript create_soccer_teams

# create the schedule which runs create_schedule20_21.py which reads from the epl_20_21.csv 
python manage.py runscript create_schedule20_21

# check your server again and look at the soccer teams / fixtures /game lines
python manage.py runserver
```