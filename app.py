from flask import Flask
from flask_restful import Api
import resources
app = Flask(__name__)
app.debug=True
api = Api(app)
api.add_resource(resources.MakeOrder, '/order')
api.add_resource(resources.Orders, '/order')
api.add_resource(resources.SpecificOrder, '/order/<id>')
api.add_resource(resources.UpdateOrder, '/order/<id>')


if __name__ == '__main__':
	app.run()