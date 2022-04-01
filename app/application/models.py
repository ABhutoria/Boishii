from __init__ import db
from datetime import datetime

#Manager Table
class Manager(db.Model): # fooditem inherits db.Mod__init__l

    __tablename__ = 'Manager'

    EmployeeID = db.Column(db.Integer, primary_key= True)

    First_Name = db.Column(db.String(50), nullable = False)
    
    Last_Name = db.Column(db.String(50), nullable = False)
    
    Validation_Code = db.Column(db.Integer,nullable = False)

    def __repr__(self):

       #f allows to print  variable inside the curly for simplicity
        return f"Manager('{self.employeeID}','{self.first_Name}', '{self.last_Name}','{self.validation_Code}')" 


#Waiter Table
class Waiter(db.Model): # fooditem inherits db.Model

    __tablename__ = 'Waiter'

    EmployeeID = db.Column(db.Integer, primary_key= True)

    First_Name = db.Column(db.String(50), nullable = False)
    
    Last_Name = db.Column(db.String(50), nullable = False)
    
    #add ManagerID foreign key

    ManagerID = db.Column(db.Integer, db.ForeignKey('Manager.EmployeeID'),nullable = False)
    def __repr__(self):
    
        return f"Waiter('{self.employeeID}','{self.first_Name}', '{self.last_Name}')" #add ManagerID

#Cook Table
class Cook(db.Model): # fooditem inherits db.Model

    __tablename__ = 'Cook'

    EmployeeID = db.Column(db.Integer, primary_key= True)

    First_Name = db.Column(db.String(50), nullable = False)
    
    Last_Name = db.Column(db.String(50), nullable = False)
    
    Position = db.Column(db.String(50), nullable = False)


    #add ManagerID foreign key

    def __repr__(self):

        return f"Cook('{self.employeeID}','{self.first_Name}', '{self.last_Name}','{self.position}')" #add ManagerID



#Table Table
class Table(db.Model): # fooditem inherits db.Model

    __tablename__ = 'Table'

    TableNum = db.Column(db.Integer, primary_key= True)

    #WaiterID is a forign key
  

    def __repr__(self):
        return f"Cook('{self.employeeID}','{self.first_Name}', '{self.last_Name}','{self.position}')" #add foreignkey



#Order Table

class Order_Reciept(db.Model): # Order Reciept inherits db.Model

    __tablename__ = 'Order_Reciept'

    OrderNum = db.Column(db.Integer, primary_key= True)

    ReciptNum = db.Column(db.Integer, primary_key= True) # are there 2 primary keys??

    Total_Price = db.Column(db.Float, default = 0)

       #TableNum is a forign key


    def __repr__(self):
        return f"Order_Reciept('{self.id}','{self.name}', '{self.description}','{self.picture}')" #TableNum is a foreignKey


#Multivariable attribute, Special Request, in Order_Reciept
class Special_Requests(db.Model): # DishQueue inherits db.Model

    __tablename__ = 'Special_Requests'

    Request = db.Column(db.String(500), nullable = False, primary_key = True)


    # OrderNum should be a foreign key and primarykey


    def __repr__(self):
        return f"Special_Requests('{self.id}','{self.first_Name}', '{self.last_Name}')" # add OrderNum 




#Items attribute of Order
class Order_Item(db.Model): # DishQueue inherits db.Model

    __tablename__ = 'Order_Item'

    Item = db.Column(db.String(500), nullable = False, primary_key = True)


    Quantity = db.Column(db.Integer, nullable = False, default = 1)

    # OrderNum should be a foreign key and primarykey
    OrderNum = db.Column(db.Integer, db.ForeignKey('Order_Reciept.OrderNum'), primary_key = True)

    def __repr__(self):
        return f"Order_Item('{self.id}','{self.first_Name}', '{self.la}',  '{self.OrderNum}')" # add OrderNum 





#Menu_Items is a table that contain ALL items to select from
class Menu_Item(db.Model): # fooditem inherits db.Model

    __tablename__ = 'Menu_Items'

    Name = db.Column(db.String(50), nullable = False, primary_key = True)

    Description = db.Column(db.String(200), nullable = False)

    Image = db.Column(db.String(20), default = "default.jpg")

    Price = db.Column(db.Integer, nullable = False)
    
    

    def __repr__(self):
        return f"Menu_Item('{self.id}','{self.name}', '{self.description}','{self.picture}')"



#Customer table which stores customer info
class Customer(db.Model): # Customer inherits db.Model

    __tablename__ = 'Customer'

    First_Name = db.Column(db.String(50), nullable = False) 
    Last_Name = db.Column(db.String(50), nullable = False)

    TableNum = db.Column(db.Integer, db.ForeignKey('Table.TableNum'),primary_key = True)
    
    TableNum = db.Column(db.Integer, db.ForeignKey('Order_Reciept.RecieptNum'), primary_key = True)
    #TableNumber should be a foreign key and primarykey
    # RecieptNum foreign key and primarykey

    def __repr__(self):
        return f"Menu_Item('{self.id}','{self.first_Name}', '{self.last_Name}')" # add TableNum and recieptNum






#Dish queue which stores the queue the kitchen has to cook the dishes
class DishQueue(db.Model): # DishQueue inherits db.Model

    __tablename__ = 'DishQueue'

    Dish = db.Column(db.String(50), nullable = False, primary_key = True)

    PositionInQueue = db.Column(db.Integer, nullable = False)


    # CookID should be a foreign key
    # RecieptNum foreign key

    def __repr__(self):
        return f"Menu_Item('{self.id}','{self.first_Name}', '{self.last_Name}')" # add CookID and recieptNum





