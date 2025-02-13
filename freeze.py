from flask_frozen import Freezer
from app import app  # Ensure 'app.py' exists

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
