from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
import os
import time

app = Flask(__name__)
CORS(app)

def get_db_connection():
    retries = 5
    while retries > 0:
        try:
            return mysql.connector.connect(
                host=os.environ.get('DB_HOST', 'db'),
                user=os.environ.get('DB_USER', 'root'),
                password=os.environ.get('DB_PASSWORD', 'sena123'),
                database=os.environ.get('DB_NAME', 'festival_db')
            )
        except mysql.connector.Error:
            retries -= 1
            time.sleep(2)
    raise Exception("No se pudo conectar a la base de datos")

@app.route('/api/info')
def get_info():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT nombre FROM artistas")
        artistas = cursor.fetchall()
        conn.close()
        
        return jsonify({
            "festival": "Pacific DevOps Music Fest",
            "fecha": "15 de Agosto de 2026",
            "artistas": [a['nombre'] for a in artistas]
        })
    except Exception as e:
        return jsonify({"error": str(e), "artistas": []})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)