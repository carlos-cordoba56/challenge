from flask import Flask, request

app = Flask(__name__) 


@app.route('/', methods=['GET']) 
def index():
	return "Hello worasakfeoijoiasld"

@app.route('/productos', methods=['GET']) 
def productos():
	return "All productos"

@app.route('/producto/<product_id>')
def get_product(product_id):
  return "The product is " + str(product_id)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')