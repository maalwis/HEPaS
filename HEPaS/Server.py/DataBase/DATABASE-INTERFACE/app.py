from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Pqr#^(XYZ&*(!',
    'database': 'testdatabase'
}

# Function to create a database connection
def create_db_connection():
    return mysql.connector.connect(**db_config)

# Function to execute queries
def execute_query(query, data=None):
    connection = create_db_connection()
    cursor = connection.cursor()
    cursor.execute(query, data)
    connection.commit()
    cursor.close()
    connection.close()

# Function to fetch data from the database
def fetch_data(query):
    connection = create_db_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/display_schema')
def display_schema():
    query = "SHOW TABLES"
    tables = fetch_data(query)
    return render_template('display_schema.html', tables=tables)

@app.route('/display_records/<table_name>')
def display_records(table_name):
    query = f"SELECT * FROM {table_name}"
    records = fetch_data(query)
    return render_template('display_records.html', records=records, table_name=table_name)

@app.route('/edit_record/<table_name>/<int:record_id>', methods=['GET', 'POST'])
def edit_record(table_name, record_id):
    if request.method == 'GET':
        query = f"SELECT * FROM {table_name} WHERE Record_No = {record_id}"
        record = fetch_data(query)[0]
        return render_template('edit_record.html', record=record, table_name=table_name)
    elif request.method == 'POST':
        # Get data from the form
        data = request.form.to_dict()
        # Generate the UPDATE query dynamically
        update_query = f"UPDATE {table_name} SET "
        for key, value in data.items():
            update_query += f"{key} = '{value}', "
        update_query = update_query[:-2]  # Remove the trailing comma and space
        update_query += f" WHERE Record_No = {record_id}"
        # Execute the UPDATE query
        execute_query(update_query)
        return redirect(url_for('display_records', table_name=table_name))

if __name__ == '__main__':
    app.run(debug=True)
