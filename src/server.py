from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/p0ubelle', methods=['POST'])
def getdata():
    data = request.json
    print(data)
    return render_template('index.html')


app.run(host="0.0.0.0", port=5000)
