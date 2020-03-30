from yavin import Client

yavin_client = Client('<yavin_secret_key>')
yavin_client.transactions.get({
    'start_date': '2019-12-12',
    'end_date': '2020-03-03',
    'limit': 2
})
print(yavin_client.transactions.data)


