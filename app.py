from flask import Flask, render_template
from flask_flatpages import FlatPages

app = Flask(__name__)
# Use .md extension for Markdown files
app.config['FLATPAGES_EXTENSION'] = '.md'
# Pages are stored in the 'pages/' directory
app.config['FLATPAGES_ROOT'] = 'pages'
pages = FlatPages(app)


@app.route('/')
def index():
    # Render the index.md as the homepage
    page = pages.get('index')  # Fetch the 'index.md' page
    return render_template('page.html', page=page)


@app.route('/<path:path>/')
def page(path):
    # Find the page from the pages/ directory by its path
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)


if __name__ == '__main__':
    app.run(debug=True)
