from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return '''<html style="background:black;color:white;text-align:center;padding-top:100px">
    <h1>BTC COINS THE HUNTER</h1>
    <h2 style="color:lime">BOT IS RUNNING 24/7</h2>
    <p>2 Coins Per Day | 20 USDT x20 | Flip after 24h | Transfer >80 to Spot</p>
    </html>'''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
