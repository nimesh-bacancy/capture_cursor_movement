from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO
import cv2
import sqlite3
import os

app = Flask(__name__)
socketio = SocketIO(app)

# Initialize the database
def init_db():
    conn = sqlite3.connect('mouse_cursor.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS mouse_cursor
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, x INTEGER, y INTEGER, img_path TEXT)''')
    conn.commit()
    conn.close()

# Save mouse data to the database
def save_mouse_data(x, y, img_path):
    conn = sqlite3.connect('mouse_cursor.db')
    c = conn.cursor()
    c.execute("INSERT INTO mouse_cursor (x, y, img_path) VALUES (?, ?, ?)", (x, y, img_path))
    conn.commit()
    conn.close()



@app.route('/view_images')
def view_images():
    conn = sqlite3.connect('mouse_cursor.db')
    c = conn.cursor()
    c.execute("SELECT x, y, img_path FROM mouse_cursor WHERE img_path IS NOT NULL")
    data = c.fetchall()
    conn.close()
    return render_template('view_data.html', data=data)

@socketio.on('mouse_event')
def handle_mouse_event(data):
    x, y = data['x'], data['y']
    img_path = None
    if data['button_pressed']:
        img_path = capture_image(x, y)
    save_mouse_data(x, y, img_path)

# capture images when button is pressed
def capture_image(x, y):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    if ret:
        if not os.path.exists('images'):
            os.makedirs('images')
        img_path = f'images/img_{x}_{y}.jpg'
        cv2.imwrite(img_path, frame)
        return img_path
    return None

@app.route('/')
def index():
    return render_template('index.html')

# Serve static files
@app.route('/images/<path:filename>')
def download_file(filename):
    return send_from_directory('images', filename)

if __name__ == '__main__':
    init_db()
    socketio.run(app, debug=True)
