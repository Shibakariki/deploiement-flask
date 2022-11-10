from flask import Flask, render_template
from flask_redis import FlaskRedis

app = Flask(__name__)
redis_client = FlaskRedis(app)

@app.route('/', methods = ['POST', 'GET'])
def index():
    return render_template("index.html")
    
@app.route('/game', methods = ['POST', 'GET'])
def game():
    try:
        request.cookies.set('userID',"cc")
        name = request.cookies.get('userID')
        return name
    except:
        return "rip"
    if name != None:    
        return render_template("game.html")
    else:
        return redirect(url_for('ask_name'))

# @app.route('/game/naasmke', methods = ['POST', 'GET'])
# def ask_name():


# @app.route('/test')
# def test():
#     return render_template("test.html")

if __name__ == '__main__':
    app.run()
