from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola mundo, madafakas!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


#export FLASK_APP=webapi.py
#set FLASK_APP=webapi.py

#flask run