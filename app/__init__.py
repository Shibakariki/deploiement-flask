from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add')
def add():
    return render_template("add.html")
    
@app.route('/game')
def game():
    return render_template("game.html")

@app.route('/main')
def main():
    return render_template("main.html")

if __name__ == '__main__':
    app.run()
