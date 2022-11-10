from flask import Flask, render_template, redirect, url_for, request, make_response
import redis

app = Flask(__name__)
redis_client = redis.Redis(
    host='localhost',
    port=6379)

@app.route('/', methods = ['POST', 'GET'])
def index():
    return render_template("index.html")
    
@app.route('/game', methods = ['POST', 'GET'])
def game():
    name = request.cookies.get('userID',default=None)
    if name != None:
        resetJetons(name)
        return render_template("game.html")
    else:
        return redirect(url_for('ask_name'))

@app.route('/game/naasmke', methods = ['POST', 'GET'])
def ask_name():
    return render_template("ask_name.html")

@app.route("/resetJetons/<name>", methods = ['GET'])
def resetJetons(name):
    jetons = request.cookies.get('ckitonbjt-v2',default=None)
    redis_client.set(name,jetons)
    return redirect(url_for('game'))

# @app.route('/test')
# def test():
#     return render_template("test.html")

if __name__ == '__main__':
    app.run()
