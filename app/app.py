import time
from db import Productos, get_db
from settings import settings
from flask import Flask

app = Flask(__name__)



@app.route('/', methods=['GET']) 
def index():
  return f"Welcome to {settings.app_name}"

@app.route('/productos', methods=['GET']) 
def get_all_products():
    conection = get_db()
    productos = conection.query(Productos).all()
    return productos

@app.route('/producto/<product_id>', methods=['GET'])
def get_product(product_id):
    conection = get_db()
    producto = conection.query(Productos)\
      .filter(Productos.id == product_id).first()
    return producto

if __name__ == '__main__':
    print("Waiting for db to start...")
    time.sleep(300)
    app.run(host='0.0.0.0')