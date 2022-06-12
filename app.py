from flask import Flask,request
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.preprocessing import image

app = Flask(__name__)
# app.register_blueprint(user_bp, url_prefix='/')


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        message = "Tidak Dikenali"

        img = request.files["images"].read()
        npimg = np.fromstring(img, np.uint8)
        img = cv2.imdecode(npimg, -1)
        img = cv2.resize(img, (150, 150))
        img = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA)

        x = image.img_to_array(img)
        x.resize(1, 150, 150, 4)

        interpreter = tf.lite.Interpreter("model/mmodel.tflite")
        interpreter.allocate_tensors()
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()

        interpreter.set_tensor(input_details[0]["index"], x)
        interpreter.invoke()
        output_data = interpreter.get_tensor(output_details[0]["index"])
        # print(output_data)
        higehst_conf = max(output_data[0])
        ix = np.where(output_data == higehst_conf)[-1][0]

        labels = {
            0: "100 Ribu",
            1: "10 Ribu",
            2: "1 Ribu",
            3: "20 Ribu",
            4: "2 Ribu",
            5: "50 Ribu",
            6: "5 Ribu",
        }

        message = labels[ix]

        try:
            return (f"Tebakan tertinggi pada {message} dengan nilai {(higehst_conf*100):.2f}%")
        except Exception as e:
            return (f"{e}")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
