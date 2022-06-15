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
        img = cv2.resize(img, (224, 224))

        x = image.img_to_array(img)
        x.resize(1, 224, 224, 3)

        interpreter = tf.lite.Interpreter("model/Mobilenetv2plusConv2d2V4.tflite")
        interpreter.allocate_tensors()
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()

        interpreter.set_tensor(input_details[0]["index"], x)
        interpreter.invoke()
        output_data = interpreter.get_tensor(output_details[0]["index"])
        # print(output_data)
        # higehst_conf = max(output_data[0])
        # ix = np.where(output_data == higehst_conf)[-1][0]

        labels = {
            0:"1.000",
            1:"10.000",
            2:"100.000",
            3:"2.000",
            4:"20.000",
            5:"5.000",
            6:"50.000",
        }

        result = f"""
        1.000 Rupiah {(output_data[0][0]*100):.2f} %
        2.000 Rupiah {(output_data[0][3]*100):.2f} %
        5.000 Rupiah {(output_data[0][5]*100):.2f} %
        10.000 Rupiah {(output_data[0][1]*100):.2f} %
        20.000 Rupiah {(output_data[0][4]*100):.2f} %
        50.000 Rupiah {(output_data[0][6]*100):.2f} %
        100.000 Rupiah {(output_data[0][2]*100):.2f} %
        """

        # message = labels[ix]

        try:
            return result
        except Exception as e:
            return f"{e}"


if __name__ == "__main__":
    app.run(port=5000, debug=True)
