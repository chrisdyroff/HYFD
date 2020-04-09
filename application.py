from flask import Flask
from flask import render_template


application = app = Flask(__name__)

posts = [
{
    'author': 'roff',
    'title': 'Blog Post 1',
    'content': 'Everything is not ok.'
},
{
    'author': 'p.',
    'title': 'Blog Post 2',
    'content': 'By fire or fire'
}

]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='about')

@app.route('/issues')
def issues():
    return render_template('issues.html', title='issues')


if (__name__) == '__main__':
    app.run(debug=True)


