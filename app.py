from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS workflows (id INTEGER PRIMARY KEY, name TEXT, status TEXT)''')
    conn.commit()
    conn.close()

# Home Route
@app.route('/')
def home():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM workflows')
    data = c.fetchall()
    conn.close()
    return render_template('index.html', workflows=data)

# Add Workflow
@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    status = request.form['status']
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO workflows (name, status) VALUES (?, ?)', (name, status))
    conn.commit()
    conn.close()
    return home()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)