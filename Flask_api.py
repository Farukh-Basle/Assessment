from flask import Flask,jsonify
from flask_restful import Api, Resource
import requests

app = Flask(__name__)
api = Api(app)

@app.route('/')
def HelloWorld():
    return 'Hello, World..!'

@app.route('/arm/<int:n>/')
def armstrong(n):
    
    sum = 0
    order = len(str(n))
    copy_n = n
    while (n>0):
        digit = n%10
        sum += digit  ** order
        n = n//10

    if (sum == copy_n):
        print(copy_n," is armstrong number")
        result = {
            "Number":copy_n,
            "Armstrong":True,        
        }
    else:
        print(copy_n,"is not armstrong number")
        result = {
            "Number":copy_n,
            "Armstrong":False,       
        }
        
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)



