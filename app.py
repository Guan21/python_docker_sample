from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

# @app.route('/hello')
# def hello_world_1():
#     return 'Hello, Docker!ssss'