import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

flask_app = Flask(__name__)
CLFmodel = pickle.load(open('xg_boost_model.pkl', 'rb'))  # load the ML model

# The route() decorator to tell Flask what URL should trigger our function.
# ‘/’ is the root of the website, such as www.westga.edu
@flask_app.route("/")   
def index():
    return render_template("index.html")


@flask_app.route("/predict", methods = ["POST"])   
def predict():
    float_features = [int(x) for x in request.form.values()]
    features = [np.array(float_features)]
    result = CLFmodel.predict(features)
    return render_template("index.html", predicted_text = result)

if __name__ =="__main__":
    flask_app.run(debug = True)
