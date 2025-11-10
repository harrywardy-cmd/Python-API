from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/")     #decorator 

def hello_world():           #the endpoint of the API
    return "hello World !"

if __name__ == "__main__":
    app.run(debug=True)      #used to start/run the flask server