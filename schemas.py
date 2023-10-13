from pydantic import BaseModel
from datetime import datetime, date

class CategoriesData(BaseModel):
    CategoryID: int
    CategoryName: str
    Description: str

    class Config:
        from_attributes = True


class CustomersData(BaseModel):
    CustomerID: int
    CustomerName: str
    ContactName: str
    Address: str
    City: str
    PostalCode: str
    Country: str

    class Config:
        from_attributes = True

class EmployeesData(BaseModel):
    EmployeeID: int
    LastName: str
    FirstName: str
    BirthDate: date
    Photo: str
    Notes: str

    class Config:
        from_attributes = True

class OrderDetailsData(BaseModel):
    OrderDetailID: int
    OrderID: int
    ProductID: int
    Quantity: int
    
    class Config:
        from_attributes = True

class OrdersData(BaseModel):
    OrderID: int
    CustomerID: int
    EmployeeID: int
    OrderDate: datetime
    ShipperID: int

    class Config:
        from_attributes = True

class ProductsData(BaseModel):
    ProductID: int
    ProductName: str
    SupplierID: int
    CategoryID: int
    Unit: str
    Price: int

    class Config:
        from_attributes = True

class ShippersData(BaseModel):
    ShipperID: int
    ShipperName: str
    Phone: str

    class Config:
        from_attributes = True

class SuppliersData(BaseModel):
    SupplierID: int
    SupplierName: str
    ContactName: str
    Address: str
    City: str
    PostalCode: str
    Country: str
    Phone: str

    class Config:
        from_attributes = True