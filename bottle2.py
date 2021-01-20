from bottle import run, route, debug, post, get, static_file


@route('/')
def index():
    return static_file('index.html', root='.')


@route('/echo/<thing>')
def echo(thing):
    return "Say hello to my little friend: %s!" % thing


debug(True)

run(host='0.0.0.0', port='9999', reloader=True)
