from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello katsara!'

@app.route('/Id')
def Id():
    return '654272116'

@app.route('/name')
def name():
    return 'katsara Buakaeo'

@app.route('/university')
def university():
    return 'Phetchaburi Rajabhat University'

if __name__ == '__main__':
    app.run(debug=True)