from flask import render_template, make_response, request
from flask import current_app as app

from .modules import summarizer


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/search')
@app.route('/search.html')
def search():
    return render_template('search.html')


@app.route('/summaryMeta', methods=['POST'])
def summaryMeta():
    if request.method == 'POST':
        obj = {
            "title": request.form['title'],
            "authors": request.form['authors'],
            "date": request.form['date'],
            "url": request.form['url']
        }

        obj.update(summarizer.summarize(obj))
        return obj


@app.route('/summary.html')
def summary():
    return render_template('summary.html')


@app.errorhandler(404)
def notfound(e):
    return make_response(render_template('404.html'))
