from .transactions import TransactionsEndpoint


class Client:
    API_URL = 'https://api.yavin.com/api'

    def __init__(self, api_key, version='v1'):
        self.version = version
        self.context = {
            'yavin_secret': api_key,
            'version': version,
            'api_url': self.API_URL
        }

        self.transactions = TransactionsEndpoint(self)

