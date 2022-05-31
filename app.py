from flask import Flask, render_template,request, jsonify
# import joblib
import numpy as np
import io
import cv2
# from routes.route import user_bp

app = Flask(__name__)
# app.register_blueprint(user_bp, url_prefix='/')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        filestr = request.files['images'].read()
        npimg = np.fromstring(filestr, np.uint8)
        img = cv2.imdecode(npimg,-1)

    return(jsonify({"response":"Hellow"}))
                

if __name__ == '__main__':
    app.run(port=5000, debug=True)