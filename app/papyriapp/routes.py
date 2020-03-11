from flask import render_template, make_response
from flask import current_app as app


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/search')
@app.route('/search.html')
def search():
    return render_template('search.html')


@app.route('/summary')
@app.route('/summary.html')
def summary():
    return render_template('summary.html')


@app.errorhandler(404)
def notfound(e):
    return make_response(render_template('404.html'))
