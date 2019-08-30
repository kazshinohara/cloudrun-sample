import os

from flask import Flask
from requests import get

app = Flask(__name__)

receiving_service_url = "https://backend-tmp-q6vo4odwpq-uc.a.run.app"

# Set up metadata server request
# See https://cloud.google.com/compute/docs/instances/verifying-instance-identity#request_signature
metadata_server_token_url = 'http://metadata/computeMetadata/v1/instance/service-accounts/default/identity?audience='

token_request_url = metadata_server_token_url + receiving_service_url
token_request_headers = {'Metadata-Flavor': 'Google'}


@app.route('/')
def hello_world():
    # Fetch the token
    token_response = get(token_request_url, headers=token_request_headers)
    jwt = token_response.content.decode("utf-8")

    # Provide the token in the request to the receiving service
    receiving_service_headers = {'Authorization': 'bearer {}'.format(jwt)}

    response = get(receiving_service_url,  headers=receiving_service_headers)
    return 'I could get {} from backend services\n'.format(response.text)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

