from flask import Flask, render_template,request, jsonify
# import joblib
# import numpy as np
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
        # filename = werkzeug.utils.get_filename(img_file)
        return jsonify({'response':'Hello World'})

if __name__ == '__main__':
    app.run(debug=True,host = '0.0.0.0')