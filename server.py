from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Привет web Мир!!'

if __name__ == "__main__": 
    app.run()