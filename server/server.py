from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    # well do img classification here by the model we trained
    return 'Hi'

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    app.run()
    # util.load_saved_artifacts()
    # app.run()