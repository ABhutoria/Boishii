from flask import Blueprint
from .__init__ import db
from .models import *



api = Blueprint('api',__name__)


# @api.route('/home/<EID>,<Fname>, <Lname>, <Vcode>')
# def create_manager(EID, Fname, Lname, Vcode):
#         manager = Manager(First_Name = Fname, Last_Name = Lname,EmployeeID = EID,Validation_Code= Vcode  )
#         db.session.add(manager)
#         db.session.commit()
#         return {"Created User!"}