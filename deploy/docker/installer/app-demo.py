from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello:https://github.com/meta-liam'


@app.route('/api/v1/hello')
def hello():
    return 'hello'


if __name__ == '__main__':
    print('[INFO] GateWay Ts is running!')
    app.run(host='0.0.0.0', port=80, debug=True)

# python  app-demo.py
