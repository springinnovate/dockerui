from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html', content='test')


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
