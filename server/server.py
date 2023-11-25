from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    # well do img classification here by the model we trained
    img_data = request.form['image_data']
    
    # tern the function reslut into a json response
    response = jsonify(util.classify_image(img_data))
    
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Sport Celebrity Image Classification...")
    util.load_saved_artifacts()
    app.run()