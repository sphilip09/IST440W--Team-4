from soaplib.client import make_service_client
from test import HelloService
client = make_service_client('http://localhost:8080/hello', HelloService())
test = raw_input('Type in Hello')
response = client.hello('Who is Sheena- this is a testing')
print response
