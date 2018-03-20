from .main import app

PORT = 8080
HOST = '0.0.0.0'
app.run(host=HOST, port=PORT, debug=True, ssl_context='adhoc')
