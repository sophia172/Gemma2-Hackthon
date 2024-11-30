from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/images', methods=['POST'])
def process_images():
    data = request.data.decode('utf-8')
    print(data)
    return "Text received successfully", 200

@app.route('/api/text', methods=['POST'])
def process_data():
    image = request.files['image']
    image.save(f"./uploaded_{image.filename}")
    print(f"Image {image.filename} received and saved.")
    return {"message": "Image uploaded successfully"}, 200

@app.route('/api/data', methods=['POST'])
def process_everything():
    text_and_images = request.json
    print(text_and_images)
    return {"message": "Data received successfully"}, 200

if __name__ == '__main__':
    app.run(debug=True)
