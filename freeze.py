from flask_frozen import Freezer
from app import app  # Replace `myapp` with your app module name

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze(destination='docs')  # Set output folder to 'docs'
