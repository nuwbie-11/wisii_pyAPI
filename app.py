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
        img = request.files['images'].read()
        npimg = np.fromstring(img, np.uint8)
        img = cv2.imdecode(npimg,-1)

        try:
            return(jsonify({"response":f"Hellow{img.shape}"}))
        except Exception as e:
            return(jsonify({"response":f"Hellow{e}"}))


if __name__ == '__main__':
    app.run(port=5000, debug=True)