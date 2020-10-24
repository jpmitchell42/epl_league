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

# create your secrets file. I've included secrets_example.json 
# the actual program reads from secrets.json which is in the .gitignore
cp secrets_example.json secrets.json

# Create a super user for yourself. 
python mangage.py createsuperuser
# choose something simple. You can skip the email field just by pressing enter.
# This will only work locally. Put your username and password in secrets.json

# we are using a tool called django_extions (see we've installed it from requirements.txt)
# The main versions of this that are useful are the shell_plus which allows you to fuck around
# and the script running ability

```