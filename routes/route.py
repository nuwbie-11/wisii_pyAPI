from flask import Blueprint
from controllers.main import *


user_bp = Blueprint('user_bp', __name__)
user_bp.route('/predict', methods=['POST'])(predict)
# user_bp.route('/about', methods=['GET'])(about)