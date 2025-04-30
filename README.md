from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "¡Hola mundo, Bitácora CS online!"

if __name__ == "__main__":
    app.run()
