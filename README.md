# pyflaskblog
Test repo for study python Flask

  Preparation:
sudo apt install virtualenv python3-pip mysql-server
mkdir flask
cd flask
mkdir app
virtualenv venv
source venv/bin/activate
pip3 install flask flask-script flask-migrate flask-sqlalchemy mysql-connector
mysql -u root -p
create database blog character set utf8 collate utf8_unicode_ci;

  Migration:
python3 migrate.py db init
python3 migrate.py db migrate
python3 migrate.py db upgrade
