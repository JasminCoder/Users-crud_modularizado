#coneccion con la BD
from flask_app.config.mysqlconnection import connectToMySQL


class User:

    def __init__(self, data):
        #data = {"id": 1, "first_name":"Elena", "last_name":"De Troya", "email":"elena@dojo.com", 
        #"created_at":"2022-09-26", "update_at":"2022-09-26"}
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.update_at = data['update_at']


    @classmethod
    def guardar(cls, formulario):
        #formulario = {"first_name":"Juana", "last_name":"De Arco", "email":"juana@cd.com"}
        query = "INSERT INTO users(first_name, last_name, email) VALUES ( %(first_name)s, %(last_name)s, %(email)s )" 
        #->INSERT INTO users(first_name, last_name, email) VALUES('Juana', 'De Arco', 'juana@codingdojo.com')
        result = connectToMySQL('esquema_usuarios_ch').query_db(query, formulario)
        return result


#usuarios index.html
    @classmethod
    def muestra_usuarios(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('esquema_usuarios_ch').query_db(query)
        #[
            #{"id": "1", "first_name":"Elena", "last_name":"De Troya"..},
            #{"id": "2", "first_name":"Juana", "last_name":"De Arco"...}
        #]
        users = []
        for u in results: #en u voy a estar guardando mi diccionario
            user = cls(u) #user = User(u) -> {"id": "1", "first_name":"Elena", "last_name":"De Troya"..}
            users.append(user)
        return users


    #para borrar usuario
    @classmethod
    def borrar(cls, formulario):
        #formulario = {"id":"1"}
        query = "DELETE FROM users WHERE id = %(id)s"
        result = connectToMySQL('esquema_usuarios_ch').query_db(query, formulario)
        return result



    @classmethod
    def mostrar(cls, formulario):
        #formulario = {"id": "1"}
        query = "SELECT * FROM users WHERE id = %(id)s" #obtenemos el usuario con todas sus columnas / select siempre regresa una lista
        result = connectToMySQL('esquema_usuarios_ch').query_db(query, formulario) #result es una lista
        #result = (lista con 1 diccionario)[
            #{"id": "1", "first_name":"Elena".....}
        #]
        diccionario = result[0] #diccionario = {"id":"1"} / guardamos en el diccionario en la lista
        usuario = cls(diccionario) #usuario = User(diccionario)
        return usuario


    #funcion para update
    @classmethod
    def actualizar(cls, formulario):
        #recibimos formulario q será igual a... formulario = {"id":"1", "first_name":"Elena".....}
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s"
        result = connectToMySQL('esquema_usuarios_ch').query_db(query, formulario)
        return result
