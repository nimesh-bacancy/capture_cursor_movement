# Mouse Tracker

This project allows you to track mouse movements and capture images on mouse clicks. The captured images, along with the mouse coordinates, are stored in a database and can be viewed on a separate page.

## Features
- Real-time mouse movement tracking
- Capture images using the webcam on mouse clicks
- Store mouse coordinates and image paths in a SQLite database
- View captured images along with their coordinates

## Requirements
- Python 3.x
- Flask
- Flask-SocketIO
- OpenCV
- SQLite

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-repo/mouse-tracker.git
    cd mouse-tracker
    ```

2. **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Initialize the database:**
    The database will be initialized automatically when you run the application for the first time.

## Running the Application

1. **Start the Flask application:**
    ```bash
    python main.py
    ```

2. **Open your web browser and navigate to:**
    ```
    http://127.0.0.1:5000/
    ```

3. **Track mouse movements and capture images:**
    - Move your mouse over the page to track the coordinates.
    - Click on the page to capture an image using your webcam.

4. **View captured images:**
    - Click the "View Captured Images" button on the index page or navigate to:
    ```
    http://127.0.0.1:5000/view_images
    ```