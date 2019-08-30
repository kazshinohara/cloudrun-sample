import os

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    target = os.environ.get('TARGET', 'World')
    return 'Hello {}!\n'.format(target)
    # host_header = request.headers.get("Host")
    # if host_header:
    #   return host_header
    # else:
    #   return target

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
    