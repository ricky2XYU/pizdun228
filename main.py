from flask import Flask, request


CHAIN_ID = 84846147 # введите любой id
CHAIN_ID_HEX = hex(CHAIN_ID)
ADDRESS = "0xd5Cb5efB99e5C9C55109D64b72ccb92B01A00F7b" # ваш METAMASK адрес
BALANCE = 16542 # баланс ETH

app = Flask(__name__)


@app.route("/", methods=['POST'])
def chain():
   if request.method == 'POST':
      data = request.get_json()
      if data["method"] == "eth_chainId":
        return '''{"jsonrpc": "2.0","id": 1,"result": "'''+CHAIN_ID_HEX+'''"}'''
      if data["method"] == "net_version":
        return '''{"jsonrpc": "2.0","id": 1,"result": "'''+str(CHAIN_ID)+'''"}'''
      if data["method"] == "eth_blockNumber":
        return '''{"jsonrpc": "2.0","id": 1,"result": "0x0"}'''
      if data["method"] == "eth_getBalance":
        resp_address = data["params"][0]
        if resp_address == ADDRESS.lower():
            return '''{"jsonrpc": "2.0","id": 1,"result": "''' + hex(int(BALANCE * 1000000000000000000)) + '''"}'''
        else:
            return '''{"jsonrpc": "2.0","id": 1,"result": "0x0"}'''
      return data


if __name__ == "__main__":
    app.run()