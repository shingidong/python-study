from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    a = open ("index.html","r")
    b = a.read()
    a.close()
    return(b)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1234)