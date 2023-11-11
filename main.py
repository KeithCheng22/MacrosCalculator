import requests
from flask import Flask, render_template, request
import os

app = Flask(__name__)

API_KEY = os.environ.get('API_KEY')
api_url = 'https://api.calorieninjas.com/v1/nutrition?query='

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form['food']
        response = requests.get(api_url + query, headers={'X-Api-Key': API_KEY})
        if response.status_code == requests.codes.ok:
            food_data = response.json()
            food_items = food_data['items']
            return render_template('index.html', sent=True, text=food_items)
        else:
            text = "Error:", response.status_code, response.text
            return render_template('index.html', sent=True, text=text)
    return render_template('index.html', sent=False)


if __name__ == '__main__':
    app.run()
