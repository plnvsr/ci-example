import websocket
import json
import time
import ssl 

# Print the received data
def on_message(ws, message):
    data = json.loads(message)
    print(data)

def on_error(ws, error):
    print(error)

def on_close(ws, status_code, close_msg):
    print("Connection closed.")

# Open a connection to receive btcusdt data for 5 seconds, then close the socket
def on_open(ws):
    ws.send(json.dumps({"method": "SUBSCRIBE", "params": ["btcusdt@trade"], "id": 1}))

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://stream.binance.com:9443/ws",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close,
                                on_open = on_open)
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
