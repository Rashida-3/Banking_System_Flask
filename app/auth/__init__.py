from flask import Blueprint


auth_bp = Blueprint('auth',__name__)
index_bp = Blueprint('index',__name__)

from app.auth.controllers import login
from app.auth.controllers import logout
from app.auth.controllers import signup

from app.auth.controllers import base