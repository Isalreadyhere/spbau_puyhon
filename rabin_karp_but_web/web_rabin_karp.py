# A very simple Flask Hello World app for you to get started with...

#return ' '.join(str(e) for e in l)
from library import rabin_karp_algorithm as rk
import flask
from flask import Flask

app = Flask(__name__)

@app.route('/')
def enter():  
    return flask.render_template('enter.html')

@app.route('/Results', methods=['POST'])
def success(): 
    if flask.request.method == 'POST': 
        l = rk.rabin_karp(flask.request.form['main_string'], flask.request.form['include_string'])
        result = ' '.join(str(e) for e in l)
        return flask.render_template('results.html', res = result) 
    else: pass



if __name__ == '__main__':
   app.run()
