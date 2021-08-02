# google translate tts

import base64
import requests
import urllib.parse

gt_url = 'https://translate.google.cn/_/TranslateWebserverUi/data/batchexecute'

headers = {'Content-Type':'application/x-www-form-urlencoded;charset=utf-8'}


text = '河南加油，河南挺住'

req = "[[[\"jQ1olc\",\"[\\\""+text+"\\\",\\\"zh-CN\\\",true]\",null,\"generic\"]]]"

req = urllib.parse.quote(req.encode("utf-8"))
data = "f.req="+req

r = requests.post(url=gt_url,data=data,headers=headers)

tts_encode = r.text.split(',')[2][4:-4]

tts = base64.b64decode(tts_encode)

with open("output.mp3","wb") as f:
	f.write(tts)
