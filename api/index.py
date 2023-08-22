from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Sus Sus Sus.... Amogus'

@app.route('/about')
def about():
    return 'About'

if __name__ == '__main__':
    app.run()