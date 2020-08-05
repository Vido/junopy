import pytest
from decouple import config
from juno import JunoClient

JUNO_CLIENT_ID = config('JUNO_CLIENT_ID')
JUNO_SECRET = config('JUNO_SECRET')

def test_request_token():
    client = JunoClient(
        'https://sandbox.boletobancario.com/api-integration',
        JUNO_CLIENT_ID,
        JUNO_SECRET
    )
    response = client._request_token()
    from IPython import embed; embed()
    assert response.status_code == 200