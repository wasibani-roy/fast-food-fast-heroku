import os
import random
orders={}
class order:

    def __init__(self):
        self.orders=orders
    def makeOrder(self, new_order):
        x = random.randint(1, 20)
        self.orders[x]= new_order
        return new_order

    def listOrders(self):

        return {"order_details": self.orders, "status_code":200}

    def specificOrder(self,orderId):
        y=int(orderId)
        if y in self.orders.keys():
            return self.orders[y]
        else:
            return ('Sorry orderid not found')

    def updateOrder(self,orderId,orderStatus):
        newStatus=int(orderStatus)
        if newStatus == 1:
            self.orders[orderId].update({"Status": "Approved"})
            return self.orders[orderId]
        elif newStatus == 2:
            self.orders[orderId].update({"Status": "Denied"})
            return self.orders[orderId]
        else:
            return {"Error": "No status change has been made"}


