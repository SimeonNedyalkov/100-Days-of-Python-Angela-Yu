import requests
import pprint
from flask import Flask,request,render_template,url_for,redirect

response = requests.get('https://api.openbrewerydb.org/breweries')
#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(response.json())

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',all_brews=response.json())

@app.route('/brew/<id>')
def singlebrewery(id):
    for brew in response.json():
        if brew['id'] == id:
            return render_template('singlebrew.html', selected_brew = brew)

if __name__ == '__main__':
    app.run(debug=True)
