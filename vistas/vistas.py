import datetime
import email
from flask import request
from flask_jwt_extended import jwt_required, create_access_token
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql import func
import time
import smtplib

from modelos import db, Usuario, UsuarioSchema
usuario_schema = UsuarioSchema()


class VistaSignIn(Resource):

    def post(self):
        nuevo_usuario = Usuario(usuario=request.json["usuario"], contrasena=request.json["contrasena"], nombre=request.json["nombre"], apellido=request.json["apellido"], cedula=request.json["cedula"], telefono=request.json["telefono"], email=request.json["email"], genero=request.json["genero"], direccion=request.json["direccion"], rol = "Apostador")
        db.session.add(nuevo_usuario)
        db.session.commit()
        token_de_acceso = create_access_token(identity=nuevo_usuario.id)
        return {"mensaje": "usuario creado exitosamente", "token": token_de_acceso, "id": nuevo_usuario.id}

    def put(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        usuario.contrasena = request.json.get("contrasena", usuario.contrasena)
        db.session.commit()
        return usuario_schema.dump(usuario)

    def delete(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        db.session.delete(usuario)
        db.session.commit()
        return '', 204


class VistaLogIn(Resource):

    def post(self):
        usr = request.json["usuario"]
        fecha =  time.strftime("%c")
        usuario = Usuario.query.filter(Usuario.usuario == request.json["usuario"],
                                       Usuario.contrasena == request.json["contrasena"]).first()
        db.session.commit()
        if usuario is None:
            
            file = open('log_signin.txt', 'a+')
            file.write('inicio de sesion incorrecto del usuario {} :{}\n'.format(usr,fecha))
            return "El usuario no existe", 404
        else:
            file = open('log_signin.txt', 'a+')
            file.write('inicio de sesion exitososo del usuario {} :{}\n'.format(usr,fecha))
            token_de_acceso = create_access_token(identity=usuario.id)
            return {"mensaje": "Inicio de sesión exitoso", "token": token_de_acceso}

class VistaEmailAprobarCompras(Resource):
    def post(self):
        message = 'Acaba de generar una compra por favor valìdela usando el còdigo 312454'
        subject = 'ABC Monitoring verificaciòn de compra'
        message = 'Subject: {}\n\n{}'.format(subject,message)
        server = smtplib.SMTP('smtp.gmail.com',587)
        server = starttls()
        server.login('mailsenderabcmonitoring@gmail.com','Arquitectura2022!')
        server.sendmail('mailsenderabcmonitoring@gmail.com','jorgeballe@gmail.com',message)
        server.quit()
        
        
