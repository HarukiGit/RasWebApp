import os
import time
import json
import hashlib
import hmac
import base64
import uuid
import requests
import json
from flask import Flask, render_template, jsonify
import datetime

token = os.getenv('API_TOKEN')
secret = os.getenv('SECRET')

nonce = str(uuid.uuid4())
t = int(round(time.time() * 1000))
string_to_sign = "{}{}{}".format(token, t, nonce)
string_to_sign = bytes(string_to_sign, "utf-8")
secret = bytes(secret, "utf-8")
sign = base64.b64encode(
    hmac.new(secret, msg=string_to_sign, digestmod=hashlib.sha256).digest()
)

apiHeader = {}
apiHeader["Authorization"] = token
apiHeader["Content-Type"] = "application/json"
apiHeader["charset"] = "utf8"
apiHeader["t"] = str(t)
apiHeader["sign"] = str(sign, "utf-8")
apiHeader["nonce"] = nonce

response = requests.get("https://api.switch-bot.com/v1.1/devices", headers=apiHeader)
print(response.json())

app = Flask(__name__)

@app.route('/')
def home():
    # 現在の時刻を取得して渡す
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', current_time=current_time)

@app.route('/get_time')
def get_time():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify(current_time=current_time)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)