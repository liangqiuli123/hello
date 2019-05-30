# -*- coding: utf-8 -*-

import requests as req
import json

apiURL='{url}?{question}'.format(
url = 'https://api.ownthink.com/bot?spoken=',
question = '谭咏麟'
)
r = req.get(apiURL)
obj = json.loads(r.text)
print(obj)
del r
