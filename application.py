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
},
{
    'author': 'p.',
    'title': 'Seamus Heaney',
    'content': '''To be carried back to the shrine some dawn
    when the sea spreads its far sun crops to the South
    and I make my morning offering again:
    that I may escape the miasma of spilled blood,
    govern the tongue, fear hybris, fear the god,
    until he speaks in my untrammelled mouth'''
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


