
from flask import Flask, render_template, request, url_for, flash
from werkzeug.utils import redirect
from flask_mysqldb import MySQL


app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'sql881.main-hosting.eu'
app.config['MYSQL_USER'] = 'u919273444_clinicas'
app.config['MYSQL_PASSWORD'] = 'Root-123456'
app.config['MYSQL_DB'] = 'u919273444_clinicasdb'

mysql = MySQL(app)