from flask import Flask, render_template, redirect, url_for, request, make_response
import redis

app = Flask(__name__)
redis_client = redis.Redis()

@app.route('/', methods = ['POST', 'GET'])
def index():
    return render_template("index.html")
    
@app.route('/game', methods = ['POST', 'GET'])
def game():
    name = request.cookies.get('userID',default=None)
    if name != None:
        try:
            jetons = redis_client.get(name)
        except:
            jetons = 100
            redis_client.set(name,jetons)
            resp = make_response(render_template("game.html"))
        try:
            resp.set_cookie('ckitonbjt-v2', value=jetons)
            return resp
        except:
            return "rip"
    else:
        return redirect(url_for('ask_name'))

@app.route('/game/naasmke', methods = ['POST', 'GET'])
def ask_name():
    return render_template("ask_name.html")


# @app.route('/test')
# def test():
#     return render_template("test.html")

if __name__ == '__main__':
    app.run()
