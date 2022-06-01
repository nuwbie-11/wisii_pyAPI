from flask import Flask, render_template,request, jsonify
# import joblib
import numpy as np
import io
import cv2
# from routes.route import user_bp
import tensorflow as tf
from tensorflow.keras.preprocessing import image

app = Flask(__name__)
# app.register_blueprint(user_bp, url_prefix='/')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        message = "Tidak Dikenali"
        model = tf.keras.load_model('model/MDClassification')
        img = request.files['images'].read()
        npimg = np.fromstring(img, np.uint8)
        img = cv2.imdecode(npimg,-1)
        img = cv2.resize(img,(150,150))

        x = image.img_to_array(img)
        x = np.expand_dims(x,axis=0)

        img = np.vstack([x])
        classes = model.predict(img,batch_size=10)

        if classes[0][0]==1:
            message = ('100k')
        elif classes[0][1]==1:
            message = ('10k')
        elif classes[0][2]==1:
            message = ('50k')

        try:
            return(jsonify({"response":f"{message}"}))
        except Exception as e:
            return(jsonify({"response":f"Hellow{e}"}))


if __name__ == '__main__':
    app.run(port=5000, debug=True)