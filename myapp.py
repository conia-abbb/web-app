from flask import Flask, render_template, request
app = Flask(__name__)
import os

items = []
@app.route('/')
def index():
    return render_template("form.html", items = items) 

@app.route('/add_todo')
def add_todo():
    item = request.args.get("item")
    items.append(item)
    return redirect("http://localhost:5000/",code = 302)

@app.route('/foo/<names>')
def foo(name):
    return render_template('index.html', to=name)


if __name__=='__main__':
    port = os.environ.get('Port', 5000)
    app.run(debug=True, host='0.0.0.0',port=port)
