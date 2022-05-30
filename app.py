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

        # data = request.get_json(force=True)
        # image_data = data['images']
        # imgdata = base64.b64decode(image_data)
        img_file = request.files['images']
        # npimg = np.fromstring(img_file,np.uint8)
        in_memory_file = io.BytesIO()
        img_file.save(in_memory_file)
        data = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8)
        color_image_flag = 1
        img = cv2.imdecode(data, color_image_flag)
        # filename = werkzeug.utils.secure_filename(img_file.filename)\
        # img = cv2.imdecode(npimg, cv2.CV_LOAD_IMAGE_UNCHANGED)
        try:
            return jsonify({'response':f'Hello World : {img.shape}'})
        except Exception as e:
            return jsonify({'response':f'Hello World : {e}'})
        

if __name__ == '__main__':
    app.run(port=5000, debug=True,host = '0.0.0.0')