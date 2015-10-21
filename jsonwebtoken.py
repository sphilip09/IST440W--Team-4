import jwt
import json

key = 'what_is_this_key?'
def encode (payload):
        return  jwt.encode(payload, key, 'HS256')


def decode (encodedStr):
        return jwt.decode(encodedStr, key, 'HS256')

def isValid(encoded):
  try:
    decode(encoded)
  except ValueError, e:
    return False
  return True

def getJsonData(obj):
        jsonObj = json.dumps(obj)
        return json.loads(jsonObj)
