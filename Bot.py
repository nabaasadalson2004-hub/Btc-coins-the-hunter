import time, ccxt, json, os
from datetime import datetime, date, timedelta

# TRACK when each trade was opened
POSITIONS_FILE = "open_positions.json"

def save_position_open_time(symbol):
    data = {}
    if os.path.exists(POSITIONS_FILE):
        with open(POSITIONS_FILE) as f: data = json.load(f)
    data[symbol] = str(datetime.now()) # save open time
    json.dump(data, open(POSITIONS_FILE, "w"))

def check_flip_after_24h():
    if not os.path.exists(POSITIONS_FILE): return
    with open(POSITIONS_FILE) as f: data = json.load(f)
    
    try:
        positions = exchange.fetch_positions()
        for pos in positions:
            symbol = pos['symbol']
            if pos['contracts'] > 0 and pos['side'] == 'short':
                if symbol in data:
                    open_time = datetime.fromisoformat(data[symbol])
                    hours_open = (datetime.now() - open_time).total_seconds() / 3600
                    
                    # YOUR RULE: After 24hrs, flip short -> long
                    if hours_open >= 24:
                        print(f"{symbol} has been SHORT for {hours_open:.1f}h - FLIPPING TO LONG after 24h")
                        exchange.create_market_buy_order(symbol, pos['contracts']) # close short
                        time.sleep(2)
                        exchange.create_market_buy_order(symbol, pos['contracts']) # open long
                        del data[symbol] # remove
                        json.dump(data, open(POSITIONS_FILE,"w"))
    except Exception as e:
        print(f"Flip check error: {e}")

# In trade() function, after opening SHORT, add:
# save_position_open_time(symbol)
