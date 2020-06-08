import os
import redis

from flask import Flask, request

app = Flask(__name__)

# Pre-requisite
# 1. set up Serverless VPC access
#    https://cloud.google.com/vpc/docs/configure-serverless-vpc-access
# 2. set up Cloud Memorystore (Redis)
#    https://cloud.google.com/memorystore/docs/redis/creating-managing-instances

redis_client = redis.Redis(host = '10.118.164.123',port = 6379, decode_responses = True)

@app.route('/')
def hello_world():
    redis_client.set('key1', 'value1')
    target = redis_client.get('key1')
    return 'Hello {}!\n'.format(target)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
    
