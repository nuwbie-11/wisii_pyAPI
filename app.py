from flask import Flask, render_template
import joblib
import numpy as np
from routes.route import user_bp

app = Flask(__name__)
app.register_blueprint(user_bp, url_prefix='/')


if __name__ == '__main__':
    app.run(port=5000, debug=True)