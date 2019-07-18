from flask import Flask

app = flask(__name__)

@app.route('today')
def whatistoday():
    return'its a tuesday'

if __name__=='__main__':
    app.run(debug=true, host='0.0.0.0')