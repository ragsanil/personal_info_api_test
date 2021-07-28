
from flask import Flask, jsonify, request

import requests
import json

app = Flask(__name__)


@app.route('/get_info',methods=['GET','POST'])
def get_info():
    name = request.args.get('name')
    response = requests.get("https://db.grow90.org/api/rest/usersdetails/"+name)
    json_data = json.loads(response.text)
    return jsonify(json_data["usersRag"][0])

if __name__ == '__main__':

    app.run(debug=True)
