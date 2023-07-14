# IMPORTAR
# flask
# flask_cors
# flask_sqlalchemy
# flask_marshmallow

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Crear la app
app = Flask(__name__)

# Utilizar Cors, permite el acceso al frontend
CORS(app)

# CONFIGURACIÓN A LA BASE DE DATOS DESDE app
# (SE LE INFORMA A LA APP DONDE UBICAR LA BASE DE DATOS)
                                                    # //user:password@url/nombre de la base de datos
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/Casamagnahotel'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False 

# Crear el objeto db
# Notifica a la app que trabajará con SQLAlchemy
db = SQLAlchemy(app)

# Objeto ma permite acceder a los métodos para transformar datos
ma = Marshmallow(app)

# DEFINICIÓN DE LA TABLA A PARTIR DE UNA CLASE (Producto)
class Habitacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre =db.Column(db.String(100))
    precio = db.Column(db.Integer)
    stock = db.Column(db.Integer)
    imagen = db.Column(db.String(400))

    def __init__(self,nombre, precio,stock,imagen):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.imagen = imagen


# CÓDIGO DE CREACIÓN DE LA TABLA
with app.app_context():
    db.create_all()

# CREAR UNA CLASE  ProductoSchema, 
# DONDE SE DEFINEN LOS CAMPOS DE LA TABLA
class HabitacionSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','precio','stock','imagen')

# CREAR DOS OBJETOS PARA TRANSFORMAR
habitacion_schema = HabitacionSchema() # Permitir convertir un sólo dato. Ej: 1 objeto
habitaciones_schema = HabitacionSchema(many=True) # Permitir convertir un listado de datos. Ej: lista de objetos
    
# CREAR LAS RUTAS PARA: productos
# '/productos' ENDPOINT PARA MOSTRAR TODOS LOS PRODUCTOS; producto:habitacion
# DISPONIBLES EN LA BASE DE DATOS: GET

@app.route("/habitaciones", methods=['GET'])
def get_habitaciones():
    # Consulta toda la info de la tabla productos
    all_habitaciones = Habitacion.query.all()
    return habitaciones_schema.jsonify(all_habitaciones)


# '/productos' ENDPOINT PARA RECIBIR DATOS: POST
@app.route('/habitaciones', methods=['POST']) # crea ruta o endpoint
def create_habitacion():
    
    # Entrada de datos:
#     {
#       "imagen": "https://picsum.photos/200/300?grayscale",
#       "nombre": "MICROONDAS",
#       "precio": 50000,
#       "stock": 10
#    }
   
    nombre=request.json['nombre']
    precio=request.json['precio']
    stock=request.json['stock']
    imagen=request.json['imagen']

    new_habitacion=Habitacion(nombre,precio,stock,imagen)
    db.session.add(new_habitacion)
    db.session.commit()

    # Retornar los datos guardados en formato JSON 
    # Para ello, usar el objeto producto_schema para que convierta con                   # jsonify los datos recién ingresados que son objetos a JSON  
    return habitacion_schema.jsonify(new_habitacion)


# '/productos/<id>' ENDPOINT PARA MOSTRAR UN PRODUCTO POR ID: GET
@app.route('/habitaciones/<id>',methods=['GET'])
def get_habitacion(id):
    habitacion=Habitacion.query.get(id)
    return habitacion_schema.jsonify(habitacion)   


@app.route('/habitaciones/<id>',methods=['DELETE'])
def delete_habitacion(id):
    # Consultar por id, a la clase Producto.
    #  Se hace una consulta (query) para obtener (get) un registro por id
    habitacion=Habitacion.query.get(id)
    
    # A partir de db y la sesión establecida con la base de datos borrar 
    # el producto.
    # Se guardan lo cambios con commit
    db.session.delete(habitacion)
    db.session.commit()
    
    # Devuelve un json con el registro eliminado
    # Para ello, usar el objeto producto_schema para que convierta con                     # jsonify el dato recién eliminado que son objetos a JSON  
    return habitacion_schema.jsonify(habitacion)   


# '/productos/<id>' ENDPOINT PARA MODIFICAR UN PRODUCTO POR ID: PUT
@app.route('/habitaciones/<id>', methods=['PUT'])
def update_habitacion(id):
    # Consultar por id, a la clase Producto.
    #  Se hace una consulta (query) para obtener (get) un registro por id
    habitacion=Habitacion.query.get(id)
 
    #  Recibir los datos a modificar
    nombre=request.json['nombre']
    precio=request.json['precio']
    stock=request.json['stock']
    imagen=request.json['imagen']

    # Del objeto resultante de la consulta modificar los valores  
    habitacion.nombre=nombre
    habitacion.precio=precio
    habitacion.stock=stock
    habitacion.imagen=imagen
#  Guardar los cambios
    db.session.commit()
# Para ello, usar el objeto producto_schema para que convierta con                     # jsonify el dato recién eliminado que son objetos a JSON  
    return habitacion_schema.jsonify(habitacion)



# BLOQUE PRINCIPAL 
if __name__=='__main__':
    app.run(debug=True)