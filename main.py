from sys import argv as args
from flask import Flask as flask_app
from flask import render_template as render

sets = {
    'port': 8000,
    'ip': '127.0.0.1',
    'debug': False,
    'cors': True
}

for i in range(len(args)):
    if args[i] == '--debug':
        sets['debug'] = True
    elif args[i] == '--no-debug':
        sets['debug'] = False
    elif args[i] == '--ip' or args[i] == '--bind':
        sets['ip'] = args[i+1]
    elif args[i] == '--port':
        sets['port'] = int(args[i + 1])
    elif args[i] == '--cors':
        sets['cors'] = True
    elif args[i] == '--no-cors':
        sets['cors'] = False

app = flask_app(__name__, template_folder = 'src', static_folder = 'static')

if sets['cors']:
    from flask_cors import CORS as cors_for_flask
    cors_for_flask(app)


@app.route('/')
def index():
    return render('index.html')


@app.route('/xash')
def xash():
    return render('xash.html')


@app.errorhandler(404)
def error404(response):
    return render('error404.html'), 404


if __name__ == '__main__':
    app.run(sets['ip'], debug = sets['debug'], port = sets['port'])
