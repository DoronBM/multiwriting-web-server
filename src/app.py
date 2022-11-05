from bottle import run
from controllers.users_controllers import *

run(host='localhost', port=8000, debug=True)
