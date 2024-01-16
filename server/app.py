#!/usr/bin/env python3
# Application and Request Contexts
# Application Context in Flask represents the state of the Flask application. It is a context within which the entire application runs.
# why:  maintain global state that needs to be accessed throughout the application's lifecycle.

import os
# Request Context in Flask represents the state of a single HTTP request.
# why :store information about the current request, such as request parameters, session data, and the current user.
from flask import Flask,request,current_app,g,make_response

app = Flask(__name__)

@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())

@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = current_app.name
    response_body =  f'{host} && {appname} && {g.path}'

    status_code = 200
    headers = {}

    return make_response(response_body, status_code, headers)
if __name__ == '__main__':
    app.run(port=5555, debug=True)
