import werkzeug
from flask import render_template, request, jsonify
import numpy as np



def predict():
    if request.method == 'POST':

        # data = request.get_json(force=True)
        # image_data = data['image']
        # imgdata = base64.b64decode(image_data)
        img_file = request.files['images']
        # filename = werkzeug.utils.get_filename(img_file)
        return jsonify({'response':f'Hello World{type(img_file)}'})