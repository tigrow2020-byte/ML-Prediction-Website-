from flask import Flask, render_template, request
from model import predict_marks

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    hours = int(request.form["hours"])
    result = predict_marks(hours)
    return render_template("index.html",
                         hours=hours,
                         result=result)

if __name__ == "__main__":
    app.run(debug=True)
