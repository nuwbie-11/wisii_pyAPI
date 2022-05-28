from flask import render_template, request, jsonify
import numpy as np



def main():
    if request.method == 'POST':
        return jsonify({'response':'Hello World'})