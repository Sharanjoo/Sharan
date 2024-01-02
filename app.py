from flask import Flask, render_template

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('index.html', name='Sharan L', usn='1BM20IS136')

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)