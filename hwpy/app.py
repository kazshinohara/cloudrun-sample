import os
import redis

from flask import Flask, request

app = Flask(__name__)

redis_client = redis.Redis(host = '10.118.164.123',port = 6379, decode_responses = True)

@app.route('/')
def hello_world():
    redis_client.set('key1', 'value1')
    target = redis_client.get('key1')
    # target = os.environ.get('TARGET', 'World')
    return 'Hello {}!\n'.format(target)
    # host_header = request.headers.get("Host")
    # if host_header:
    #   return host_header
    # else:
    #   return target

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
    
