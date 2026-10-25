from flask import Flask
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
body{background:#050505;color:white;text-align:center;font-family:Arial;margin:0;padding:15px}
.btn{padding:14px 20px;margin:8px;border:none;border-radius:12px;font-weight:bold;color:white;cursor:pointer;font-size:14px;width:90%;max-width:320px}
.green{background:#00c853;box-shadow:0 0 12px #00c853}
.red{background:#d50000;box-shadow:0 0 12px #d50000}
.blue{background:#2962ff;box-shadow:0 0 12px #2962ff}
.card{background:#111;border:1px solid #333;border-radius:16px;padding:12px;margin:15px auto;max-width:420px}
.balance-box{background:#111;border:2px solid #00ff88;border-radius:16px;padding:18px;margin:15px auto;max-width:420px;box-shadow:0 0 15px #00ff8866}
.balance-amount{font-size:32px;color:#00ff88;font-weight:bold}
.footer{margin-top:20px;padding:15px;border-top:1px solid #222;color:#7ef9ff;font-size:11px}
</style>
</head>
<body>
<h1>BTC COINS THE HUNTER</h1>
<h3 style="color:lime">BOT IS RUNNING 24/7</h3>

<div class="balance-box">
<div style="font-size:10px;color:#888">YOUR BALANCE ON BINANCE</div>
<div class="balance-amount">$1,240.56</div>
<div style="font-size:11px;color:#aaa;margin-top:5px">Spot: $850 | Bot: $390 | 2 Coins | PNL +$124</div>
</div>

<button class="btn green" onclick="window.open('https://www.binance.com/en/my/wallet/account/main/deposit/crypto','_blank')">Deposit → Binance</button>
<button class="btn red" onclick="window.open('https://www.binance.com/en/my/wallet/account/main/withdrawal/crypto','_blank')">Withdraw → Binance</button>
<button class="btn blue" onclick="window.open('https://www.binance.com/en/my/wallet/account/overview','_blank')">Balance $1,240 → View on Binance</button>

<div class="card">
<div style="display:flex;justify-content:space-between;font-size:11px;color:#888">
<span>MEGAUSDT • 1m • Live</span><span style="color:lime">+12.34%</span><span style="color:#00ff88">0.9462</span>
</div>
<canvas id="tradeChart" height="230"></canvas>
<div style="font-size:10px;color:#aaa;text-align:left;background:#0a0a0a;padding:10px;border-radius:8px;margin-top:8px">
<b style="color:white">HOW THIS SIGNAL WILL TRADE:</b><br>
📍 BUY at 0.8450 (dip) - $20 USDT x20 = $400<br>
📍 SELL 50% at 0.9200 (+8.8% profit)<br>
📍 SELL 50% at 0.9850 (+16.5% profit)<br>
⏱️ 2 trades per day | 🔄 Flip after 24h | 💰 Amount: $40 per trade
</div>
</div>

<div class="footer">✨ BUILD YOUR FUTURE FOR THE BETTERNESS OF TOMORROW ✨</div>

<script>
const ctx=document.getElementById('tradeChart');
new Chart(ctx,{
 type:'line',
 data:{
  labels:['9:00',[STRIPPED]
  datasets:[{
   label:'MEGAUSDT',
   data:[0.82,0.835,0.825,0.845,0.86,0.875,0.865,0.89,0.92,0.91,0.93,0.946],
   borderColor:'#00ff88',
   backgroundColor:'rgba(0,255,136,0.08)',
   tension:0.4,
   fill:true,
   borderWidth:2,
   pointBackgroundColor:function(c){let i=c.dataIndex; if(i==3) return 'blue'; if(i==8||i==11) return 'red'; return '#00ff88';},
   pointRadius:function(c){let i=c.dataIndex; if(i==3||i==8||i==11) return 6; return 0;}
  }]
 },
 options:{
  plugins:{
   legend:{display:false},
   tooltip:{callbacks:{label:function(c){if(c.dataIndex==3) return ' BUY HERE 0.8450'; if(c.dataIndex==8) return ' SELL 50% 0.92'; if(c.dataIndex==11) return ' SELL 100% 0.9462'; return ' $'+c.raw;}}}
  },
  scales:{x:{grid:{color:'#1a1a1a'},ticks:{color:'#666',font:{size:9}}},y:{grid:{color:'#1a1a1a'},ticks:{color:'#666'}}}
 }
});
</script>
</body>
</html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
