#run by 'python3 -i anay-dev.py'
from .models import *
from .__init__ import *

app = init_app()

ctx = app.app_context()
ctx.push()






