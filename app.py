from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_image', methods=['POST'])
def process_image():
    image_file = request.files['image']
    prompt = request.form['prompt']

        
    r = requests.post(
        "https://api.deepai.org/api/3d-character-generator",
        files={'image': image_file},
        data={'text': prompt},
        headers={'api-key': '415fcf85-9478-4ecc-9ee3-79bfd328f346'}
    )

    output_url = r.json()['output_url']

    return render_template('index.html', output_url=output_url)
if __name__ == '__main__':
    app.run(debug=True, port=8000)

