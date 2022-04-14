from flask import Flask, make_response, render_template, url_for, request, redirect, flash
from flask import current_app as app
from sqlalchemy import null
from .forms import RestaurantForm
from .__init__ import *
from .models import *
from random import randint
import json
#import requests

receiptNum = 0

@app.route('/', methods = ['POST', 'GET'])
@app.route('/home')
@app.route('/index')
def index():
    #DEV
    #db.drop_all()
        # db.create_all()
        # db_init(db)
    
    rForm = RestaurantForm()
    global receiptNum
        

    if request.method == 'POST':
        managerExists = db.session.query(Manager.Validation_Code).filter_by(Validation_Code = rForm.restID.data).first() is not None
        if (managerExists):
            Customer.create(rForm.cName.data, int(rForm.tableNum.data), incrReceiptNum(), int(rForm.restID.data))
            return redirect(url_for('order_page'))
        else:
            flash("Invalid Restaurant ID")
        
        
        #url = 'http://localhost:5000/validate'
        #headers = {'Content-Type': 'application/json'}
        #params = {'RestaurantID':rForm.restID.data}
        #response = requests.get(url, headers = headers, data = params)
        #print(response.text)
        #if response.json() == "True":
        #    return render_template("appetizers.html", title="Boishii Mobile Menu | Appetizers")
        #else:
        #    return render_template('index.html', title="Boishii Mobile Menu | Home", form=rForm)
    return render_template('index.html', title="Boishii Mobile Menu | Home", form=rForm)

@app.route('/order', methods=["GET"])
@app.route('/Appetizers')
def order_page():
    appies = db.session.query(Menu_Item).filter_by(Category = "Appetizer").all()
    return render_template("order_page.html", title="Boishii Mobile Menu | Order", menu_items=appies)

@app.route('/Main_Courses', methods=["GET"])
def main_courses():
    mains = db.session.query(Menu_Item).filter_by(Category = "Main").all()
    return render_template("order_page.html", title="Boishii Mobile Menu | Main Courses", menu_items=mains)

@app.route('/Dessert', methods=["GET"])
def dessert():
    desserts = db.session.query(Menu_Item).filter_by(Category = "Dessert").all()
    return render_template("order_page.html", title="Boishii Mobile Menu | Dessert", menu_items=desserts)

@app.route('/Drinks', methods=["GET"])
def drinks():
    drinks = db.session.query(Menu_Item).filter_by(Category = "Drink").all()
    return render_template("order_page.html", title="Boishii Mobile Menu | Drinks", menu_items=drinks)



#API to verify restaurantID
# A json body will be received that will look something like 
# {
#      "RestaurantID": 1234
# }
@app.route('/validate', methods=["POST"])
def validate():
    content = request.get_json()
    managerExists = db.session.query(Manager.Validation_Code).filter_by(Validation_Code = content["RestaurantID"]).first() is not None
    print(managerExists)
    if (managerExists == False):
        return "False"
    Customer.create(content["Name"], int(content["TableNum"]), incrReceiptNum(), int(content["RestaurantID"]))
    return "True"

def incrReceiptNum():
    global receiptNum
    receiptNum += 1
    return receiptNum

#API to retieve menu items from database
# Example input: 
# {
#      "Name": "Pizza"
# }
@app.route('/getItem', methods = ["POST"])
def getItem():
   
    content = request.get_json()
    try:
        menuItem = db.session.query(Menu_Item).filter_by(Name = content["Name"]).first() # how does the api get the name of which tuple to retieve

        #print(menuItem.Name)
        dict = {"Name" : menuItem.Name,
                "Description" : menuItem.Description, 
                "Image": menuItem.Image, 
                "Price": menuItem.Price
                
                }
        return dict
    except:
        return "-1"



#API to add menu items to an Order
# Example input: 
# {
#   "Quantity" : 3
#   "OrderNum" : 123   
#   "Name": "Pizza"
# }
@app.route('/addItem', methods = ["POST"])
def addItemToOrder():
    try:
        content = request.get_json()
        item = Order_Item(OrderNum = content["OrderNum"], Item = content["Name"], Quantity = content["Quantity"])
        db.session.add(item)
        db.session.commit()

        print("added " ,content["Name"], "to Order Number" , content["OrderNum"])
        return "Successfully Added Item"
    except:
        return "-1"
   


#API to remove menu items to an Order
# A json body will be received that will look something like 
# {
#   "OrderNum" : 123   
#   "Name": "Pizza"
# }
@app.route('/removeItem', methods = ["DELETE"])
def removeItemToOrder():
   
    content = request.get_json()
    try:  
        item = db.session.query(Order_Item).filter_by(Item = content["Name"], OrderNum = content["OrderNum"]).first()
        db.session.delete(item)
        db.session.commit()

        print("removed ", content["Name"] , " from Order Number " , content["OrderNum"])
        return "Successfully removed Item"
   
    except:
        return "-1" #if cannot remove item return -1






#API to create the order
# Example input: 
# {
#   "OrderNum" : 123   
#   "RecieptNum": 345
#   "TableNum" : 2
# }
@app.route('/createOrder', methods = ["POST"])
def createOrder():

    content = request.get_json()
    ord = Order_Receipt(OrderNum = content["OrderNum"], ReceiptNum = receiptNum, TableNum = content["TableNum"])
    try:
        db.session.add(ord)
        db.session.commit()
        return "Successfully created Order"
    except:
        return "-1"
    



#API delete order from order Database
# Example input: 
# {
#   "OrderNum" : 123   
# }
@app.route('/deleteOrder', methods = ["DELETE"])
def deleteOrder():

    content = request.get_json()

    try: # remove all items in Order_Item with the input ordernumber 
        items = db.session.query(Order_Item).filter_by(OrderNum = content["OrderNum"]).all() 

        print(items)
        for i in items :
            db.session.delete(i)

        db.session.commit()

        #remove order from Order Reciept
        ord = db.session.query(Order_Receipt).filter_by(OrderNum = content["OrderNum"]).first() # how does the api get the name of which tuple to retieve


        db.session.delete(ord)
        db.session.commit()

        return "Successfully deleted Order"
    except:
        return "-1"  #if cannot remove order return -1



#API get Order from the database
# Example input: 
# {
#   "OrderNum" : 123   
# }

# Example return
# {
#     "Steak" : 1
#     "Nachos" : 4
# }
@app.route('/getOrder', methods = ["GET"])
def getOrder():

    content = request.get_json()

    try: # remove all items in Order_Item with the input ordernumber 
        items = db.session.query(Order_Item).filter_by(OrderNum = content["OrderNum"]).all() 

        dict = {}

        print(items)
        for i in range(len(items)):

            dict[items[i].Item] = items[i].Quantity

    
        return dict   #if dict is notempty then return the dict otherwise return -1
        
        
    except:
        return "-1" #if error then return -1



#API get Order from the database
# Example input: 
# {
#   "OrderNum" : 123 
#   "Name"     : Steak
#   "Quantity" : 5  
# }
@app.route('/changeOrder', methods = ["GET"])
def changeOrder():

    content = request.get_json()

    try: # remove all items in Order_Item with the input ordernumber 
        item = db.session.query(Order_Item).filter_by(OrderNum = content["OrderNum"],Item = content["Name"]).first() 

        item.Quantity = content["Quantity"]
    
        db.session.commit()
    
        return "Successfully changed quantity"   #if dict is notempty then return the dict otherwise return -1
        
        
    except:
        return "-1" #if order or item does not exist then return -1















def db_init(db):

    #ADDING MANAGERS

    manager1 = Manager(EmployeeID = 1 ,First_Name = "Austin", Last_Name = "Ficzere" ,Validation_Code= 67890 )

    db.session.add(manager1)
    db.session.commit()

    manager2 = Manager(EmployeeID = 2,First_Name = "Josh", Last_Name = "Cordeiro-Zebkowitz",Validation_Code= 12345 )

    db.session.add(manager2)


    manager3 = Manager(EmployeeID = 3,First_Name = "Anay", Last_Name = "Bhutoria",Validation_Code= 34889 )

    db.session.add(manager3)

    db.session.commit()
    #ADDING Cooks

    cooks1 = Cook(First_Name = "Ahmed", Last_Name = "Al Marouf", EmployeeID = 4, Position = "sous chef", ManagerID = 1 )
    db.session.add(cooks1)

    cooks2 = Cook(First_Name = "Moein", Last_Name = "Mirzaei", EmployeeID = 5, Position = "sous chef", ManagerID = 2 )
    db.session.add(cooks2)

    cooks3 = Cook(First_Name = "Eric", Last_Name = "Wang", EmployeeID = 6, Position = "sous chef", ManagerID = 3 )
    db.session.add(cooks3)

    db.session.commit()
    #Adding Tables

    Table1 = Table(TableNum = 1, WaiterID = None)
    db.session.add(Table1)
    Table2 = Table(TableNum = 2, WaiterID = None)
    db.session.add(Table2)
    Table3 = Table(TableNum = 3, WaiterID = None)
    db.session.add(Table3)

    #Adding Waiter


    Waiter1 = Waiter(EmployeeID = 7, First_Name = "Mana", Last_Name = "Kim", ManagerID = 1)
    db.session.add(Waiter1)
    Waiter2 = Waiter(EmployeeID = 8, First_Name = "Kashfia ", Last_Name = "Sailunaz ", ManagerID = 2)
    db.session.add(Waiter2)
    Waiter3 = Waiter(EmployeeID = 9, First_Name = "Wayne", Last_Name = "Eberly", ManagerID = 3)
    db.session.add(Waiter3)
    #adding items to menu_items  
    



    
    #template = Menu_Item(Name = "", Description ="", Image =".png",Price = 12.99)
    #db.session.add(template)

    #Appetizers

    nachos = Menu_Item(Name = "Nachos", Description = "Beef nachos with jalapenos, tomotoes, and onions. Sour cream and salsa on the side.", Image ="nachos.png", Price = 5.99, Category = "Appetizer")
    db.session.add(nachos)
    
    chickenWings = Menu_Item(Name = "Chicken Wings", Description = "BBQ bone-in chicken wings. Comes with ranch and celery!", Image ="chickenwings.png",Price = 7.99 ,Category = "Appetizer")
    db.session.add(chickenWings)
    
    calamari = Menu_Item(Name = "Calamari", Description ="A massive mound of crsipy calamari!", Image ="calamari.png",Price = 12.99,Category = "Appetizer")
    db.session.add(calamari)
    
    olives = Menu_Item(Name = "Olives", Description ="Some salty olives to keep you satisfied while you wait.", Image ="olives.png",Price = 2.99,Category = "Appetizer")
    db.session.add(olives)
    
    sushi = Menu_Item(Name = "Sushi", Description ="A sushi platter with everything you would ever desire!", Image ="sushi.png",Price = 17.99,Category = "Appetizer")
    db.session.add(sushi)

    burger = Menu_Item(Name = "Burger", Description ="A BBQ burger with onion rings!", Image ="burger.png",Price = 8.99,Category = "Appetizer")
    db.session.add(burger)

    db.session.commit()
    #Main Course

    #pho

    pho = Menu_Item(Name = "Pho", Description ="Its pho, you just cant miss, just buy it already", Image ="pho.jpg",Price = 10.99,Category = "Main")
    db.session.add(pho)



    #Pizza
    pizza = Menu_Item(Name = "Pizza", Description ="Its italian pizza ", Image ="pizza.jpg",Price = 16.99,Category = "Main")
    db.session.add(pizza)


    #Butter Chicken
    butterChicken = Menu_Item(Name = "Butter Chicken", Description ="spicy food", Image ="butter-chicken.jpg",Price = 13.99,Category = "Main")
    db.session.add(butterChicken)

    #Garlic Naan

    garlicNaan = Menu_Item(Name = "Garlic Naan", Description ="indian bread", Image ="garlicNaan.jpg",Price = 12.99,Category = "Main")
    db.session.add(garlicNaan)

    #Biranyi 


    biryani = Menu_Item(Name = "Biryani", Description ="indian rice", Image ="biryani.jpeg",Price = 19.99,Category = "Main")
    db.session.add(biryani)

    #Steak

    steak = Menu_Item(Name = "Steak", Description ="MEAT", Image ="steak.jpg",Price = 43.99,Category = "Main")
    db.session.add(steak)
    
    
    # Unfortuantely Fish and chips 

    fishChips = Menu_Item(Name = "Fish and Chips", Description ="fish with fries", Image ="fishNChips.jpg",Price = 25.99,Category = "Main")
    db.session.add(fishChips)

    # Shawarma 

    shawarma = Menu_Item(Name = "Chicken Shawarma", Description ="the best wrap you will ever eat, buy it", Image ="chickenShawarma.jpg",Price = 12.99,Category = "Main")
    db.session.add(shawarma)


    db.session.commit()
    #Dessert
    
    chocolateCake = Menu_Item(Name = "Chocolate Cake", Description ="Cake, just eat it", Image ="chocoCake.jpg",Price = 12.99,Category = "Dessert")
    db.session.add(chocolateCake)

    waffle = Menu_Item(Name = "Waffles", Description ="Waffles with fruit", Image ="waffle.jpg",Price = 16.99,Category = "Dessert")
    db.session.add(waffle)


    crepe = Menu_Item(Name = "Crepes", Description ="Crepes with fruit", Image ="crepe.jpg",Price = 17.99,Category = "Dessert")
    db.session.add(crepe)

    fondue = Menu_Item(Name = "Fondue", Description ="Fondue with fruit", Image ="fondue.jpg",Price = 24.99,Category = "Dessert")
    db.session.add(fondue)

    db.session.commit()

    #Drinks

    coke = Menu_Item(Name = "Coca-Cola", Description ="it is a sweet liquid", Image="coke.jpg",Price = 2.99,Category = "Drink")
    db.session.add(coke)

    pepsi = Menu_Item(Name = "Pepsi", Description ="drink it", Image="pepsi.jpg",Price = 2.99,Category = "Drink")
    db.session.add(pepsi)

    guinness = Menu_Item(Name = "guinness", Description ="drink the head, feel the lead", Image="guinness.jpg",Price = 12.99,Category = "Drink")
    db.session.add(guinness)



    absinthe = Menu_Item(Name = "Absinthe", Description ="For the Bold", Image="absinthe.jpg",Price = 12.99,Category = "Drink")
    db.session.add(absinthe)


    db.session.commit()

    return

