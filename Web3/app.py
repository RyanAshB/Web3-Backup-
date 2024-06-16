from flask import Flask, render_template

app = Flask(__name__)

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/questions')
def questions():
    return render_template('questions.html')

@app.route('/hiw')
def hiw():
    return render_template('hiw.html')

if __name__ == '__main__':
    app.run(debug=True)

