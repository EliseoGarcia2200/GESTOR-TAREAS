from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "¡Hola, mundo! Mi gestor de tareas ya está vivo."

if __name__ == "__main__":
    app.run(debug=True)