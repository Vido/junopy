import os
import base64
import requests

"""
https://github.com/Vido/junopy
"""

class JunoClient():
    """
    https://dev.juno.com.br/api/v2#operation/getAccessToken
    """
    def __init__(self, baseurl, client_id, client_secret):
        self.credentials = base64.b64encode(
            f'{client_id}:{client_secret}'.encode('ascii')
        ).decode('ascii')
        self.baseurl = baseurl
        self.auth = {}

    def _request_token(self):
        """
        https://dev.juno.com.br/api/v2#tag/Autorizacao
        """
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': f'Basic {self.credentials}'
        }
        data = {'grant_type': 'client_credentials'}
        response = requests.post(
            os.path.join(self.baseurl, 'authorization-server/oauth/token'),
            headers=headers, data=data)
        return response

    def _authenticated(self):
        # TODO: Verificar se o token expirou
        if not self.auth:
            response = self._request_token()
            self.auth = response.json()

    def _post(self, route, *args, **kwargs):
        """
        """
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Authorization': f'Bearer {self.auth["access_token"]}',
            'X-Api-Version': 2,
        }
        self._authenticated()
        response = requests.post(
            os.path.join(self.baseurl, route),
            headers=self.headers, *args, **kwargs)
        return response

    def create_charge(self, charge, billing):
        """
        https://dev.juno.com.br/api/v2#operation/createCharge
        """
        # TODO
        pass

    def list_charges(self):
        """
        https://dev.juno.com.br/api/v2#operation/listCharges
        """
        # TODO
        pass
