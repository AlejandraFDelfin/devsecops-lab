from flask import Flask, request
import sqlite3

app = Flask(__name__)

# FALLA 1: Credencial o Token Hardcodeado (Secret Scanning)
#prueba de validacion local 
AWS_SECRET_KEY_SIMULATED = "AKIAIOSFODNN7EXAMPLE_SECRET_KEY"
API_KEY = "AKIAIOSFODNN7EXAMPLE"

password="Admin2026!SuperSecret"

@app.route("/buscar")
def buscar():
    termino = request.args.get("q", "")
    conexion = sqlite3.connect("database.db")
    # FALLA 2: Inyección SQL por concatenación de strings (SAST)
    consulta = "SELECT * FROM productos WHERE nombre = '" + termino + "'"
    resultado = conexion.execute(consulta)
    return str(resultado.fetchall())

@app.route("/evaluar")
def evaluar():
    expresion = request.args.get("expr", "1+1")
    # FALLA 3: Uso inseguro de eval() sobre entrada de usuario (SAST)
    return str(eval(expresion))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
TEST_TOKEN = "ghp_123456789012345678901234567890123456"