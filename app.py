from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api

from modelos import db
from modelos.modelos import Usuario, UsuarioSchema
from vistas import  VistaSignIn, VistaLogIn

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eporra.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'frase-secreta'
app.config['PROPAGATE_EXCEPTIONS'] = True

import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

with app.app_context():
   usuario_schema = UsuarioSchema
   usuario_test = Usuario(usuario = "user_test", contrasena = "password", nombre="user_test", apellido= "user_test",cedula="9000000",telefono ="88888", email = "test@test.com", genero ="masculino", direccion="asdasd", rol="test")
   db.session.add(usuario_test)
   db.session.commit()
#     apostador_Schema=ApostadorSchema()

#     apuesta_schema =ApuestaSchema()
    
#     A = Apostador(nombre_apostador= "Jose")
#     A1 = Apostador(nombre_apostador= "Manuel")
#     c = Apuesta (valor_apostado=100,nombre_apostador="jose")
#     c1 = Apuesta (valor_apostado=200,nombre_apostador="jose")

#     A.apuestas.append(c)
#     A.apuestas.append(c1)

     

    
#     db.session.add(A)
#     db.session.commit()
#     Apuesta.query.filter_by(apostador=1).all()
    
   #print( Apostador.query.filter_by(id=1).all()[].nombre_apostador)
#  


cors = CORS(app)


api = Api(app)
api.add_resource(VistaSignIn, '/signin')
api.add_resource(VistaLogIn, '/login')


jwt = JWTManager(app)
