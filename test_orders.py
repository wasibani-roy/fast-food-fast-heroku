import unittest
import resources
from models import *
from app import app
class testOrders(unittest.TestCase):
    def setUp(self):
        self.test_data = {"product": "chicken", "quantity": "1", "price": "12000"}
        self.test_data_update = {"product": "chicken", "quantity": "1", "price": "12000", "Status":"Approved"}
        self.test_data_update_deny = {"product": "chicken", "quantity": "1", "price": "12000", "Status": "Denied"}
        self.testModal = order()
        self.testModal.orders = {1: {"product": "chicken", "quantity": "1", "price": "12000"}}

    def test_API_Make_Order(self):
        self.assertEqual(self.testModal.makeOrder(self.test_data), self.test_data)

    def test_API_Get_All_Orders(self):
        orderValue = self.testModal.listOrders()
        self.assertEqual(orderValue["status_code"], 200)
        self.assertEqual(orderValue["order_details"], self.testModal.orders)

    def test_API_get_specific_order(self):
        self.assertEqual(self.testModal.specificOrder(1), self.test_data)

    def test_API_update_specific_order_approved(self):
        self.assertEqual(self.testModal.updateOrder(1,1), self.test_data_update)

    def test_API_update_specific_order_denied(self):
        self.assertEqual(self.testModal.updateOrder(1,2), self.test_data_update_deny)


if __name__ == '__main__':
        unittest.main()


