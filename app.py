from flask import Flask, request
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.preprocessing import image

app = Flask(__name__)
# app.register_blueprint(user_bp, url_prefix='/')


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":

        img = request.files["images"].read()
        npimg = np.fromstring(img, np.uint8)
        img = cv2.imdecode(npimg, -1)
        img = cv2.resize(img, (224, 224))/255

#         x = image.img_to_array(img)
        x = tf.convert_to_tensor(x)
        # img = tf.image.per_image_standardization(img)
        img = tf.expand_dims(x, axis=0)

        interpreter = tf.lite.Interpreter("model/forskripsi.tflite")
        interpreter.allocate_tensors()

        input_details = interpreter.get_input_details()

        interpreter.set_tensor(input_details[0]["index"], img)
        interpreter.invoke()


        output_details = interpreter.get_output_details()
        output_data = interpreter.get_tensor(output_details[0]["index"])


        classes = {
            0:"Rp 1.000",
            1:"Rp 10.000",
            2:"Rp 100.000",

            3:"Rp 2.000",
            4:"Rp 20.000",

            5:"Rp 5.000",
            6:"Rp 50.000"
        }
        
        try:
            return classes[np.argmax(output_data)]
        except Exception as e:
            return f"{e}"


if __name__ == "__main__":
    app.run(port=5000, debug=True)
