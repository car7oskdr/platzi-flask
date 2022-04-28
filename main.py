from  flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello Bitch <br> and you.</h1>"

if __name__ == '__main__':
    app.run(port = 5000, debug = True)