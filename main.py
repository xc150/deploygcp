from flask import Flask
from flask import jsonify, render_template

app = Flask(__name__)

@app.route('/')
def homapage():
    """Return my homepage."""
    return render_template("index.html")

@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)

@app.route('/xc')
def xc():
    return "Yeah it's me"

@app.route('/bob')
def bob():
    val = {"value": "bob"}
    return jsonify(val)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)