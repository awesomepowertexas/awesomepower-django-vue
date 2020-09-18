dropdb awesomepower
createdb awesomepower
pipenv run python manage.py migrate
heroku accounts:set personal
heroku pg:backups:capture -a awesomepower
heroku pg:backups:download -a awesomepower
pg_restore -d awesomepower latest.dump --clean --no-privileges --no-owner
rm latest.dump
