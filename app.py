from flask import Flask, render_template
from peewee import *

app = Flask(__name__)
app.config.from_object('config_local')

db = MySQLDatabase(
	app.config['MYSQL_DB'], 
	user=app.config['MYSQL_USER'], 
	passwd=app.config['MYSQL_PASSWORD'],
	host=app.config['MYSQL_HOST']
)

import views