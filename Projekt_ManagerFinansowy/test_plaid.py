from plaid import Client
Client(
    client_id=os.environ['CLIENT_ID'],
    secret=os.environ['SECRET'],
    environment='sandbox',
    api_version="2020-09-14",
    client_app="plaid-python-unit-tests"
)