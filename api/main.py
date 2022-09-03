import flask
import flask_mysqldb
from flask_mysqldb import MySQL

app = flask.Flask(__name__)

app.config["DEBUG"] = True
app.config["MYSQL_HOST"] = 'host.docker.internal'
app.config["MYSQL_PASSWORD"] = ''
app.config["MYSQL_DB"] = 'flaskhost'
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port="5000")


from endpoints.loss import loss_blup

app.register_blueprint(loss_blup, url_prefix="/loss")