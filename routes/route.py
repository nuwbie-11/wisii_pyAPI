from flask import Blueprint
from controllers.main import *


user_bp = Blueprint('user_bp', __name__)
user_bp.route('/get', methods=['POST'])(get)
# user_bp.route('/about', methods=['GET'])(about)