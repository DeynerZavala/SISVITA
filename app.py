from flask import Flask
from flask_cors import CORS

from routes.opciones_routes import opciones_routes
from routes.preguntas_routes import preguntas_routes
from routes.test_routes import test_routes
from routes.especialistas_routes import especialistas_routes
from routes.usuarios_routes import usuarios_routes
from config import DATABASE_CONNECTION_URI
from utils.db import db

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_POOL_SIZE"] = 20
app.config["SQLALCHEMY_POOL_TIMEOUT"] = 30
app.config["SQLALCHEMY_POOL_RECYCLE"] = 1800

# no cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

db.init_app(app)

app.register_blueprint(usuarios_routes)
app.register_blueprint(especialistas_routes)
app.register_blueprint(test_routes)
app.register_blueprint(preguntas_routes)
app.register_blueprint(opciones_routes)
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(port=8000)
