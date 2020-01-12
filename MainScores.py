from flask import Flask, escape, request
from Scores import read_score
from Utils import *

app = Flask(__name__)

@app.route('/')
@app.route('/score_server')
def score_server():
    score = read_score()
    if score != BAD_RETURN_CODE:
        return '''
        <html>
        <head>
           <title>Scores Game</title>
        </head>
        <body>
            <h1><h1>The score is <div id="score"> The score is:''' + score + '''</div></h1></h1>
        </body>
        </html>
        '''
    else:
        return '''
        <head>
        <title>Scores Game</title>
        </head>
        <body>
        <body>
        <h1><div id="score" style="color:red"> Error ''' + score + '''</div></h1>
        </body>
        </html>
                '''
