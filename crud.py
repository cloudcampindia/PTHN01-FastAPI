import models
from sqlalchemy.orm import Session

def read_suppliers(db: Session):
    return db.query(models.SuppliersData).all()

"""
{
  "OrderID": 10248,
  "CustomerID": 90,
  "EmployeeID": 5,
  "OrderDate": "1996-07-04T00:00:00",
  "ShipperID": 3
}
"""

def get_order(db: Session, order_id: int=10248):
    orders_data = {}
    data = db.query(models.OrdersData).filter(models.OrdersData.OrderID == order_id).first()
    orders_data["OrderID"] = data.OrderID
    orders_data["EmployeeName"] = data.orders_employees.FirstName + ' ' + data.orders_employees.LastName
    orders_data["CustomerName"] = data.orders_customers.CustomerName
    orders_data["OrderDate"] = data.OrderDate
    orders_data["ShipperName"] = data.orders_shippers.ShipperName

    products_list = [od.order_details_products.ProductName for od in data.orders_order_details]
    price_details = [od.order_details_products.Price for od in data.orders_order_details]
    quantity_details = [od.Quantity for od in data.orders_order_details]
    
    total_price = 0
    for p, q in zip(price_details, quantity_details):
        total_price += (p * q)

    orders_data["orderDetails"] = {"products": products_list, "totalPrice": total_price}

    return orders_data