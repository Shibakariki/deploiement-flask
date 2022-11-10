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
        return name
        # try:
        #     jetons = redis_client.get(name)
        # except:
        #     jetons = "100"
        #     return str(name)
        #     redis_client.set(name,"100")
        #     return redis_client.get(name)
        # resp = make_response(render_template("game.html"))
        # resp.set_cookie('ckitonbjt-v2',jetons)
        # return resp
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
