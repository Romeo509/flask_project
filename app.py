from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydatabase"
)

@app.route('/')
def index():
    # Retrieve data from MySQL
    cursor = db.cursor()
    cursor.execute("SELECT * FROM mytable")
    data = cursor.fetchall()
    cursor.close()
    
    # Render HTML template with data
    return render_template('index.html', data=data)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']

        # Insert the new user into the database
        cursor = db.cursor()
        cursor.execute("INSERT INTO mytable (name, age) VALUES (%s, %s)", (name, age))
        db.commit()
        cursor.close()

        return redirect(url_for('index'))

    return render_template('add_user.html')

if __name__ == '__main__':
    app.run(debug=True)
