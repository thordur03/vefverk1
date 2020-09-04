from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    #the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>sida1</h1>
    <p>It is currently {time}.</p>
    <a href="/">forsíða</a>
    <a href="seccondpage">Síða 2</a>
    <a href="thirdpage">Síða 3</a>
    <br>
    <img src="http://loremflickr.com/600/400">
    """
    #format(time=the_time)

@app.route('/seccondpage')
def seccondpage():
    # the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>sida2</h1>
    <p>It is currently {time}.</p>
    <a href="/">forsíða</a>
    <a href="seccondpage">Síða 2</a>
    <a href="thirdpage">Síða 3</a>
    <br>
    <img src="http://loremflickr.com/600/400">
    """#.format(time=the_time)

@app.route('/thirdpage')
def thirdpage():
    # the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>sida3</h1>
    <p>It is currently {time}.</p>
    <a href="/">forsíða</a>
    <a href="seccondpage">Síða 2</a>
    <a href="thirdpage">Síða 3</a>
    <br>
    <img src="http://loremflickr.com/600/400">
    """#.format(time=the_time)
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)