heroku accounts:set personal
heroku pg:backups:capture -a awesomepower
heroku pg:backups:download -a awesomepower
pipenv run python manage.py flush --no-input
pg_restore -d awesomepower latest.dump --clean --no-privileges --no-owner
rm latest.dump
