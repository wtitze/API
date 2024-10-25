import os
from flask import Flask, jsonify, request, redirect, url_for
import mysql.connector
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

def get_db_connection():
    return mysql.connector.connect(
        host="mysql-9b7d77c-iisgalvanimi-49c1.h.aivencloud.com",
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        database="W3Schools",
        port=16723
    )

@app.route('/')
def home():
    return redirect('/apidocs/')

@app.route('/api/tables', methods=['GET'])
def get_tables():
    """
    Un endpoint per restituire le tabelle del database
    ---
    responses:
      200:
        description: tabelle del database
        schema:
          type: object
          properties:
            message:
              type: string
              example: "[
                    'Categories',
                    'Customers',
                    '...',
                    'Shippers',
                    'Suppliers'
                ]"
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SHOW TABLES")
    
    tables = [row[0] for row in cursor.fetchall()]
    cursor.close()
    connection.close()
    
    return jsonify(tables)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)