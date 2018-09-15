from flask_restful import Resource
import flask
from models import order

class MakeOrder(Resource):
    def post(self):
        orders=order()
        product = flask.request.form["product"]
        quantity = flask.request.form["quantity"]
        price = flask.request.form["price"]
        if product=="" or quantity=="" or price=="":
            return {"Error":"The order is incomplete please try again"}
        else:
            newOrder={"product":product, "quantity":quantity, "price":price}
            return orders.makeOrder(newOrder)


class Orders(Resource):
    def get(self):
        orders = order()

        return orders.listOrders()


class SpecificOrder(Resource):
    def get(self, id):
        orders=order()
        orderid = int(id)
        return orders.specificOrder(orderid)


class UpdateOrder(Resource):
    def put(self, id):
        orders=order()
        orderStatus = flask.request.form["status"]
        return orders.updateOrder(id,orderStatus)

