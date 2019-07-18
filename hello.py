from flask import Flask

app = flask(__name__)

@app.route('greetings')
def whatistoday():
    return'hello world'

if __name__=='__main__':
    app.run(debug=true, host='0.0.0.0')