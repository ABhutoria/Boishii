from .__init__ import db
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
        return f"Manager('{self.EmployeeID}','{self.First_Name}', '{self.Last_Name}','{self.Validation_Code}')" 


#Waiter Table
class Waiter(db.Model): # fooditem inherits db.Model

    __tablename__ = 'Waiter'

    EmployeeID = db.Column(db.Integer, primary_key= True)

    First_Name = db.Column(db.String(50), nullable = False)
    
    Last_Name = db.Column(db.String(50), nullable = False)
    
    ManagerID = db.Column(db.Integer, db.ForeignKey('Manager.EmployeeID'),nullable = False)
    
    
    
    def __repr__(self):
    
        return f"Waiter('{self.EmployeeID}','{self.First_Name}', '{self.Last_Name}', '{self.ManagerID}')"


        
#Cook Table
class Cook(db.Model): # fooditem inherits db.Model

    __tablename__ = 'Cook'

    First_Name = db.Column(db.String(50), nullable = False)
    
    Last_Name = db.Column(db.String(50), nullable = False)
    
    EmployeeID = db.Column(db.Integer, primary_key= True)

    Position = db.Column(db.String(50), nullable = False)

    ManagerID = db.Column(db.Integer,db.ForeignKey('Manager.EmployeeID') , nullable = False)
  

    def __repr__(self):

        return f"Cook('{self.EmployeeID}','{self.First_Name}', '{self.Last_Name}','{self.Position}','{self.ManagerID}')" #add ManagerID



#Table Table
class Table(db.Model): # Table inherits db.Model

    __tablename__ = 'Table'

    TableNum = db.Column(db.Integer, primary_key= True)

  
    WaiterID = db.Column(db.Integer, db.ForeignKey('Waiter.EmployeeID'))

    def __repr__(self):
        return f"Table('{self.TableNum}','{self.WaiterID}')"



#Order Table

class Order_Receipt(db.Model): # Order Receipt inherits db.Model

    __tablename__ = 'Order_Receipt'

    OrderNum = db.Column(db.Integer, primary_key= True )

    ReceiptNum = db.Column(db.Integer, primary_key= True) # are there 2 primary keys??

    Total_Price = db.Column(db.Float, default = 0)

    TableNum = db.Column(db.Integer, db.ForeignKey('Table.TableNum'))

    def __init__(self, orderNum: int, receiptNum: int, totalPrice: float, tableNum: int):
       self.OrderNum = orderNum
       self.TableNum = tableNum
       self.ReceiptNum = receiptNum
       self.Total_Price = totalPrice

    @staticmethod
    def create(orderNum, receiptNum, totalPrice, tableNum):
       newO = Order_Receipt(orderNum, receiptNum, totalPrice, tableNum)
       db.session.add(newO)
       db.session.commit()

    def __repr__(self):
        return f"Order_Receipt('{self.OrderNum}','{self.ReceiptNum}','{self.Total_Price}', '{self.TableNum})" #TableNum is a foreignKey


#Multivariable attribute, Special Request, in Order_Receipt
class Special_Requests(db.Model): # Special_Request inherits db.Model

    __tablename__ = 'Special_Requests'

    Request = db.Column(db.String(500), nullable = False, primary_key = True)

    OrderNum = db.Column(db.Integer, db.ForeignKey('Order_Receipt.OrderNum'))

    def __repr__(self):
        return f"Special_Requests('{self.Request}','{self.OrderNum}')" # add OrderNum 




#Items attribute of Order
class Order_Item(db.Model): # Order_Item inherits db.Model

    __tablename__ = 'Order_Item'


    Item = db.Column(db.String(500),db.ForeignKey('Menu_Item.Name'),primary_key = True, nullable = False)


    Quantity = db.Column(db.Integer, nullable = False, default = 1)

    
    OrderNum = db.Column(db.Integer, db.ForeignKey('Order_Receipt.OrderNum'), primary_key = True)

    def __repr__(self):
        return f"Order_Item('{self.Item}','{self.Quantity}','{self.OrderNum}')" # add OrderNum 





#Menu_Items is a table that contain ALL items to select from
class Menu_Item(db.Model): # Menu_Item inherits db.Model

    __tablename__ = 'Menu_Item'

    Name = db.Column(db.String(50), nullable = False, primary_key = True)

    Description = db.Column(db.String(200), nullable = False)

    Image = db.Column(db.String(20), default = "default.jpg")

    Price = db.Column(db.Float, nullable = False)
    
    Category = db.Column(db.String(200), nullable = False)

    def __repr__(self):
        return f"Menu_Item('{self.Name}','{self.Description}', '{self.Image}','{self.Price}')"



#Customer table which stores customer info
class Customer(db.Model): # Customer inherits db.Model

    __tablename__ = 'Customer'

    Name = db.Column(db.String(90), nullable = False, primary_key = True) 
   # Last_Name = db.Column(db.String(50), nullable = False)

    TableNum = db.Column(db.Integer, db.ForeignKey('Table.TableNum'))
    
    ReceiptNum = db.Column(db.Integer, db.ForeignKey('Order_Receipt.ReceiptNum'))
    RestaurantID = db.Column(db.Integer)

    def __init__(self, name: str, tableNum: int, receiptNum: int, restaurantID: int):
       self.Name = name
       self.TableNum = tableNum
       self.ReceiptNum = receiptNum
       self.RestaurantID = restaurantID

    @staticmethod
    def create(name, tableNum, receiptNum, restaurantID):
       newC = Customer(name, tableNum, receiptNum, restaurantID)
       db.session.add(newC)
       db.session.commit()

    def __repr__(self):
       return f"Customer('{self.Name}', '{self.TableNum}','{self.ReceiptNum}''{self.RestaurantID}')" 






#Dish queue which stores the queue the kitchen has to cook the dishes
class DishQueue(db.Model): # DishQueue inherits db.Model

    __tablename__ = 'DishQueue'

    Dish = db.Column(db.String(50), nullable = False, primary_key = True)

    PositionInQueue = db.Column(db.Integer, nullable = False)

    CookID =  db.Column(db.Integer, db.ForeignKey('Cook.EmployeeID'))
    ReceiptNum = db.Column(db.Integer, db.ForeignKey('Order_Receipt.ReceiptNum'))
   

    def __repr__(self):
        return f"DishQueue('{self.Dish}','{self.PositionInQueue}','{self.CookID}','{self.ReceiptNum}')" # add CookID and receiptNum





