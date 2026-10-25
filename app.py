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
from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
body{background:black;color:white;text-align:center;font-family:Arial;margin:0;padding:20px}
.btn{padding:12px 20px;margin:8px;border:none;border-radius:12px;font-weight:bold;color:white;cursor:pointer;font-size:14px}
.green{background:#00c853;box-shadow:0 0 10px #00c853}
.red{background:#d50000;box-shadow:0 0 10px #d50000}
.blue{background:#2962ff;box-shadow:0 0 10px #2962ff}
.card{background:#111;border:1px solid #333;border-radius:16px;padding:15px;margin:20px auto;max-width:400px}
</style>
</head>
<body>
<h1>BTC COINS THE HUNTER</h1>
<h3 style="color:lime">BOT IS RUNNING 24/7</h3>

<button class="btn green" onclick="window.open('https://www.binance.com/en/my/wallet/account/main/deposit','_blank')">Deposit</button>
<button class="btn red" onclick="window.open('https://www.binance.com/en/my/wallet/account/main/withdraw','_blank')">Withdraw</button>
<button class="btn blue" onclick="alert('Balance: Checking...\\nStrategy: 2 Coins/Day | 20 USDT x20 | Flip after 24h')">Balance</button>

<div class="card">
<div style="text-align:left;font-size:12px;color:#888">MEGAUSDT > <span style="color:lime">+12.34%</span></div>
<canvas id="chart"></canvas>
<div style="margin-top:10px;font-size:11px;color:#aaa">
Entry: 0.8420 | Current: 0.9462 | PNL: <span style="color:lime">+$1,240.56</span><br>
Strategy: Trend Hunter | Trades: 2/day | Uptime: 24h
</div>
</div>

<p style="font-size:11px;color:#666">2 Coins Per Day | 20 USDT x20 | Flip after 24h | Transfer >80 to Spot</p>

<script>
const ctx=document.getElementById('chart');
new Chart(ctx,{type:'line',data:{labels:['','','','','','','',''],datasets:[{label:'MEGAUSDT',data:[0.80,0.82,0.86,0.83,0.89,0.88,0.92,0.94],borderColor:'lime',backgroundColor:'rgba(0,255,0,0.1)',tension:0.4,pointRadius:5,pointBackgroundColor:'lime'}]},options:{plugins:{legend:{display:false}},scales:{x:{display:false},y:{display:false}}}})
</script>
</body>
</html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
