from sqlalchemy import (Boolean, Column, Date, DateTime, Float, ForeignKey,
                        Integer, String, Text)
from sqlalchemy.orm import relationship

from database import Base


class CategoriesData(Base):
    __tablename__ = "Categories"

    CategoryID = Column(Integer, primary_key=True)
    CategoryName = Column(Text)
    Description = Column(Text)

    categories_products = relationship("ProductsData", back_populates="products_categories")

class CustomersData(Base):
    __tablename__ = "Customers"
    
    CustomerID = Column(Integer, primary_key=True)
    CustomerName = Column(Text)
    ContactName = Column(Text)
    Address = Column(Text)
    City = Column(Text)
    PostalCode = Column(Text)
    Country = Column(Text)

    customers_orders = relationship("OrdersData", back_populates="orders_customers")

class EmployeesData(Base):
    __tablename__ = "Employees"

    EmployeeID = Column(Integer, primary_key=True)
    LastName = Column(Text)
    FirstName = Column(Text)
    BirthDate = Column(Date)
    Photo = Column(Text)
    Notes = Column(Text)

    employees_orders = relationship("OrdersData", back_populates="orders_employees")

class OrderDetailsData(Base):
    __tablename__ = "OrderDetails"

    OrderDetailID = Column(Integer, primary_key=True)
    OrderID = Column(Integer, ForeignKey("Orders.OrderID"))
    ProductID = Column(Integer, ForeignKey("Products.ProductID"))
    Quantity = Column(Integer)
    
    order_details_orders = relationship("OrdersData", back_populates="orders_order_details")
    order_details_products = relationship("ProductsData", back_populates="products_order_details")

class OrdersData(Base):
    __tablename__ = "Orders"

    OrderID = Column(Integer, primary_key=True)
    CustomerID = Column(Integer, ForeignKey("Customers.CustomerID"))
    EmployeeID = Column(Integer, ForeignKey("Employees.EmployeeID"))
    OrderDate = Column(DateTime)
    ShipperID  = Column(Integer, ForeignKey("Shippers.ShipperID"))

    orders_order_details = relationship("OrderDetailsData", back_populates="order_details_orders")
    orders_customers = relationship("CustomersData", back_populates="customers_orders")
    orders_employees = relationship("EmployeesData", back_populates="employees_orders")
    orders_shippers = relationship("ShippersData", back_populates="shippers_orders")

class ProductsData(Base):
    __tablename__ = "Products"

    ProductID = Column(Integer, primary_key=True)
    ProductName = Column(Text)
    SupplierID = Column(Integer, ForeignKey("Suppliers.SupplierID"))
    CategoryID = Column(Integer, ForeignKey("Categories.CategoryID"))
    Unit = Column(Text)
    Price = Column(Integer, default=0)

    products_categories = relationship("CategoriesData", back_populates="categories_products")
    products_suppliers = relationship("SuppliersData", back_populates="suppliers_products")
    products_order_details = relationship("OrderDetailsData", back_populates="order_details_products")

class ShippersData(Base):
    __tablename__ = "Shippers"

    ShipperID = Column(Integer, primary_key=True)
    ShipperName = Column(Text)
    Phone = Column(Text)

    shippers_orders = relationship("OrdersData", back_populates="orders_shippers")

class SuppliersData(Base):
    __tablename__ = "Suppliers"

    SupplierID = Column(Integer, primary_key=True)
    SupplierName = Column(Text)
    ContactName = Column(Text)
    Address = Column(Text)
    City = Column(Text)
    PostalCode = Column(Text)
    Country = Column(Text)
    Phone = Column(Text)

    suppliers_products = relationship("ProductsData", back_populates="products_suppliers")