from flask import Flask, render_template,request, jsonify
# import joblib
import numpy as np
import cv2
# from routes.route import user_bp

app = Flask(__name__)
# app.register_blueprint(user_bp, url_prefix='/')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':

        # data = request.get_json(force=True)
        # image_data = data['images']
        # imgdata = base64.b64decode(image_data)
        img_file = request.files['images'].read()
        # npimg = np.fromstring(img_file,np.uint8)
        # filename = werkzeug.utils.secure_filename(img_file.filename)\
        # img = cv2.imdecode(npimg, cv2.CV_LOAD_IMAGE_UNCHANGED)
        return jsonify({'response':f'Hello World{img_file}'})

if __name__ == '__main__':
    app.run(port=5000, debug=True,host = '0.0.0.0')