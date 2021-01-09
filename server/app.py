from flask import Flask

from footage.raw import raw_footage_bp

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


app.register_blueprint(raw_footage_bp, url_prefix='/api/v1/raw')

if __name__ == '__main__':
    app.run()
