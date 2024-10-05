from flask_frozen import Freezer
from app import app  # Replace `myapp` with your actual app module

# Update the output folder
app.config['FREEZER_DESTINATION'] = 'docs'  # Use 'docs' as the destination folder

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
