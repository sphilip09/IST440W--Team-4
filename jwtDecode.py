#!/usr/bin/python

import jwt
key = '$ebffc391615e1b1ccc99a5621a10a65303eaee'
token = raw_input('enter token')
decode = jwt.decode(token, key, 'HS256')

print decode
