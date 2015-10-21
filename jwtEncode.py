#!/usr/bin/python

import jwt
#header

{
  "typ": "JWT",
  "alg": "HS256",
}

#//claims
{
  "soap": "123",
}


key = '$ebffc391615e1b1ccc99a5621a10a65303eaee'
payload = {'soap':'123',}
token = jwt.encode(payload, key, 'HS256')

print token

#decode = jwt.decode(token, key, 'HS256')

#print decode

