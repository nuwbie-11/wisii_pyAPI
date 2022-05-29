import base64
from flask import render_template, request, jsonify
import numpy as np



def main():
    if request.method == 'POST':
        data = request.get_json(force=True)
        image_data = data['image']
        imgdata = base64.b64decode(image_data)
        return jsonify({'response':f'Hello World{image_data}'})