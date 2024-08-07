from flask import Flask
from flask_cors import CORS

from routes.ansiedad_routes import ansiedad_routes
from routes.diagnostico_routes import diagnostico_routes
from routes.ansiedad_semaforo_routes import ansiedad_semaforo_routes
from routes.opciones_routes import opciones_routes
from routes.preguntas_routes import preguntas_routes
from routes.test_routes import test_routes
from routes.especialistas_routes import especialistas_routes
from routes.titulo_routes import titulo_routes
from routes.tratamientos_routes import tratamientos_routes
from routes.ubigeo_routes import ubigeo_routes
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
app.register_blueprint(titulo_routes)
app.register_blueprint(ansiedad_semaforo_routes)
app.register_blueprint(ubigeo_routes)
app.register_blueprint(diagnostico_routes)
app.register_blueprint(ansiedad_routes)
app.register_blueprint(tratamientos_routes)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(port=8000)
