from flask import Flask, make_response, render_template, url_for, request, redirect
from flask import current_app as app
from sqlalchemy import null
from .forms import RestaurantForm
from .__init__ import *
from .models import *
from random import randint
import json

@app.route('/', methods = ['POST', 'GET'])
@app.route('/home')
@app.route('/index')
def index():
    db_init(db)
    #db.create_all()
    rForm = RestaurantForm()
    if request.method == 'POST':
        Customer.create(rForm.cName.data, int(rForm.tableNum.data), randint(0, 200), int(rForm.restID.data))
        return make_response(redirect('/order'))
    return render_template('index.html', title="Boishii Mobile Menu | Home", form=rForm)




 #API to retieve menu items from database
@app.route('/getItems', methods = ["GET"])
def getItems():
   
    content = request.get_json()
    #print(content["Name"])
    #data = json.loads(content)
   # print(data)
    menuItem = db.session.query(Menu_Item).filter_by(Name = content["Name"]).first() # how does the api get the name of which tuple to retieve
    
    print(menuItem.Name)
    dict = {"Name" : menuItem.Name,
            "Description" : menuItem.Description, 
            "Image": menuItem.Image, 
            "Price": menuItem.Price
            }
    return dict



#input should be order number, Item name, Quantity


@app.route('/addItem', methods = ["POST"])
def addItemToOrder():
   
    content = request.get_json()
    item = Order_Item(OrderNum = content["OrderNum"], Item = content["Name"], Quantity = content["Quantity"])
    db.session.add(item)
    db.session.commit()

    print("added " + content["Name"]+ "to Order Number" + content["OrderNum"])
    return "Successfully Added Item"
   
   



@app.route('/removeItem', methods = ["POST"])
def removeItemToOrder():
   
    content = request.get_json()
    
    item = Order_Item(OrderNum = content["OrderNum"], Item = content["Name"], Quantity = content["Quantity"])
    db.session.delete(item)
    db.session.commit()

    print("removed ", content["Name"] , " to Order Number " , content["OrderNum"])
    return "Successfully removed Item"
   





# @app.route('/<EID>,<Fname>, <Lname>, <Vcode>')
# def create_manager(EID, Fname, Lname, Vcode):
#         manager = Manager(First_Name = Fname, Last_Name = Lname,EmployeeID = EID,Validation_Code= Vcode  )
#         db.session.add(manager)
#         db.session.commit()
#         Manager.query.all()
#         return "Created User!"


# @app.route('/<EID>&<Fname>&<Lname>&<Vcode>')
# def create_manager(EID, Fname, Lname, Vcode):
#         manager = Manager(First_Name = Fname, Last_Name = Lname,EmployeeID = EID,Validation_Code= Vcode  )
#         print("eid =" + EID + "fname = " + Fname + "lname = "+ Lname + "vcode = " +Vcode)
        
#         db.session.add(manager) 
#         db.session.commit()
#      #   Manager.query.all()
#         return "Created User!"

# @app.route('/?cust_name=<Cname>&table_num=<tnum>&restaurant_id=<rID>')
# def create_customer(Cname, tnum, rID):
#         cust = Customer(Name = Cname, TableNum = tnum,ResturantID = rID)
#         print("name =" + Cname + "fname = " + tnum + "lname = "+ rID)
#         db.session.add(cust)
#         db.session.commit()
#         #Manager.query.all()
#         return "Created User!"

# @app.route('/?cust_name=<name>&table_num=<tnum>&restaurant_id=<rID>')
# def create_customer(name,tnum,rID):
#         # cust = Customer(Name = name, TableNum = tnum,ResturantID = rID)
#         # db.session.add(cust)
#         # db.session.commit()
        
#         return "Created User!"



# @app.route('/<EID>&<Fname>&<Lname>&<Vcode>')
# def create_manager(EID, Fname, Lname, Vcode):
#         manager = Manager(First_Name = Fname, Last_Name = Lname,EmployeeID = EID,Validation_Code= Vcode  )
#         db.session.add(manager)
#         db.session.commit()
#         Manager.query.all()
#         return "Created User!"



# @app.route('/<name>,<age>')
# def create_manager(name,age):
   
#         return f"Created User : name: {name} + age: {age}!"




def db_init(db):

    #ADDING MANAGERS

    manager = Manager(First_Name = "Austin", Last_Name = "Ficzere" ,EmployeeID = 123,Validation_Code= 67890 )

    db.session.add(manager)

    manager1 = Manager(First_Name = "Josh", Last_Name = "Cordeiro-Zebkowitz",EmployeeID = 9,Validation_Code= 12345 )

    db.session.add(manager1)


    manager2 = Manager(First_Name = "Anay", Last_Name = "Bhutoria",EmployeeID = 1,Validation_Code= 34889 )

    db.session.add(manager2)


    #ADDING Cooks

    cooks1 = Cook(First_Name = "Ahmed", Last_Name = "Al Marouf", EmployeeID = "122", Postion = "sous chef", ManagerID = 67890 )
    db.session.add(cooks1)

    cooks2 = Cook(First_Name = "Moein ", Last_Name = "Mirzaei", EmployeeID = "152", Postion = "sous chef", ManagerID = 67890 )
    db.session.add(cooks2)

    cooks3 = Cook(First_Name = "Eric  ", Last_Name = "Wang", EmployeeID = "172", Postion = "sous chef", ManagerID = 67890 )
    db.session.add(cooks3)

    #Adding Tables

    Table1 = Table(TableNum = 1, WaiterID = None)
    Table2 = Table(TableNum = 2, WaiterID = None)
    Table3 = Table(TableNum = 3, WaiterID = None)



    
    #adding items to menu_items  
    
    
    #template = Menu_Item(Name = "", Description ="", Image =".png",Price = 12.99)
    #db.session.add(template)

    #Appetizers

    nachos = Menu_Item(Name = "Nachos", Description = "Beef nachos with jalapenos, tomotoes, and onions. Sour cream and salsa on the side.", Image ="nachos.png",Price = 5.99)
    db.session.add(nachos)
    
    chickenWings = Menu_Item(Name = "Chicken Wings", Description = "BBQ bone-in chicken wings. Comes with ranch and celery!", Image ="chickenwings.png",Price = 7.99)
    db.session.add(chickenWings)
    
    calamari = Menu_Item(Name = "Calamari", Description ="A massive mound of crsipy calamari!", Image ="calamari.png",Price = 12.99)
    db.session.add(calamari)
    
    olives = Menu_Item(Name = "Olives", Description ="Some salty olives to keep you satisfied while you wait.", Image ="olives.png",Price = 2.99)
    db.session.add(olives)
    
    sushi = Menu_Item(Name = "Sushi", Description ="A sushi platter with everything you would ever desire!", Image ="sushi.png",Price = 17.99)
    db.session.add(sushi)

    burger = Menu_Item(Name = "Burger", Description ="A BBQ burger with onion rings!", Image ="burger.png",Price = 8.99)
    db.session.add(burger)


    #Main Course

    #pho

    pho = Menu_Item(Name = "Pho", Description ="Its pho, you just cant miss, just buy it already", Image ="pho.jpeg",Price = 10.99)
    db.session.add(pho)



    #Pizza
    pizza = Menu_Item(Name = "Pizza", Description ="Its italian pizza ", Image ="pizza.jpeg",Price = 16.99)
    db.session.add(pizza)


    #Butter Chicken

    butterChicken = Menu_Item(Name = "Butter Chicken", Description ="spicy food", Image ="butter-chicken.jpeg",Price = 13.99)
    db.session.add(butterChicken)

    #Garlic Naan

    garlicNaan = Menu_Item(Name = "Garlic Naan", Description ="indian bread", Image ="garlicNaan.jpeg",Price = 12.99)
    db.session.add(garlicNaan)

    #Biranyi 

    biryani = Menu_Item(Name = "Biryani", Description ="indian rice", Image ="briyani.jpeg",Price = 19.99)
    db.session.add(biryani)

    #Steak

    steak = Menu_Item(Name = "Steak", Description ="MEAT", Image ="briyani.jpeg",Price = 43.99)
    db.session.add(steak)
    
    
    # Unfortuantely Fish and chips 

    fishChips = Menu_Item(Name = "Fish and Chips", Description ="fish with fries", Image ="fishNChips.jpeg",Price = 25.99)
    db.session.add(fishChips)

    # Shawarma 

    shawarma = Menu_Item(Name = "Chicken Shawarma", Description ="the best wrap you will ever eat, buy it", Image ="chickenShawarma.jpeg",Price = 12.99)
    db.session.add(shawarma)



    #Dessert
    
    chocolateCake = Menu_Item(Name = "Chocolate Cake", Description ="Cake, just eat it", Image ="chocoCake.jpeg",Price = 12.99)
    db.session.add(chocolateCake)

    waffle = Menu_Item(Name = "Waffles", Description ="Waffles with fruit", Image ="waffle.jpeg",Price = 16.99)
    db.session.add(waffle)


    crepe = Menu_Item(Name = "Crepes", Description ="Crepes with fruit", Image ="crepe.jpeg",Price = 17.99)
    db.session.add(crepe)

    fondue = Menu_Item(Name = "Fondue", Description ="Fondue with fruit", Image ="fondue.jpeg",Price = 24.99)
    db.session.add(fondue)

    

    #Drinks

    coke = Menu_Item(Name = "Coca-Cola", Description ="it is a sweet liquid", Image="coke.jpeg",Price = 2.99)
    db.session.add(coke)

    pepsi = Menu_Item(Name = "Pepsi", Description ="drink it", Image="pepsi.jpeg",Price = 2.99)
    db.session.add(pepsi)

    guinness = Menu_Item(Name = "guinness", Description ="drink the head, feel the lead", Image="guinness.jpeg",Price = 12.99)
    db.session.add(guinness)



    absinthe = Menu_Item(Name = "Absinthe", Description ="For the Bold", Image="absinthe.jpeg",Price = 12.99)
    db.session.add(absinthe)


    db.session.commit()

    return

