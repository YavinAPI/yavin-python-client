# Yavin API Python Client

Python client for Yavin API

## Getting started

Register or sign up to get your developer API key: [my.yavin.com](https://my.yavin.com)

Read our documentation: [api.yavin.com/docs](https://api.yavin.com/docs/?python)

## Install 

    pip install yavin


## Example

```python
from yavin import Client

yavin_client = Client('<yavin_secret_key>')
yavin_client.transactions.get({
    'start_date': '2019-12-12',
    'end_date': '2020-03-03',
    'limit': 2
})
print(yavin_client.transactions.data)
```



Learn more about our Yavin : [www.yavin.com](https://www.yavin.com)
