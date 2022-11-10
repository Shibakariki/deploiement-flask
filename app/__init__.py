from flask import Flask, render_template, redirect, url_for, request, make_response
import redis

app = Flask(__name__)
redis_client = redis.Redis(
    host='localhost',
    port=6379)

@app.route('/', methods = ['POST', 'GET'])
def index():
    return render_template("index.html")

@app.route('/add', methods = ['POST', 'GET'])
def add():
    return render_template("add.html")

@app.route('/addJetons', methods = ['POST'])
def addJetons():
    name = request.form.get('username')
    jetons = request.form.get('donate')
    if name != None:
        try:
            redis_client.set(name,redis_client.get(name)+jetons)
        except:
            var = str(int(redis_client.get(name))+int(jetons))
            return var
        try:
            redis_client.rpush("add"+name,jetons)
        except:
            return "ripa"
    return redirect(url_for('game'))


@app.route('/game', methods = ['POST', 'GET'])
def game():
    name = request.cookies.get('userID',default=None)
    if name != None:
        jetons = redis_client.get(name)
        if jetons == None:
            jetons = "100"
            redis_client.set(name,jetons)
        resp = make_response(render_template("game.html"))
        resp.set_cookie('ckitonbjt-v2',jetons)
        return resp        
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
