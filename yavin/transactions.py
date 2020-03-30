import requests


class Endpoint:
    endpoint = NotImplemented
    data = None
    meta = None
    raw_response = None
    headers = {
        'Content-Type': 'application/json'
    }
    context = {}

    def get(self, params=None):
        if params is None:
            params = {}
        params['yavin_secret'] = self.context['yavin_secret']
        return self._process_response(requests.get(self.context['url'], params, headers=self.headers))

    def _process_response(self, response):
        self.raw_response = response
        try:
            response.raise_for_status()
            self.data = response.json()['data'][self.endpoint]
            self.meta = response.json()['meta']
        except Exception as e:
            try:
                print("Error {} : {} at url : {}".format(
                    response.json()['meta']['code'],
                    response.json()['meta']['message'],
                    self.context['url']
                ))
            except:
                print(e)

        return self.data


class TransactionsEndpoint(Endpoint):
    endpoint = 'transactions'

    def __init__(self, client):
        self.context.update(client.context)
        self.context['endpoint'] = self.endpoint
        self.context['url'] = '/'.join([self.context['api_url'], self.context['version'], self.endpoint])
