from bottle import run, route, debug, post, get, static_file


@route('/')
def index():
    return static_file('index.html', root='.')


debug(True)
run(host='0.0.0.0', port='9999')
